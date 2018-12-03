import sys 
from scapy.all import *

interface = 'wlan0mon'
hiddenNets = []
decloaked = []

def Dot11Sniffer(pkt):
	if pkt.haslayer('Dot11ProbResp'):
		addr2 = pkt.getlayer(Dot11).addr2
		if (addr2 in hiddenNets)&(addr2 not in decloaked):
			netName = pkt.getlayer(Dot11ProbeResp).info
			print '[+] Hidden Network found'+ netName + 'for MAC:' + addr2
			decloaked.append(addr2)

		if pkt.haslayer(Dot11Beacon):
			if pkt.getlayer(Dot11Beacon).info == '':
				addr2 = pkt.getlayer(Dot11).addr2
				if addr2 not in hiddenNets:
					print '[+]Hidden Network Found with MAC: ' + addr2
					hiddenNets.append(addr2)
sniff(iface=interface, prn=Dot11Sniffer) 