import subprocess
import os

from modules.getvars import getPaths

base, templates, servers = getPaths()


def list(what):
	if what == 'versions':
		out = subprocess.check_output(f'ls {templates} --hide=*installer*'.split(), text=True)
	else:
		out =  subprocess.check_output(f'ls {servers} --hide=*installer*'.split(), text=True)
	if out == '':
		out = 'no servers or versions where found'
	return out


def new(name, version):
	os.system(f'cp -R {templates}{version} {servers}{name}')

def start(name):
	# creates a new screen with the name of the server and then runs commands in that screen to run the start up script
	os.system(f'screen -dmS mc-{name} bash -c "cd {servers}{name}; bash -c ./start.sh"')
