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







temp = {
    "discord":{
        "token": "AAAABBBBCCCCDDDDEEEEFFFF.GGGGGG.HHHHIIIIJJJJKKKKLLLLMMMMNNN",
        "guild": [111111111111111111],
    
        "owner": 111111111111111111,
        "admin": 111111111111111111,
        "everyone": 111111111111111111
    },
    "minecraft": {
        "basepath": "mcservers/", 
        "templates": "templates/",
        "servers": "servers/"
    }

    
}


if __name__=="__main__":
	# create new file from template if it doesn't exist

	try:
		with open('settings.json', 'r') as f:
			print('file exists')
	except FileNotFoundError:
		with open('settings.json', 'w') as f:
			json.dump(temp, f, indent='\t')
		