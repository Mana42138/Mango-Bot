
import os
import json
from turtle import title
from types import NoneType
from .modules.DataScrambler import *
from .modules.Obfuscation import *


import discord
from discord import app_commands, file
from discord.ext import commands
from discord.ext.commands import Context

def find_python_files(folder_path):
    python_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files

class Owner(commands.Cog, name="owner"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(
        name="sync",
        description="Synchonizes the slash commands.",
    )
    @app_commands.describe(scope="The scope of the sync. Can be `global` or `guild`")
    @commands.is_owner()
    async def sync(self, context: discord.Interaction, scope: str):
        """
        Synchonizes the slash commands.

        :param context: The command context.
        :param scope: The scope of the sync. Can be `global` or `guild`.
        """

        if scope == "global":
            await app_commands.tree.CommandTree.sync()
            embed = discord.Embed(
                description="Slash commands have been globally synchronized.",
                color=0xBEBEFE,
            )
            await context.response.send_message(embed=embed)
            return
        elif scope == "guild":
            app_commands.tree.CommandTree.copy_global_to(guild=context.guild)
            await app_commands.tree.CommandTree.sync(guild=context.guild)
            embed = discord.Embed(
                description="Slash commands have been synchronized in this guild.",
                color=0xBEBEFE,
            )
            await context.response.send_message(embed=embed)
            return
        embed = discord.Embed(
            description="The scope must be `global` or `guild`.", color=0xE02B2B
        )
        await context.response.send_message(embed=embed)

    @commands.command(
        name="unsync",
        description="Unsynchonizes the slash commands.",
    )
    @app_commands.describe(
        scope="The scope of the sync. Can be `global`, `current_guild` or `guild`"
    )
    @commands.is_owner()
    async def unsync(self, context: discord.Interaction, scope: str) -> None:
        """
        Unsynchonizes the slash commands.

        :param context: The command context.
        :param scope: The scope of the sync. Can be `global`, `current_guild` or `guild`.
        """

        if scope == "global":
            app_commands.tree.CommandTree.clear_commands(guild=None)
            await app_commands.tree.CommandTree.sync()
            embed = discord.Embed(
                description="Slash commands have been globally unsynchronized.",
                color=0xBEBEFE,
            )
            await context.response.send_message(embed=embed)
            return
        elif scope == "guild":
            app_commands.tree.CommandTree.clear_commands(guild=context.guild)
            await app_commands.tree.CommandTree.sync(guild=context.guild)
            embed = discord.Embed(
                description="Slash commands have been unsynchronized in this guild.",
                color=0xBEBEFE,
            )
            await context.response.send_message(embed=embed)
            return
        embed = discord.Embed(
            description="The scope must be `global` or `guild`.", color=0xE02B2B
        )
        await context.response.send_message(embed=embed)

    @app_commands.command(
        name="load",
        description="Load a cog",
    )
    @app_commands.describe(cog="The name of the cog to load")
    @commands.is_owner()
    async def load(self, context: discord.Interaction, cog: str) -> None:
        """
        The bot will load the given cog.

        :param context: The hybrid command context.
        :param cog: The name of the cog to load.
        """
        try:
            await self.bot.load_extension(f"cogs.{cog}")
        except Exception:
            embed = discord.Embed(
                description=f"Could not load the `{cog}` cog.", color=0xE02B2B
            )
            await context.response.send_message(embed=embed)
            return
        embed = discord.Embed(
            description=f"Successfully loaded the `{cog}` cog.", color=0xBEBEFE
        )
        await context.response.send_message(embed=embed)

    @app_commands.command(
        name="unload",
        description="Unloads a cog.",
    )
    @app_commands.describe(cog="The name of the cog to unload")
    @commands.is_owner()
    async def unload(self, context: discord.Interaction, cog: str) -> None:
        """
        The bot will unload the given cog.

        :param context: The hybrid command context.
        :param cog: The name of the cog to unload.
        """
        try:
            await self.bot.unload_extension(f"cogs.{cog}")
        except Exception:
            embed = discord.Embed(
                description=f"Could not unload the `{cog}` cog.", color=0xE02B2B
            )
            await context.response.send_message(embed=embed)
            return
        embed = discord.Embed(
            description=f"Successfully unloaded the `{cog}` cog.", color=0xBEBEFE
        )
        await context.response.send_message(embed=embed)
        
    async def reload_python_files(self, bot):
        script_directory = os.path.dirname(os.path.realpath(__file__))
        py_files = find_python_files(script_directory)
        for file in py_files:
            if file.endswith(".py"):
                file = os.path.splitext(file)[0]
                file = os.path.relpath(file, script_directory).replace(os.sep, ".")
            file = os.path.splitext(file)[0]
            file = os.path.relpath(file, script_directory).replace(os.sep, ".")
            try:
                await bot.reload_extension(f"cogs.{file}")
            except Exception as e:
                print(f"Failed to reload extension {file}: {e}")

    @app_commands.command(
        name="reload",
        description="Reloads a cog.",
    )
    @app_commands.describe(cog="The name of the cog to reload")
    @commands.is_owner()
    async def reload(self, context: discord.Interaction, *, cog: str = None) -> None:
        """
        The bot will reload the given cog.

        :param context: The hybrid command context.
        :param cog: The name of the cog to reload.
        """
        try:
            if cog == None:
                await self.reload_python_files(self.bot)
                cog = "All"
            else:
                await self.bot.reload_extension(f"cogs.{cog}")
        except Exception:
            embed = discord.Embed(
                description=f"Could not reload the `{cog}` cog.", color=0xE02B2B
            )
            await context.response.send_message(embed=embed)
            return
        embed = discord.Embed(
            description=f"Successfully reloaded the `{cog}` cog.", color=0xBEBEFE
        )
        await context.response.send_message(embed=embed)

    @app_commands.command(
        name="shutdown",
        description="Make the bot shutdown.",
    )
    @commands.is_owner()
    async def shutdown(self, context: discord.Interaction) -> None:
        """
        Shuts down the bot.

        :param context: The hybrid command context.
        """
        embed = discord.Embed(description="Shutting down. Bye! :wave:", color=0xBEBEFE)
        await context.response.send_message(embed=embed)
        await self.bot.close()

    @app_commands.command(
        name="say",
        description="The bot will say anything you want.",
    )
    @app_commands.describe(message="The message that should be repeated by the bot")
    @commands.is_owner()
    async def say(self, context: discord.Interaction, *, message: str) -> None:
        """
        The bot will say anything you want.

        :param context: The hybrid command context.
        :param message: The message that should be repeated by the bot.
        """
        await context.response.send_message(message)
        
    @app_commands.command(
        name="embed",
        description="The bot will say anything you want, but within embeds.",
    )
    @app_commands.describe(message="The message that should be repeated by the bot")
    @commands.is_owner()
    async def embed(self, context: discord.Interaction, *, message: str) -> None:
        """
        The bot will say anything you want, but using embeds.

        :param context: The hybrid command context.
        :param message: The message that should be repeated by the bot.
        """
        embed = discord.Embed(description=message, color=0xBEBEFE)
        await context.response.send_message(embed=embed)

    @app_commands.command(
        name="datasetup",
        description="Data setup.",
    )
    @commands.is_owner()
    async def datasetup(self, context: discord.Interaction, *, name: str = "") -> None:
        """
        Test Bot Data

        :param context: The hybrid command context.
        :param name: The name that should be added by the bot.
        """
        
        if await check_private(context):
            return
        
        if await check_has_premissions(context):
            print("roles not found!")
            return

        parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        file_path = os.path.join(parent_dir, "database", "database.json")
        
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        try:
            guild_id = str(context.guild.id)
            guild_data = data.get(guild_id, {})
            guild_data["Name"] = name or ""
            data[guild_id] = guild_data

            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(e)

        embed = discord.Embed(description=f"Adding {name} to the server data!", color=0xBEBEFE)
        await context.response.send_message(embed=embed)
        
    @app_commands.command(
        name="obfuscate",
        description="Obfuscate Data",
    )
    @commands.is_owner()
    async def obfuscat(self, context: discord.Interaction, file: discord.Attachment) -> None:
        """
        Test bot obfuiscation

        :param context: The hybrid command context.
        :param file: The File data you want to obfuscate
        """
        
        try:
            obfuscated_file = await Obfuscate(file)
        except Exception as e:
            print(e)
            pass

        embed = discord.Embed(description=f"Testing Obfuscation", color=0xBEBEFE)
        await context.response.send_message(file=obfuscated_file)

        obfuscated_file.close()

        os.remove(obfuscated_file.fp.name)
        
    @app_commands.command(
        name="deobfuscate",
        description="DeObfuscate Data",
    )
    @commands.is_owner()
    async def deobfuscat(self, context: discord.Interaction, file: discord.Attachment) -> None:
        """
        Test bot deobfuiscation

        :param context: The hybrid command context.
        :param file: The File data you want to obfuscate
        """
        
        try:
            obfuscated_file = await DeObfuscate(file)
        except Exception as e:
            print(e)
            pass

        embed = discord.Embed(description=f"Still in experimental phase", color=0xBEBEFE)
        await context.response.send_message(embed=embed, file=obfuscated_file)
        
        obfuscated_file.close()

        os.remove(obfuscated_file.fp.name)

async def setup(bot):
    await bot.add_cog(Owner(bot))
