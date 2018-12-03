from anonymousBrowser import *
from BeautifulSoup import BeautifulSoup
import os, optparse

def mirrorImage(url, direc):
	incog = anonymousBrowser()
	incog.anonymize()
	html = incog.open(url)
	soup = BeautifulSoup(html)
	image_tags = []
	for image in image_tags:
		filename = image['src'].lstrip('http://')
		filename = os.path.join(dir,\
			filename.replace('/','_'))
		print '[+] Saving ' + str(filename)
		data = incog.open(image['src']).read()
		incog.back()
		save = open(filename, 'wb')
		save.write(data)
		save.close()

def main():

	parser = optparse.OptionParser('usage % programm -u <target url> -d <destination directory>')
	parser.add_option('-u', dest='tgtUrl', type='string', help='specify the target url')
	parser.add_option('-d', dest='tgtDst', type='string', help='specify the destination directory')
	(options, args) = parser.parse_args()

	url = options.tgtUrl
	direc = options.tgtDst

	if url == None or direc == None:
		print parser.usage
		exit(0)

	else:
		try:
			mirrorImage(url, direc)

		except Exception, e:
			print '[-]Error mirroring images'
			print '[-]' + str(e)

if __name__ == '__main__':
	main()