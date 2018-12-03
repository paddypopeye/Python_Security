import optparse, time 
from scapy import *
from IPy import IP as IPTEST

ttlValues = {}
THRESH = 5

def checkTTL(ipsrc, ttl):
	if IPTEST(ipsrc).iptype() == 'PRIVATE':
		return

	if not ttlValues.has_key(ipsrc):
		pkt = sr1(IP(dst=ipsrc)/ICMP(),retry=0, timeout=1, verbose=0)
		ttlValues[ipsrc] = pkt.ttl
		if abs(int(ttl) - int(ttlValues[ipsrc])) > THRESH:
			print '[!]Detected possible spoof packet from ' + ipsrc
			print '[!] TTL: ' +ttl+ ' Actual TTL: ' + str(ttlValues[ipsrc])

def testTTL(pkt):
	try:
		if pkt.haslayer(IP):
			ipsrc  = pkt.getlayer(IP).src
			ttl = str(pkt.ttl)
			checkTTL(ipsrc.ttl)
	except:
		pass

def main():
	parser = optparse.OptionParser('Usage%prog' + '-i <interface> -t <threshold>')
	parser.add_option('-i', dest='iface', type='string', help='specify the interface')
	parser.add_option('-t', dest='thresh', type='string', help='specify the threshhold')
	(options, args) = parser.parse_args()
	
	if options.iface == None:
		print parser.usage
	else:
		conf.iface = options.iface

	if options.thresh != None:
		THRESHs = options.thresh
	else:
		THRESH = 5
	sniff(prn=testTTL, store=0)

if __name__ == 'main':
	 main()