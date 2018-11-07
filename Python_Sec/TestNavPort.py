from scapy.all import *
NAVPORT = 5556

def printPkt(pkt):
	if (pkt.haslayer(UDP)):
		raw = pkt.sprintf('%Raw.load%')
		print raw

conf.iface = 'wlan0mon'
sniff(prn=printPkt)