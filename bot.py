# bot.py

# import discord, discord extension, and discord slash commands
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_commands import create_choice, create_option, create_permission, get_all_commands, remove_all_commands



# import other libraries
import os
from dotenv import load_dotenv


# load environment variables of bot and server id
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('DISCORD_GUILD'))

# load environment variable of different role and user ids
OWNER = int(os.getenv('DISCORD_BOTOWNER'))
ADMIN = int(os.getenv('DISCORD_ADMIN'))
EVERYONE = int(os.getenv('DISCORD_EVERYONE'))

# turn the guild id into a list for use in slash commands
guild_ids = [GUILD]


# create bot with ! prefix and all intents 
# and create slash commands from the bot and make sure they sync on startup
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

# print to console that the bot is ready
@bot.event
async def on_ready():
	print("Ready!")
	print(f"{bot.latency*1000} (ms)")



#ping the bot
@slash.slash(
	guild_ids=guild_ids,
	name="ping",
	description="ping the bot")
async def _ping(ctx):
	# create and embed and print the latency to console then send the embed
	embed=discord.Embed(title="Pong!", description=f"{bot.latency*1000} (ms)", color=0x2497d6)
	print(f"ping {bot.latency*1000} (ms)")
	await ctx.send(embed = embed)


# stop the bot from the server
@slash.slash(
	guild_ids=guild_ids,
	name='stop',
	description='kill the bot',
	permissions={
		GUILD: [
		create_permission(EVERYONE, SlashCommandPermissionType.ROLE, False),
		create_permission(ADMIN, SlashCommandPermissionType.ROLE, False),
		create_permission(OWNER, SlashCommandPermissionType.USER, True),
		]
	})
async def _stop(ctx):
	await ctx.send("stopping bot", hidden=True)
	print("stopping bot")
	await ctx.bot.close()


@slash.slash(
	guild_ids=guild_ids,
	name='removeall',
	description='remove all commands',
	permissions={
		GUILD: [
		create_permission(EVERYONE, SlashCommandPermissionType.ROLE, False),
		create_permission(ADMIN, SlashCommandPermissionType.ROLE, False),
		create_permission(OWNER, SlashCommandPermissionType.USER, True),
		]
	})
async def _removeall(ctx):
	resp = await (remove_all_commands(855675247675179019, TOKEN, [GUILD]))
	print(resp)
	await ctx.send('done', hidden=True)

@slash.slash(
	guild_ids=guild_ids,
	name='getall',
	description='get lsit of global commands or commands of a guild',
	permissions={
		GUILD: [
		create_permission(EVERYONE, SlashCommandPermissionType.ROLE, False),
		create_permission(ADMIN, SlashCommandPermissionType.ROLE, False),
		create_permission(OWNER, SlashCommandPermissionType.USER, True),
		]
	},
	options=[
		create_option(
			name='guild',
			description='get list of commands in this servevr',
			option_type=4,
			required=False
		)
	])
async def _getall(ctx, guild: int=None):
	resp = await (get_all_commands(855675247675179019, TOKEN, guild))
	print(resp)
	await ctx.send('done', hidden=True)




# run the bot
bot.run(TOKEN)
