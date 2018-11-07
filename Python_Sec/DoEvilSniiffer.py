import optparse
from scapy.all import *

def doEvil(pkt):
	if pkt.haslayer(Raw):
		payload = pkt.getlayer(Raw).load
		if 'GET' in payload:
			if 'google' in payload:
				reg = re.findall(r'(?!)\&q=(.*?)\&', payload)
				if reg:
					search = reg[0].split('&')[0]
					search = search.replace('q=', '')\
					.replace('+', ' ').replace('%20', ' ')
					print '[+] Searched for' + search

def main():
	parser = optparse.OptionParser('usage % program -i <interface>')
	parser.add_option('-i', dest='interface', type='string', help='specify the interface')
	(options, args) = parser.parse_args()

	if options.interface == None:
		print parser.usage
		exit(0)
	else:
		conf.iface = options.interface
	try:
		print '[*] DoEvil sniffer running'
		sniff(filter='tcp port 80', prn=doEvil)
	except KeyboardInterrupt:
		exit(0)

if __name__ == '__main__':
	main()