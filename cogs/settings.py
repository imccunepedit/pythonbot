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


class Settings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	### ping the bot
	@cog_ext.cog_slash(
		name='ping',
		description='ping the bot',
		guild_ids=guild_ids
		)
	async def ping(self, ctx):
		# create and embed and print the latency to console then send the embed
		embed=discord.Embed(title="Pong!", description=f"{self.bot.latency*1000} (ms)", color=0x2497d6)
		print(f"ping {self.bot.latency*1000} (ms)")
		await ctx.send(embed = embed)



	# stop the bot from the server
	@cog_ext.cog_slash(
		guild_ids=guild_ids,
		name='stop',
		description='kill the bot',
		permissions=ownerPerm
		)
	async def stop(ctx):
		await ctx.send("stopping bot", hidden=True)
		print("stopping bot")
		await ctx.bot.close()



	# remove all commands
	@cog_ext.cog_slash(
		guild_ids=guild_ids,
		name='removeall',
		description='remove all commands',
		permissions=ownerPerm
		)
	async def removeall(ctx):
		resp = await (manage_commands.remove_all_commands(855675247675179019, TOKEN, [GUILD]))
		print(resp)
		await ctx.send('done', hidden=True)


	# gett all commands
	@cog_ext.cog_slash(
		guild_ids=guild_ids,
		name='getall',
		description='get lsit of global commands or commands of a guild',
		permissions=ownerPerm,
		options=[
			manage_commands.create_option(
				name='guild',
				description='get list of commands in this servevr',
				option_type=4,
				required=False
			)
		])
	async def getall(ctx, guild: int=None):
		resp = await (manage_commands.get_all_commands(855675247675179019, TOKEN, guild))
		print(resp)
		await ctx.send('done', hidden=True)









def setup(bot: commands.Bot):
	bot.add_cog(Settings(bot))



