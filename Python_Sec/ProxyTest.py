import mechanize 
import cookielib

def testProxy(url, proxy):
	browser = mechanize.Browser()
	browser.set_proxies(proxy)
	page = browser.open(url)
	source_code = page.read()
	print source_code


def testUserAgent(url, userAgent):
	browser = mechanize.Browser()
 	browser.addheaders = userAgent
	page = browser.open(url)
	source_code = page.read()

	print source_code

def printCookies(url):
	browser = mechanize.Browser()
	cookie_jar = cookielib.LWPCookieJar()
	browser.set_cookiejar(cookie_jar)
	page = browser.open(url)
	for cookie in cookie_jar:
		print cookie
url = 'https://youtube.com/'
printCookies(url)
userAgent = [('User-agent', 'Mozilla/5.0 (X11; U;'+\
	'Linux 2.4.2-2 1586; en-US; m18) Gecko/20010132 Netscape6/6.01')]
#testUserAgent(url, userAgent)