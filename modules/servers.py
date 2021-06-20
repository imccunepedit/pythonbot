import subprocess
import os

from modules.getvars import getPaths

base, templates, servers = getPaths()


def listVers(what: str):
	if what == 'versions':
		return subprocess.check_output(f'ls {templates} --hide=*installer*'.split(), text=True)
	else:
		return subprocess.check_output(f'ls {servers} --hide=*installer*'.split(), text=True)


def new(name: str, version: str):
	os.system(f'cp -R {templates}/{version} {servers}/{name}')

def start(name):
	os.system(f'')