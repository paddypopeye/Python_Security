#!/usr/bin/python3
import threading, socket

class clientConnect(threading.Thread):
	"""docstring for clientConnect"""
	def __init__(self):
		threading.Thread.__init__(self)


	def run(self):

		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			addr = ("www.google.com", 443)
			sock.connect(addr)
			print ("Connected...\n\r")

		except Exception as e:
			print("Error occurred")

def main():
	sockClients = []
	for i in range(1,1000):
		sock = clientConnect()
		sock.start()
		print("Started thread" , i)
		sockClients.append(sock)
		print(sockClients)

if __name__ == "__main__":
	main()