
import json
import os
import sys

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context


class Reminders(commands.Cog, name="reminders"):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @app_commands.command(
        name="reminder", description="Add a reminder at a spesific time."
    )
    async def help(self, context: discord.Interaction) -> None:
        
        await context.response.send_message("TEST")

async def setup(bot) -> None:
    await bot.add_cog(Reminders(bot))