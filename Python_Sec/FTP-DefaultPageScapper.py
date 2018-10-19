#!/usr/bin/python
#-*-coding utf-8-*-
import ftplib

def returnDefault(ftp):
	try:
		dirList = ftp.nlst()

	except:
		dirList = []
		print '[-]Could not list directory contents'
		print '[-]Skipping to the next target'
		return

	retList = []
	for fileName in dirList:
		fd = fileName.lower()
		if '.php' in fd or '.htm' in fd or '.asp' in fd:
			print '[+]Found default page' + fileName
			retList.append(fileName)
		return retList


host = '192.168.56.102'
userName = 'root'
passWord = 'toor'
ftp = ftplib.FTP(host)
ftp.login(userName,passWord)
returnDefault(ftp)