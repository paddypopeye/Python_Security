import re, os, optparse, sqlite3


def printDownloads(downloadDB):
	conn = sqlite3.connect(downloadDB)
	cur = conn.cursor()
	cur.execute("SELECT name, souce, datetime(endTime/1000000, 'unixepoch') FROM moz_downloads")

	print '\n[*]---Searchinf Files Downloaded'

	for row in cur:

		print '[+]File:' + str(row[0]) + 'from source ' + str(row[1])\
		+ 'at ' + str(row[2])


def printCookies(cookiesDB):
	try:
		conn =sqlite3.connect(cookiesDB)
		cur = conn.cursor()
		cur.execute("SELECT host, name, value FROM moz_cookies")

		print '[+] Found Cookies' 

		for row in cur:

			host = str(row[0])
			name = str(row[1])
			value = str(row[2])

			print '[+]Host: ' + host + 'name: ' + name + 'value: ' + value

	except Exception, e:
		if 'encrypted' in str(e):

			print '\nError reading the places DB'
			print '[*]Try upgrading your python-sqlite3 libraries'


def printHistory(placesDB):
	try:
		conn =sqlite3.connect(cookiesDB)
		cur = conn.cursor()
		cur.execute("SELECT url, datetime(visit_date/1000000, 'unixepoch')\
			FROM moz_places, moz_historyvisits\
			WHERE visit_count > 0\
			and moz_places.id == moz_historyvisits.place_id;")

		print '[*]-----History Found-----'

		for row in cur:

			url = str(row[0])
			date = str(row[1])
			print '[+] ' + date + ' Visited: ' + url

	except Exception, e:

		if 'encrypted' in str(e):
			print '\nError reading the places DB'
			print '[*]Try upgrading your python-sqlite3 libraries'



def printGoogle(placesDB):
	conn =sqlite3.connect(placesDB)
	cur = conn.cursor()
	cur.execute("SELECT url, datetime(visit_date/1000000,\
		'unixepoch')\
		FROM moz_places, moz_historyvisits\
		WHERE visit_count > 0 and moz_places.id == moz_historyvisits.place_id")
	print '[*] -----Google Searches Found-----'
	for row in cur:
		url = str(row[0])
		date = str(row[1])

		if 'google' in url.lower():
			r = re.findall(r'q=.*\&', url)
			if r:
				search = r[0].split('&')[0]
				search = search.replace('q=', '').replace('+','')
				print '[+]' + date + 'Searched for: ' + search

def main():
	parser = optparse.OptionParser('Usage%prog' + '-p <Firefox profile path>')
	parser.add_option('-p', dest='pathName', type='string', help='specify the profile path')
	(options, args) = parser.parse_args()

	pathName = options.pathName

	if pathName == None:
		print parser.usage 
		exit(0)
	elif os.path.isdir(pathName) == False:

		print '[-]The given path does not exist' + pathName
		exit(0)

	else: 
		downloadDB = os.path.join(pathName, 'downloads.sqlite3')

		if os.path.isfile(downloadDB):
			printDownloads(downloadDB)

		else:
			print '[!]Downloads DB does not exist' + downloadDB

		cookiesDB = os.path.join(pathName, 'cookies.sqlite')
		if os.path.isfile(cookiesDB):
			printCookies(cookiesDB)
		else:
			print '[!]Cookies DB does not exist' + cookiesDB

		placesDB = os.path.join(pathName, 'places.sqlite')

		if os.path.isfile(placesDB):
			printHistory(placesDB)
			printGoogle(placesDB)
		else:
			print '[!]Places DB does not exist' + placesDB

if __name__ == '__main__':
	main()