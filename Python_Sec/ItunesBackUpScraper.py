import os, sqlite3, optparse

def isMessageTable(iPhoneDB):
	try:
		conn = sqlite3.connect(iPhoneDB)
		cur = conn.cursor()
		cur.execute("SELECT * FROM sqlite_master WHERE type==\"table\";")
		for row in cur:
			if 'message' in str(row):
				return True
	except: 
		return False


def printMessage(msgDB):

	try:
		conn = sqlite3.connect(msgDB)
		cur = conn.cursor()
		cur.execute('SELECT datetime(date,"unixepoch"), address, text FROM message WHERE address>0;')

		for row in cur:

		date = str(row[0])
		address = str(row[1])
		text = str(row[2])

		print '\nDate: '+date+'Address: '+address+'Message: '+message
	except:
		pass

def main():

	parser = optparse.OptionParser('Usage%prog' + '-p <iPhone backup directory>')
	parser.add_option('-p', dest='backup', type='string', help='specify the backup directory')
	(options, args) = parser.parse_args()
	pathName = options.backup
	if pathName == None:
		print parser.usage 
		exit(0)
	else:
		dirList = os.listdir(pathName)
		for fileName in dirList:
			try:
				print '[*] ----Messages found------'
				printMessage(iPhoneDB)
			except:
				pass

if __name__ == "__main__":
	main()