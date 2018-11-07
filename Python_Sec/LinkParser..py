from anonymousBrowser import *
from BeautifulSoup import BeautifulSoup
import os, optparse, re

def printLinks(url):
	incog = anonymousBrowser()
	incog.anonymize()
	page = incog.open(url)
	html = page.read()

	try:
		print '[+] Printing the links from Regex'
		link_finder =  re.compile('href="(.*?)"')
		links =  link_finder.findall(html)
		for link in links:
			print link
	except:
		pass
	try:
		print '\n [+] Printing Links from BeautifulSoup'
		soup = BeautifulSoup(html)
		links = soup.findAll(name='a')
		for link in links:
			if link.has_key('href'):
				print link['href']
	except:
		pass

def main():
	parser = optparse.OptionParser('usage % program -u <target url>')
	parser.add_option('-u', dest='tgtUrl', type='string', help='specify the target url')
	(options,args) = parser.parse_args()
	tgtUrl = options.tgtUrl
	if tgtUrl == None:
		print parser.usage
		exit(0)
	else:
		printLinks(tgtUrl)

if __name__ == '__main__':
	main()