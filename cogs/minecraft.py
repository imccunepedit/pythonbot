import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils import manage_commands

from getvars import getVars, getPerm

TOKEN = getVars('token')
GUILD = getVars('guild')
OWNER = getVars('owner')
ADMIN = getVars('admin')
EVERYONE = getVars('everyone')

ownerPerm = getPerm('owner')


guild_ids = [GUILD]

class Minecraft(commands.Cog):
    @cog_ext.cog_slash(
        guild_ids=guild_ids,
        name='mcver',
        description='list avaliable server version')
    async def mcver(ctx):
        
        print('executed mcver')