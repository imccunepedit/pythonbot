import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option

from modules.getvars import getDiscordVars, getPerm
import modules.servers as mcservers


ownerPerm = getPerm('owner')


guild_ids = getDiscordVars('guild')

class Minecraft(commands.Cog):
	def __init__(self, bot):
			self.bot = bot

	
	@cog_ext.cog_slash(
		guild_ids=guild_ids,
		name='mclist',
		description='list avaliable server version/ types')
	async def mclist(self, ctx):
		print('executed mclist')
		await ctx.send(mcservers.listVersion())




	@cog_ext.cog_slash(
		guild_ids=guild_ids,
		name='mcnew',
		description='new minecraft server',
		options=[
			create_option(
				name='sname',
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
	async def mcnew(self, ctx, sname: str, version: str):
		print('executed mcnew')

		embed=discord.Embed(title="New server", description="new server created", color=0x01bc4f)
		embed.add_field(name="Name", value=sname, inline=True)
		embed.add_field(name="Verions", value=version, inline=True)
		await ctx.send(embed=embed)








def setup(bot: commands.Bot):
	bot.add_cog(Minecraft(bot))
