import pcapy, socket
from struct import *

pcap_file = pcapy.open_offline("file.pcap")
count = 1

while  count:
	print ("Packet #:", count)
	count += 1
	(header, payload) = pcap_file.next()
	l2hdr = payload[:14]
	l2data = unpack("!6s6sH", l2hdr)
	srcMac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" %(ord(l2hdr[0]), ord(l2hdr[1]), ord(l2hdr[2]),ord(l2hdr[3]),ord(l2hdr[4]),ord(l2hdr[5]))
	dstMac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" %(ord(l2hdr[6]), ord(l2hdr[7]), ord(l2hdr[8]),ord(l2hdr[9]),ord(l2hdr[10]),ord(l2hdr[11]))
	print ("Source MAC: ", srcMac, "Destination MAC:", dstMac )

	##Ip header 20bytes
	ipHeader = unpack("!BBHHHBBH4s4s". payload[13:34])
	ttl = ipHeader[5]
	protocol = ipHeader[6]
	print "Protocol", str(protocol), "The TTL: ", str(ttl)

#Multicasting
mgrp = "224.1.1.1"
mport = 5775

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.REUSEADDR, 1)
for i in range(1,10):
	sock.sendto(b"some msg",(mgrp,mport))

print("Message sent to Group")