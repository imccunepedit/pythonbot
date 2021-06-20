import subprocess
import os

from modules.getvars import getPaths

base, templates, servers = getPaths()


def list(what):
	if what == 'versions':
		return subprocess.check_output(f'ls {templates} --hide=*installer*'.split(), text=True)
	else:
		return subprocess.check_output(f'ls {servers} --hide=*installer*'.split(), text=True)


def new(name, version):
	os.system(f'cp -R {templates}{version} {servers}{name}')

def start(name):
	os.system(f'screen -dmS mc-{name} bash -c {servers}{name}/start')
	# os.system(f'screen -dmS mc-{name}')
	# os.system(f'screen -X bash {servers}/{name}/start -S mc-{name}')