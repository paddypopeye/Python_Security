from scapy.all import *


def pktPrint(pkt):
	if pkt.haslayer(Dot11Beacon):
		print '[+] Detected 802.11 Beacon Frame'
	elif pkt.haslayer(Dot11ProbeReq):
		print '[+] Detected 802.11 Probe Requet Frame'
	elif pkt.haslayer(TCP):
		print '[+] Detected TCP Packet'
	elif pkt.haslayer(DNS):
		print '[+] Detected DNS Packet'

conf.iface = 'wlan0mon'
sniff(prn=pktPrint)
