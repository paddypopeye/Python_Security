import nmap
import optparse
import threading

def nmapScan(tgtHost, tgtPort):
	nmScan = nmap.PortScanner()
	nmScan.scan(tgtHost, tgtPort)

	state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
	print "[*] " +tgtHost+ "tcp/"+tgtPort+" "+state

def main():
	parser = optparse.OptionParser('usage%prog' + '-H <target host> -p <target port>')

	parser.add_option('-H', dest='tgtHost', type='string', help='specify a target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify a target port(s), seperated by a comma')

	(options, args) = parser.parse_args()
	tgtHost  = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')


	if ((tgtHost == None) | (tgtPorts[0] == None)):
		print parser.usage
		exit(0)

	for tgtPort in tgtPorts:
		t = threading.Thread(target=nmapScan, args=(tgtHost,tgtPort))
		t.start()
		#nmapScan(tgtHost, tgtPort)

if __name__ == '__main__':
	main()