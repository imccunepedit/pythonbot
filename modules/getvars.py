import json

from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_commands import create_permission


with open('settings.json') as f:
	s = json.load(f)


def getDiscordVars(var: str):
    vars = s['discord']
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
	a = s['minecraft']
	b = a['basepath']
	return b, b+a['templates'], b+a['servers']
	




TOKEN = getDiscordVars('token')
GUILD = getDiscordVars('guild')[0]
OWNER = getDiscordVars('owner')
ADMIN = getDiscordVars('admin')
EVERYONE = getDiscordVars('everyone')