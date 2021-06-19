import json

from discord_slash.model import SlashCommandPermissionType
from discord_slash.utils.manage_commands import create_permission






def getVars(var: str):
    vars = json.load(open('settings/settings.json'))
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



TOKEN = getVars('token')
GUILD = getVars('guild')
OWNER = getVars('owner')
ADMIN = getVars('admin')
EVERYONE = getVars('everyone')