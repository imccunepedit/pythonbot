from os import name
import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option

from modules.getvars import getDiscordVars, getPerm
import modules.servers as mcservers


ownerPerm = getPerm('owner')


guild_ids = getDiscordVars('guild')

class Minecraft(commands.Cog):
	def __init__(self, bot):
			self.bot = bot

	# list minecraft version or servers
	@cog_ext.cog_slash(
		guild_ids=guild_ids,
		name='mclist',
		description='list avaliable server version/types',
		options=[
			create_option(
				name='what',
				description='servers or versions',
				option_type=3,
				required=True,
				choices=[
					create_choice(
						name='versions',
						value='versions'
					),
					create_choice(
						name='servers',
						value='servers'
					)
				]
			)
		])
	async def mclist(self, ctx, what: str):
		print('executed mclist')
		await ctx.send(mcservers.list(what))



	# create a new minecraft server from a supplied version and name
	@cog_ext.cog_slash(
		guild_ids=guild_ids,
		name='mcnew',
		description='new minecraft server',
		options=[
			create_option(
				name='name',
				description='name for the minecraft server, used in various places for naming and will appear in server list',
				option_type=3,
				required=True
			),
			create_option(
				name='version',
				description='version or type of server to create',
				option_type=3,
				required=True
			),
		])
	async def mcnew(self, ctx, name: str, version: str):
		print('executed mcnew')
		mcservers.new(name, version)
		embed=discord.Embed(title="New server", description="new server created", color=0x01bc4f)
		embed.add_field(name="Name", value=name, inline=False)
		embed.add_field(name="Verion", value=version, inline=False)
		await ctx.send(embed=embed)



	@cog_ext.cog_slash(
		guild_ids=guild_ids,
		name='mcstart',
		description='start an existing minecraft server',
		options=[
			create_option(
				name='name',
				description='name of server to be started',
				option_type=3,
				required=True
			)
		])
	async def mcstart(self, ctx, name: str):
		print('executed mcstart')
		mcservers.start(name)
		await ctx.send('started server')






def setup(bot: commands.Bot):
	bot.add_cog(Minecraft(bot))
