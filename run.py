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
	print('	Instagram scraper: osintgram, instagram-scraper, instaloader')
	print('	OWASP Amass: amass')
	print('	IntelOwl: intelowl')
	print('	email2phonenumber')
	print('	Tracker: trape')
	print('	goohak')
	print('	Tidos Framework: tidv2, tidconsole')
	print('	Moriarty-Project: moriarty')
	print('	ReconDog: dog')
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
	elif shl[:5]=='amass':
		os.system('cd tools/amass_linux_amd64 && ./%s' % shl)
	elif shl[:9]=='osintgram':
		os.system('cd tools/Osintgram && python3 main.py %s' % shl[10:])
	elif shl[:8]=='intelowl':
		os.system('cd tools/IntelOwl && python3 start.py %s' % shl[9:])
	elif shl[:17]=='email2phonenumber':
		os.system('cd tools/email2phonenumber && python3 email2phonenumber.py %s' % shl[18:])
	elif shl[:5]=='trape':
		os.system('cd tools/trape && python3 trape.py %s' % shl[6:])
	elif shl[:6]=='goohak':
		os.system('cd tools/goohak && ./goohak %s' % shl[7:])
	elif shl[:5]=='tidv2':
		os.system('cd tools/tidos-framework && python3 tidv2 %s' % shl[6:])
	elif shl[:5]=='tidconsole':
		os.system('cd tools/tidos-framework && python3 tidconsole.py %s' % shl[6:])
	elif shl[:8]=='moriarty':
		os.system('cd tools/Moriarty-Project && python3 Moriarty.py %s' % shl[9:])
	elif shl[:3]=='dog':
		os.system('cd tools/ReconDog && python3 %s' % shl)
	elif shl=='help':
		usage()
	elif shl=='exit' or shl=='bye':
		break
	else:
		os.system('%s' % shl)
