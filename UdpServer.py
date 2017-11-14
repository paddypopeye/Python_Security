import socket 


BIND_IP = "0.0.0.0"
BIND_PORT = 9000


server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((BIND_IP,BIND_PORT))
print "Waiting on port" + str(BIND_PORT)

while True:
	data, addr = server.recvfrom(1024)
	print data
server.sento("ACK",(BIND_PORT))
