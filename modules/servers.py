import subprocess
import os

from modules.getvars import getPaths

base, templates, server = getPaths()


def listVersion():
	return subprocess.check_output(f'ls {templates} --hide=*installer*'.split(), text=True)