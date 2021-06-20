import json
import discord

from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_commands import create_permission






def getDiscordVars(var: str):
    vars = json.load(open('settings.json'))['discord']
    return vars[var]

def getPerm(perm: str):
    if perm == 'owner':
        return {
			GUILD: [
			create_permission(EVERYONE, SlashCommandPermissionType.ROLE, False),
			create_permission(OWNER, SlashCommandPermissionType.USER, True),
			]
		}
    elif perm == 'admin':
        return {
			GUILD: [
			create_permission(EVERYONE, SlashCommandPermissionType.ROLE, False),
			create_permission(ADMIN, SlashCommandPermissionType.ROLE, True),
			create_permission(OWNER, SlashCommandPermissionType.USER, True),
			]
		}
    else:
        return {
			GUILD: [
			create_permission(EVERYONE, SlashCommandPermissionType.ROLE, True)
			]
		}


def getPaths():
	a = json.load(open('settings.json'))['minecraft']
	b = a['basepath']
	return b, b+a['templates'], b+a['servers']
	






TOKEN = getDiscordVars('token')
GUILD = getDiscordVars('guild')[0]
OWNER = getDiscordVars('owner')
ADMIN = getDiscordVars('admin')
EVERYONE = getDiscordVars('everyone')