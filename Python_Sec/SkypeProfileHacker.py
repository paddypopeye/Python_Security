import optparse, os, sqlite3

def printProfile(skypeDB):
	conn = sqlite3.connect(skypeDB)
	cur = conn.cursor()
	cur.execute("SELECT fullname, skypename, city, country, datetime(profile_timestamp, 'unixepoch') FROM Accounts")

	for row in cur:

		print '[*] ---Skype Account Found----'
		print '[+] User                  :' + str(row[0])
		print '[+] Skype UserName        :' + str(row[1])
		print '[+] Location              :' + str(row[2]) + '.' + str(row[3])
		print '[+] Profile Date          :' + str(row[4])

def printContacts(skypeDB):
	conn = sqlite3.connect(skypeDB)
	cur = conn.cursor()
	cur.execute("SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts")

	for row in cur:
		print '[*] ---Skype Contacts Found----'
		print '[+] User                  :' + str(row[0])
		print '[+] Skype UserName        :' + str(row[1])
		if str(row[2]) != '' and str(row[3]) != 'None':
			print '[+] Location          :' + str(row[2]) + '.' + str(row[3])
		if str(row[4]) != 'None':
			print '[+] Profile Date      :' + str(row[4])
		if str(row[5]) != 'None':
			print '[+] Birthday          :' + str(row[5])

def printCallLog(skypeDB):
	conn = sqlite3.connect(skypeDB)
	cur = conn.cursor()
	cur.execute("SELECT datetime(begin_timestamp, 'unixepoch'), identity FROM calls, conversations WHERE calls.conv_dbid = conversations.id;")

	print '[+]----Searching Vistim\'s Call History------'

	for row in cur:

		print ' [+]Time: ' + str(row[0]) + '|Partner: ' + str(row[1])

def printMessages(skypeDB):
		conn = sqlite3.connect(skypeDB)
		cur = conn.cursor()
		cur.execute("SELECT datetime(timestamp, 'unixepoch'), diag_partner, author, body_xml FROM Messages;")
		print '\n[*] ---Searching Messages------'
		for row in cur:
			try:
				if partlist not in str(row[3]):
					if str(row[1]) != str(row[2]):
						msgDirection = 'To ' + str(row[1]) + ':' 
					else:
						msgDirection = 'From ' + str(row[2]) + ':'

					print 'Time: ' + str(row[0]) + ' ' + msgDirection + str(row[3])
			except:
				pass

def main():

	parser = optparse.OptionParser('Usage%prog' + '-p <skype profile path>')
	parser.add_option('-p', dest='path', type='string', help='specify the profile path')
	(options, args) = parser.parse_args()

	pathName = options.path

	if pathName == None:
		print parser.usage
		exit(0)
	
	elif os.path.isdir(pathName) == False:
		print '[!]The given path does not exist: ' + pathName
		exit(0)

	else:
		skypeDB = os.path.join(pathName, 'main.db')
		if os.path.isfile(skypeDB):
			printProfile(skypeDB)
			printContacts(skypeDB)
			printCallLog(skypeDB)
			printMessages(skypeDB)

		else:
			print '[!} No Skype database found matching: ' + skypeDB
if __name__ == '__main__':
	main()