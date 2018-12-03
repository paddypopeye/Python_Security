#!/usr/bin/python2.7

import socket 

target_host = "www.google.es"
target_port = 80
request = "GET / HTTP/1.1\r\nHost: google.es\r\n\r\n"

#Create socket obkect
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connect
client.connect((target_host,target_port))
#Send daata
client.send(request)
#Receive data
response = client.recv(4096)
print response