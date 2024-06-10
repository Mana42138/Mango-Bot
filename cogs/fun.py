
import random
import os
import sys
import json

import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context


class Choice(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.value = None

    @discord.ui.button(label="Heads", style=discord.ButtonStyle.blurple)
    async def confirm(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ) -> None:
        self.value = "heads"
        self.stop()

    @discord.ui.button(label="Tails", style=discord.ButtonStyle.blurple)
    async def cancel(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ) -> None:
        self.value = "tails"
        self.stop()


class RockPaperScissors(discord.ui.Select):
    def __init__(self) -> None:
        options = [
            discord.SelectOption(
                label="Scissors", description="You choose scissors.", emoji="✂"
            ),
            discord.SelectOption(
                label="Rock", description="You choose rock.", emoji="🪨"
            ),
            discord.SelectOption(
                label="Paper", description="You choose paper.", emoji="🧻"
            ),
        ]
        super().__init__(
            placeholder="Choose...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction) -> None:
        choices = {
            "rock": ["🪨", 0],
            "paper": ["🧻", 1],
            "scissors": ["✂", 2],
        }
        user_choice = self.values[0].lower()
        user_choice_index = choices[user_choice][1]

        bot_choice = random.choice(list(choices.keys()))
        bot_choice_index = choices[bot_choice][1]

        result_embed = discord.Embed(color=0xBEBEFE)
        result_embed.set_author(
            name=interaction.user.name, icon_url=interaction.user.display_avatar.url
        )

        winner = (3 + user_choice_index - bot_choice_index) % 3
        if winner == 0:
            result_embed.description = f"**That's a draw!**\nYou've chosen **{user_choice}** and I've chosen **{bot_choice}**."
            result_embed.add_field(name="**Elements**", value=f"{choices[user_choice][0]} | {choices[bot_choice][0]}")
            result_embed.colour = 0xF59E42
        elif winner == 1:
            result_embed.description = f"**You won!**\nYou've chosen **{user_choice}** and I've chosen **{bot_choice}**."
            result_embed.add_field(name="**Elements**", value=f"{choices[user_choice][0]} | {choices[bot_choice][0]}")
            result_embed.colour = 0x57F287
        else:
            result_embed.description = f"**You lost!**\nYou've chosen **{user_choice}** and I've chosen **{bot_choice}**."
            result_embed.add_field(name="**Elements**", value=f"{choices[bot_choice][0]} | {choices[user_choice][0]}")
            result_embed.colour = 0xE02B2B

        await interaction.response.edit_message(
            embed=result_embed, content=None, view=None
        )


class RockPaperScissorsView(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.add_item(RockPaperScissors())


class Fun(commands.Cog, name="fun"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @app_commands.command(name="randomfact", description="Get a random fact.")
    async def randomfact(self, context: discord.Interaction) -> None:
        """
        Get a random fact.

        :param context: The hybrid command context.
        """
        # This will prevent your bot from stopping everything when doing a web request - see: https://discordpy.readthedocs.io/en/stable/faq.html#how-do-i-make-a-web-request
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://uselessfacts.jsph.pl/random.json?language=en"
            ) as request:
                if request.status == 200:
                    data = await request.json()
                    embed = discord.Embed(description=data["text"], color=0xD75BF4)
                else:
                    embed = discord.Embed(
                        title="Error!",
                        description="There is something wrong with the API, please try again later",
                        color=0xE02B2B,
                    )
                await context.response.send_message(embed=embed)

    @app_commands.command(
        name="coinflip", description="Make a coin flip, but give your bet before."
    )
    async def coinflip(self, context: discord.Interaction) -> None:
        """
        Make a coin flip, but give your bet before.

        :param context: The hybrid command context.
        """
        buttons = Choice()
        embed = discord.Embed(description="What is your bet?", color=0xBEBEFE)
        await context.response.send_message(embed=embed, view=buttons)
        await buttons.wait()  # We wait for the user to click a button.
        result = random.choice(["heads", "tails"])
        if buttons.value == result:
            embed = discord.Embed(
                description=f"Correct! You guessed **{buttons.value}** and I flipped the coin to **{result}**.",
                color=0xBEBEFE,
            )
        else:
            embed = discord.Embed(
                description=f"Woops! You guessed **{buttons.value}** and I flipped the coin to **{result}**, better luck next time!",
                color=0xE02B2B,
            )
        await context.edit_original_response(embed=embed, view=None, content=None)

    @app_commands.command(
        name="rps", description="Play the rock paper scissors game against the bot."
    )
    async def rock_paper_scissors(self, context: discord.Interaction) -> None:
        """
        Play the rock paper scissors game against the bot.

        :param context: The hybrid command context.
        """
        view = RockPaperScissorsView()
        await context.response.send_message("Please make your choice", view=view)


async def setup(bot) -> None:
    await bot.add_cog(Fun(bot))
