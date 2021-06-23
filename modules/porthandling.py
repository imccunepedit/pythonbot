import json



def getPorts(key: str=''):
	with open('ports.json') as f:
		if key =='':
			return json.load(f)
		else:
			return json.load(f)[key]

def setPorts(p):
	with open('ports.json', 'w') as f:
		json.dump(p, f, indent='\t')


def getMinMax(w: str=''):
	p = getPorts('minmax')
	if w == '':
		return p
	else:
		return p[w]




def getUsing():
	p = getPorts()
	if len(p['unused']) == 0:
		return 1
	port = p['unused'][0]
	p['unused'].remove(port)
	p['used'] += [port]
	setPorts(p)
	return port


def resetPorts():
	p = getPorts()
	p['used'] = []
	p['unused'] = list(range(getMinMax('min'), getMinMax('max')+1))
	setPorts(p)



t = getPorts()
if t['unused'] == [] and t['used'] == []:
	resetPorts()
		
	





temp = {
	"used": [],
	"unused": [],
	"minmax": {
		"min": 0,
		"max": 0
	}
}
if __name__=="__main__":
	# create new file from template if it doesn't exist
	try:
		with open('ports.json', 'r') as f:
			print('file exists')
	except FileNotFoundError:
		with open('ports.json', 'w') as f:
			json.dump(temp, f, indent='\t')
