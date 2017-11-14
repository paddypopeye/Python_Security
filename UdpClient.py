import socket

DATA = "AAABBBCCC"
TARGET = "127.0.0.1"
PORT = 9000

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(DATA,(TARGET,PORT))
data, addr = client.recvfrom(4096)
print data, addr 
