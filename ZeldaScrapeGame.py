import requests
import time
import csv
from bs4 import BeautifulSoup

f = open('gamesNames.txt','a')

r = requests.get('http://zeldawiki.org/Category:Games')

soup = BeautifulSoup(r.text)

nameDiv = soup.find("div", { "id" : "mw-pages" })

nameLi= nameDiv.select('li a')

for links in nameLi:

	f.write((links.text + ',' + links['href'] + '\n').encode('utf-8'))
	#triple = ''
	#triple = '<http://zeldawiki.org' + links['href'] + '>'
# the variable triple is currently not being used.
#f.close()
	f2 = open('gamesData.txt', 'a')

	r2 = requests.get('http://zeldawiki.org' + links['href'])

	time.sleep(1)

	print 'requesting:', 'http://zeldawiki.org' + links['href']

	soup2 = BeautifulSoup(r2.text)

	canonCheck = soup2.find('table', {'class' :'gradient'}) 
	if canonCheck is not None:
		checkingCanon = canonCheck.select('a')
		print "Dude, I'm gonna check the canon."
		if checkingCanon is not None:
			canonLink = raw_input('Oh schnap son! This Canon for' + ' ' + links.text + ' ' + 'is all suspect brah! Do you want me to toss her?')
		#True == 'y'
		#False == 'n'
			if canonLink == 'y':
				print "Aight, I'm tossing!"
				pass
			elif canonLink == 'n':
				print "Cool dude, I'm gonna check for a box." 
				infoBox = soup2.find('table', {'class' : 'toccolours'}) or soup2.find('table', {'class' : 'wikitable'})

				if infoBox is not None:

					print "We have a box!"

					rows = infoBox.select('tr')

					for tableHeader in rows:

						tableHeader.select('th')

						f2.write((tableHeader.text + ',').encode('utf-8'))

					for tableLinks in rows:

						MyTableLinks = tableLinks.find('a')

						if MyTableLinks is not None:
							#if MyTableLinks 
							f2.write(('\n' + MyTableLinks['href'] + ',' +'\n' + MyTableLinks.text + ',' +'\n' + tableHeader.text + ',' + '\n').encode('utf-8'))

							print "Grabbing box info brah!!!"
				else:

					print "No box info brah :( Bummer."

					f2.write('\n' + '\n' + links.text + " has no box info brah. Bummer." + '\n' + '\n')
	elif canonCheck is None: 
		infoBox = soup2.find('table', {'class' : 'toccolours'}) or soup2.find('table', {'class' : 'wikitable'})

		if infoBox is not None:

			print "We have a box"

			rows = infoBox.select('tr') 

			for tableHeader in rows:

				tableHeader.select('th')

				f2.write((tableHeader.text + ',').encode('utf-8'))

			for tableLinks in rows:

				MyTableLinks = tableLinks.find('a')

				if MyTableLinks is not None:
					#if MyTableLinks 
					f2.write(('\n' + MyTableLinks['href'] + ',' +'\n' + MyTableLinks.text + ',' +'\n' + tableHeader.text + ',' + '\n').encode('utf-8'))

					print "Grabbing box info brah!!!"
		else:

			print "No box info brah :( Bummer."

			f2.write('\n' + '\n' + links.text + " has no box info brah. Bummer." +'\n' + '\n'