from scapy.all import *

def dupRadio(pkt):
	rPkt = pkt.getlayer(RadioTap)
	version = rPkt.version
	pad = rPkt.pad
	present=rPkt.present
	notdecoded = rPkt.notdecoded

	newPkt = RadioTap(version=version,pad=pad,present=present,notdecoded=notdecoded)

	return newPkt

def dupDot11(pkt):
	destPkt = pkt.getlayer(Dot11)
	subtype = destPkt.subtype
	Type = destPkt.type
	proto = destPkt.proto
	FCfield = destPkt.FCfield
	ID =destPkt.ID
	addr1 = destPkt.addr1
	addr2 = destPkt.addr2
	addr3 = destPkt.addr3
	SC = destPkt.sc
	addr4 = destPkt.addr4

	newPkt=Dot11(subtype=subtype,\
				type=Type,\
				proto=proto,\
				FCfield=FCfield,\
				ID=ID,\
				addr1=addr1,\
				addr2=addr2,\
				addr3=addr3,\
				SC=sc,\
				addr4=addr4
				)
	return newPkt

def dupSNAP(pkt):
	srcPkt = pkt.getlayer(SNAP)
	oui = srcPkt.oui
	code = srcPkt.code
	newPkt =  SNAP(OUI=oui, code=code)
	return newPkt

def dupLLC(pkt):
	 llcPkt = pkt.getlayer(LLC)
	 dsap =  llcPkt.dsap
	 ssap = llcPkt.ssap
	 ctrl =  llcPkt.ctrl
	 newPkt = LLC(dsap=dsap,ssap=ssap,ctrl=ctrl)
	 return newPkt

def dupIP(pkt):
	IPpkt = pkt.getlayer(IP)
	version = IPpkt.version
	tos = IPpkt.tos
	ID = IPpkt.ID
	flags = IPpkt.flags
	ttl = IPpkt.ttl
	flags = IPpkt.flags
	proto = IPpkt.proto
	src = IPpkt.src
	dst = IPpkt.dst
	options = IPpkt.options

	newPkt = IP(version=version,\
		tos=tos,\
		ID=ID,\
		flags=flags,\
		ttl=ttl,\
		proto=proto,\
		options=options)
	return newPkt

def dupUDP(pkt):
	udpPkt = pkt.getlayer(UDP)
	sport = udpPkt.sport
	dport = udpPkt.dport
	newPkt = UDP(sport=sport,dport=dport)
	return newPkt