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




def setUsing():
	p = getPorts()
	if len(p['unused']) == 0:
		return 1
	port = p['unused'][0]
	p['unused'].remove(port)
	p['used'] += [port]
	setPorts(p)
	return port





if __name__=="__main__":
	# open file and read contents
	p = getPorts()
	if p['unused'] == [] and p['used'] == []:
		p['unused'] = list(range(getMinMax('min'), getMinMax('max')+1))
		
	setUsing()
		
