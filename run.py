#!/usr/bin/python3
import os

def usage():
	print('Usage:')
	print('	Username search: sherlock')
	print('	Domain search: theHarvester')
	print('	Device search: shodan')
	print('	Various search: spiderfoot')
	print('	Recon-ng Framework: recon-ng, recon-web, recon-cli')
	print('	Twitter scraper: twint')
	print('	Instagram scraper: instagram-scraper')
	print('	Basic commands: help, exit')

print('Run with root to get rid of errors.')
usage()

while True:
	shl=input('> ')
	if shl[:8]=='sherlock':
		os.system('cd tools/sherlock/sherlock && python3 sherlock.py %s' % shl[9:])
	elif shl[:12]=='theHarvester' or shl[:12]=='theharvester':
		os.system('cd tools/theHarvester && python3 theHarvester.py %s' % shl[13:])
	elif shl[:8]=='recon-ng' or shl[:9]=='recon-web' or shl[:9]=='recon-cli':
		os.system('cd tools/recon-ng && ./%s' % shl)
	elif shl[:10]=='spiderfoot':
		os.system('cd tools/spiderfoot-3.3 && python3 sf.py %s' % shl[11:])
	elif shl=='help':
		usage()
	elif shl=='exit' or shl=='bye':
		break
	else:
		os.system('%s' % shl)