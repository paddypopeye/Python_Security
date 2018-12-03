import dpkt, optparse, pygeoip, socket

gi = pygeoip.GeoIP('/opt/GeoIP/GeoIP.dat')

def retKLM(ip):
	rec = gi.record_by_name(ip)
	try:
		longitude = rec['longitude']
		latitude = rec['latitude']
		klm = (
			'<Placemaker>\n'
			'<name>%s</name>\n'
			'<Point>\n'
			'<coordiantes>%6f,%6f</coordiantes>\n'
			'</Point>\n'
			'</Placemaker>\n') %(ip, longitude, latitude)
		return klm
	except: 
		return ''

def plotIPs(pcap):
	kmlPts = ''
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			srcKML = retKLM(src)
			dst = socket.inet_ntoa(ip.dst)
			dstKML = retKLM(dst)
			kmlPts = kmlPts + srcKML + dstKML
		except:
			pass

	return kmlPts

def main():
	parser = optparse.OptionParser('Usage%prog' + '-p <pcap file>')
	parser.add_option('-p', dest='pcapFile', type='string', help='specify the pcap file')
	(options, args) = parser.parse_args()
	pcapFile = options.pcapFile

	if pcapFile == None:
		print parser.usage
		exit(0)

	fd = open(pcapFile)
	pcap = dpkt.pcap.Reader(fd)

	kmlheader  = '<?xml version="1.0" encoding="UTF-8" ?>\
	<kml xmlns="https:www.opengis.net/kml/2.2">\n<Document>\n'

	kmlfooter = '<Document>\n </kml>\n'
	kmldoc = kmlheader+plotIPs(pcap)+kmlfooter

	print kmldoc

if __name__ == '__main__':
	main()