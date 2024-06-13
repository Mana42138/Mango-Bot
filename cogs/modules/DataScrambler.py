import os


import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

async def check_private(context: discord.Interaction):
    try:
        if not context.guild:
            embed = discord.Embed(title="Error", description=f"This command must be executed in a guild!", color=0xE74C3C)
            await context.response.send_message(embed=embed, ephemeral=True)
            return True
        else:
            return False
    except Exception as e:
        return True
    
def find_python_files(folder_path):
    python_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files

def default_permissions(role):
    if role.administrator or role.ban_members or role.kick_members or role.manage_guild or role.manage_roles or role.moderate_members:
        return True
    return False
    
    
async def get_roles(context: discord.Interaction):
    if not await check_private(context):
        try:
            for role in context.user.roles:
                role_prem = role.permissions
                if default_permissions(role_prem):
                    return True
                return False
        except Exception as e:
            print(f"{e} get_roles()")
            return False
    else:
        return False
    
async def check_has_premissions(context: discord.Interaction):
    try:
        if await get_roles(context):
            return True
        return False
    except Exception as e:
        print(f"{e} check_has_premissions()")
        return True