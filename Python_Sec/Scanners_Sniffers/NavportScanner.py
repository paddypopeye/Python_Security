import sys
from scapy.all import *
interface = 'wlan0mon'
hidddenNets = []
decloaked = []

def sniffDot11(pkt):
	if pkt.haslayer(Dot11ProbResp):
		addr2 == pkt.getlayer(Dot11).addr2
		if (addr2 in  hidddenNets) & (addr2 not in decloaked):
			netName = pkt.getlayer('Dot11ProbResp').info
			print '[+]Found hidden SSID: ' + netName +'with MAC: ' + addr2
			decloaked.append(addr2)

	if pkt.haslayer(Dot11Beacon):
		if pkt.getlayer(Dot11Beacon).info == '':
			addr2 = pkt.getlayer(Dot11).addr2
			if addr2 not in decloaked:
				print '[-] Found SSID: with MAC: ' + addr2
				hidddenNets.append(addr2)

sniff(iface=interface, prn=sniffDot11)


