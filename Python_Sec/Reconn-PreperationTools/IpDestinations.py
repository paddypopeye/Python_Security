import dpkt, socket, pygeoip, optparse

gi = pygeoip.GeoIP('/opt/GeoIP/GeoIP.dat')

def retGeoStr(ip):
	try:
		rec = gi.record_by_name(ip)
		city = rec['city']
		country = rec['country_code3']
		if city != '':
			geoLoc = city + '. ' + country
		else:
			geoLoc = country
				
		return geoLoc
		
	except Eception, e:
		return 'Unregistered'
		
def printPcap(pcap):
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)

			print '[+] Src: ' + src + '----> Dst: ' + dst

			print '[+] Src: ' + retGeoStr(src) + '----> Dst: ' + retGeoStr(dst)
		
		except: 
			pass

def main():
	parser  = optparse.OptionParser('Uasage%prog' + '-p <pcap file>')
	parser.add_option('-p', dest='pcapFile', type='string', help='specify the pcap file')

	(options, args) = parser.parse_args()
	
	if options.pcapFile == None: 
		print parser.usage
		exit(0)

	else:
		pcapFile= options.pcapFile
		fd = open(pcapFile, 'rb')
		pcap = dpkt.pcap.Reader(fd)
		printPcap(pcap)

if __name__ == '__main__':
	main()