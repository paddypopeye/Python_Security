import urllib2, optparse 
from bs4 import BeautifulSoup
from urlparse import urlsplit
from os.path import basename
from PIL import Image
from PIL.ExifTags import TAGS

def findImages(url):
	print '[*] Searching for images on' + url

	urlContent = urllib2.urlopen(url).read()
	soup = BeautifulSoup(urlContent, features="html5lib")
	imgTags = soup.findAll('img')

	return imgTags

def downloadImages(imgTags):

	try:
		print '[+]Trying to download images...'
		imgSrc = imgTags['src']
		imgContent = urllib2.urlopen(imgSrc).read()
		imgFileName = basename(urlsplit(imgSrc)[2])
		imgfile = open(imgFileName, 'wb')
		imgFile.write(imgContent)
		imgFile.close()
		
		return imgFile
	except: 
		return ""

def testForExif(imgFileName):
	try:
		exifData = []
		imgFile = Image.open(imgFileName)
		info = imgFile._getexif()

		if info:
			for (tag,value) in info.items():
				decoded = TAGS.get(tag, tag)
				exifData[decoded] = value

			exifGPS = exifData['GPSinfo']
			if exifGPS:
				print '[*] ' + imgFileName + 'contains GPS information'
	except:
		pass

def main():
	parser = optparse.OptionParser('Usage%prog' + '-u <target url>')
	parser.add_option('-u', dest='url', type='string', help='specify the URL')
	(options, args) = parser.parse_args()

	targetUrl =  options.url

	if targetUrl == None:
		print parser.usage
		exit(0)

	else:
		imgTags = findImages(targetUrl)
		for imgTag in imgTags:
			imgFileName = downloadImages(imgTag)
			testForExif(imgFileName)

if __name__ == '__main__':
	main()