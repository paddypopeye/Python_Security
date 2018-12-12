import _winreg
from scapy.all import *
from scapy.utils import rdpcap

src_mac = "MAC_ADDR"
dst_mc = "MAC_ADDR"
dst_ip = "<SOME_IP>"
src_ip = "<SOME_IP>"

frames = rdpcap("somepcapfile.pcap")
for frame in fames:
	try:
		frame[Ether].src = src_mac
		frame[Ether].dst = dst_ip
		if IP in frame:
			frame[IP].src =src_ip
			frame[IP].dst = dst_ip
		sendp(frame)
	except Exception as e:
		print("Error", e)

keyName =   _winreg.CreateKey(_winreg.HKEY_CURRENT_USER)