import optparse
from scapy.all  import *

def ftpSniffer(pkt):
	dest = pkt.getlayer(IP).dst
	raw = pkt.sprintf('%Raw.load%')
	user = re.findall('(?i)USER (.*)', raw)
	pswd = re.findall('(?i)PASS (.*)', raw)

	if user:
		print '[*] FTP login for ' + str(dst)
		print '[+] User details ' +str(user[0])

	elif pswd:
		print '[+]Detected Password ' + ste(pswd[0])


def main():
	parser = optparse.OptionParser('usage % program  -i <interface>')
	parser.add_option('-i', dest='interface', type='string', help='specify the interface')
	(options, args) = parser.parse_args()

	if options.interface == None:
		print parser.usage
		exit(0)
	else:
		conf.iface = options.interface
	try:
		sniff(filter='tcp', prn=ftpSniffer)

	except KeyboardInterrupt:
		exit(0)


if __name__ == '__main__':
	main()

