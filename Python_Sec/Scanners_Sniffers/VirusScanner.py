import httplib, os, optparse, re, time
from urlparse import urlparse

def printResults(url):
	status = 200
	host = urlparse(url)[1]
	path = urlparse(url)[2]

	if 'analysis' not in path:
		while status != 302:
			conn = httplib.HTTPConnection(host)
			conn.request('GET', path)
			resp = conn.getresponse()
			print resp.read()
			print resp.status, resp.reason

			status = resp.status
			print status
			print '[+]Scanning the file now..'
			conn.close()
			time.sleep(15)

	print '[+] Scan completed...'
	path = path.replace('file', 'analysis')
	conn = httplib.HTTPConnection(host)
	conn.request('GET', path)
	resp = conn.getresponse()
	data = resp.read()
	print data
	conn.close()

	# regexResults = re.findall(r'Detection rate:.*\) ',data)
	# htmlStripResult = regexResults[1].replace\
	# ('&lt;font color=\'red\'&gt;','')\
	# .replace('&lt;/font&gt;','')
	# print '[+]' + str(htmlStripResult)

def uploadFile(filename):
	print '[+]Uploading file %s' %(str(filename)) + ' to NoVirusThanks'

	fileContents = open(filename, 'rb').read()
	header = {'Content-Type': 'multipart/form-data; boundary=----WebkitFormBoundaryF17rwCZdGuPNPT9U'}

	params = "------WebkitFormBoundaryF17rwCZdGuPNPT9U"
	params += "\r\nContent-Disposition: form-data; name=\"upfile\"; filename=\""+str(filename)+"\""
	params += "\r\nContent-Type: application/octet stream\r\n\r\n"
	params += fileContents
	params += "\r\n------WebkitFormBoundaryF17rwCZdGuPNPT9U"
	params += "\r\nContent-Disposition: form-data name=\"submitfile\"\r\n"
	params += "\r\nSubmit File\r\n"
	params += "------WebkitFormBoundaryF17rwCZdGuPNPT9U\r\n"

	conn = httplib.HTTPConnection('www.virustotal.com')
	conn.request('POST', "/", params, header)
	response = conn.getresponse()
	location = response.getheader('location')
	conn.close()
	return location

def main():
	parser = optparse.OptionParser('usage % program -f <filename>')
	parser.add_option('-f', dest='fileName', type='string', help='specify the file to scan')
	(options, args) = parser.parse_args()
	fileName = options.fileName

	if fileName == None:
		print parser.usage
		exit(0)
	elif os.path.isfile(fileName) == False:
		print '[-]File does not exist'
		exit(0)

	else:
		uploaded = uploadFile(fileName)
		printResults(uploaded)

if __name__ == '__main__':
	main()



