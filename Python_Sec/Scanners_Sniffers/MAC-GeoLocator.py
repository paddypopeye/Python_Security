import mechanize, urllib, re, optparse, urlparse, sys
def val2addr(val):
	addr = ''
	for ch in val:
		addr += '%20x' %ord(ch)
	addr = addr.strip(' ').replace('',':')[0:17]
	return addr

def wiglePrint(username, password, netid):
	browser = mechanize.Browser()
	browser.open('https://wigle.net')
	reqData = urllib.urlencode({
		'credential_0': username,
		'credential_1': password
		})

	browser.open('https://wigle.net/gps/gps/main/confirmquery', reqData)
	params = {}
	params['netid'] = netid
	reqParams = urllib.urlencode(params)
	respURL = 'https://wigle.net/gps/gps/main/confirmquery'
	resp = browser.open(respURL, reqParams).read()
	mapLat = 'N/A'
	mapLon = 'N/A'
	rLat = re.findall(r'maplat=.*\&', resp)
	if rLat:
		mapLat = rLat[0].split('&')[0].split('=')[1]
	
	rLon = re.findall(r'maplon=.*\&', resp)
	
	if rLon:
		mapLon = rLon[0].split()

	print '[-] Lat: ' + mapLat + ' Lon:' + mapLon

def printNets():

	net = "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Networklist\\Signatures\\Unmanaged"
	key = OpenKey(HKEY_LOCAL_MACHINE, net)

	print '\n[*]Networks found..'

	for i in range(100):
		try:
			guid = EnumKey(key, i)
			netKey = OpenKey(key, str(guid))

			(n, addr, t) = EnumValue(netKey, 5)
			(n, name, t) = EnumValue(netKey, 4)
			macAddr = val2addr(addr)
			netName = str(name)
			print '[+]' + netName + ' ' + macAddr
			CloseKey(netKey)
		except:
			break

def main():
	parser = optparse.OptionParser('Usage%prog: ' + "-u <wigle username> -p <wigle password>")
	parser.add_option('-u', dest='username',type='string', help='specify the username')
	parser.add_option('-p', dest='password', type='string', help='specify the password')
	(options, args) = parser.parse_args()
	username = options.username
	password = options.password
	if username == None or password == None:
		print parser.usage
		sys.exit(0)

if __name__ == '__main__':
	main()


	

