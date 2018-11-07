from scapy.all import *
from bluetooth import *
import time

def retBtAddr(addr):
	bluethAddr = str(hex(int(addr.replace(':',''),16)+1))[2:]
	bluethAddr = bluethAddr[0:2] + ':' + bluethAddr[2:4] +\
	':'+ bluethAddr[4:6]+ ':' + bluethAddr[6:8]+ ':' + bluethAddr[8:10]\
	 + ':' + bluethAddr[10:12]

	return bluethAddr 

def checkBluetooth(bluethAddr):
	bluethName = lookup_names(bluethAddr)
	if bluethName:
		print '[+] Device Detected' + bluethName

	else:
		print '[-] No Devices Detected'

def wifiPrint(pkt):
	iPhone_OUI = 'd0:23:db'

	if pkt.haslayer(Dot11):
		wifiMAC = pkt.getlayer(Dot11).addr2
		if iPhone_OUI == wifiMAC[:8]:
			print '[*] iPhone MAC detected' + wifiMAC
			bluethAddr = retBtAddr(wifiMAC)
			print '[+] Testing the Bluetooth'

def wifiPrintPkt(pkt):
	iPhone_OUI = 'd0:23:db'
	if pkt.haslayer(Dot11):
		wifiMAC = pkt.getlayer(Dot11).addr2
		if iPhone_OUI == wifiMAC[:8]:
			print '[*] iPhone Mac detedted' + wifiMAC
			bluethAddr = retBtAddr(wifiMAC)
			print '[+] Testing the Bluetooth' + bluethAddr
			checkBluetooth(bluethAddr)

conf.iface  = 'wlan0mon'
sniff(prn=wifiPrint)