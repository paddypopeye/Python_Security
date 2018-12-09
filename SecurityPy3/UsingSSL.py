import ssl, socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sslSock = ssl.wrap_socket(sock)

try:
	sslSock.connect(("www.google.com", 443))
	print (sslSock.cipher())

except Exception as e:
	print ("Connection Error", e)


try:
	sslSock.write(b"GET / HTTP/1.1 \r\n")
	sslSock.write(b"Host: www.google.com \n\n")

except Exception as e:
	print ("Write Error", e)

data = bytearray()

try:
	data = sslSock.read()

except Exception as e:
	print ("Read Error", e)

print(data.decode("ISO-8859-1"))