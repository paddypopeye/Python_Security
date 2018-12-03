import dpkt, socket, optparse

THRESH = 1000

def findDownLoad(pcap):
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			tcp = ip.data

			if http.method == 'GET':
				uri = http.uri.lower()
				if '.zip' in uri and 'loic' in uri:
					print '[!]' + src + ' Downloaded LOIC'
		except:
			pass

def findHivemind(pcap):
	for(ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			tcp = ip.data
			dport = tcp.dport
			sport = tcp.sport

			if dport == 6667:
				if '!laz"or' in tcp.data.lower():
					print '[!]DDoS Hivemind issued by: ' +sr 
					print '[+]Target CMD ' + tcp.data
				
				if sport == 6667:
					if '!lazor' in tcp.data.lower()
					print '[!]DDoS Hivemind issued to: ' +src
					print '[+] Target CDM: ' + tcp.data
		except:
			pass

def findAttack(pcap):
	pktCount = {}
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			tcp = ip.data
			dport = tcp.dport
			if dport == 80:
				stream = src + ':' + dst
				if pktCount.has_key(stream):
					pktCount[stream] = pktCount[stream]+1
				else:
					pktCount[stream]=1
		except:
			pass
		for stream in pktCount:
			pktsSent = pktCount[stream]
			if pktsSent > THRESH:
				src = stream.split(':')[0]
				dst = stream.split(':')[1]
				print '[+] ' + src + ' attacked ' + dst + ' with ' + str(pktsSent)+' packets'

def main():
	parser = optparse.OptionParser('Usage%prog' + '-p <pcap file>')
	parser.add_option('-p', dest='pcapFile', type='string', help='specify the pcap file')
	parser.add_option('-T', dest='thresh', type='string', help='specify the threshold')

	(options, args) = parser.parse_args()

	pcapFile = options.pcapFile
	thresh = options.thresh

	if pcapFile == None:
		print parser.usage 
		exit(0)

	if options.THRESH != None:
		THRESH = options.thresh

	fd = open(pcapFile)
	pcap =  dpkt.pcap.Reader(fd)
	findDownLoad(pcap)
	findHivemind(pcap)
	findAttack(pcap)

if __name__ == '__main__':
	main()