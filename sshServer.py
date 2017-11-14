import socket
import paramiko
import threading
import sys

host_key = paramiko.RSAKey(filename='/xxx/xxx')

class Server(paramiko.ServerInterface):

	def __init__(self):
		self.event = threading.Event()
			def check_chan_request(self, kind, chanid):
		if kind == 'session':
			return paramiko.OPEN_SUCCEEDED
		return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

	def check_auth_password(self, user, password):
		if user == 'user' and password == 'password':
			return paramiko.AUTH_SUCCESSFUL
		return paramiko.AUTH_FAILED

server = sys.argv[1]
ssh_port = int(sys.argv[2])

try: 
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	socket.bind(server, ssh_port)
	socket.listen(100)
	print "[+] Listening for connection ..."
	client, addr = socket.accept()
except Exception, e:
	print "[+] Failed to listen on %s:%d \n" %(server,ssh_port) + str(e)
	sys.exit(1)
print "[+] Connection Successful"

try:
	ssh_session = paramiko.Transport(client)
	ssh_session.add_server_key(host_key)
	server = Server()
	try:
		ssh_session.start_server(server=server)
	except paramiko.SSHException, x:
		print "SSH Negotiation Failed"
	chan = ssh_session.accept(20)
	print "Authetication Successful"
	print chan.recv(1024)
	chan.send('Welcome to sshServer')


	while True:
		try:
			command = raw_input("Please Enter a Command")
			if command != 'exit':
				chan.send(command)
				print chan.recv(1024)
			else:
				chan.send('exit')
				print "Exiting..."
				ssh_session.close()
				raise Exception('exit')
		except KetBoardInterrupt:
			ssh_session.close()

except Exception, e:
	print "Caught Exception:" + str(e)
	try:
		ssh_session.close()
	except:
		pass
	sys.exit(1)
