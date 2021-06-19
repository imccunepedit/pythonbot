# bot.py

# import discord, discord extension, and discord slash commands
import discord
from discord.ext import commands
from discord_slash import SlashCommand


# import other libraries
from .getvars import getVars


# load environment variables of bot and server id

TOKEN = getVars('token')
GUILD = getVars('guild')



# create bot with ! prefix and all intents 
# and create slash commands from the bot and make sure they sync on startup
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)

# print to console that the bot is ready
@bot.event
async def on_ready():
	print("Ready!")
	print(f"{bot.latency*1000} (ms)")


# load cogs
bot.load_extension('cogs.settings')


# run the bot
bot.run(TOKEN)
