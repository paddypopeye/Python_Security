from pyfuzz.generator import *
import socket, random

msg = b"GET " + random_ascii() + b"HTTP /1.1\n Host: 127.0.0.1\r\n"
try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	addr = ("127.0.0.1", 8080)
	sock.connect(addr)
	sock.sendall(msg)
	response = sock.recv(4096)
	print(response)
except Exception as e:

	print("Error", e)

finally:
	sock.close()