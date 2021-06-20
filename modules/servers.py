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
		out = 'no servers or versoin where found'
	return out


def new(name, version):
	os.system(f'cp -R {templates}{version} {servers}{name}')

def start(name):
	os.system(f'bash -c {servers}{name}/start')
	# os.system(f'screen -dmS mc-{name}')
	# os.system(f'screen -X bash {servers}/{name}/start -S mc-{name}')