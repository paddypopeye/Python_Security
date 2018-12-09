import urllib, urllib2
from HTMLParser import HTMLParser

class myParser(HTMLParser):
	def handle_starttag(self,tag,attrs):
		if (tag == "input"):
			print("Input field found", tag)
			print(attrs)


class mySpider(HTMLParser):
	def handle_starttag(self,tag,attrs):
		if (tag == 'a'):
			for a in attrs:
				if a[0] == "href":
					link = a[1]
					if (link.find("http") >= 0):
						print link
						newParse = mySpider()
						newParse.feed(link)


url = "http://www.infiniteskills.com"
data = {"name": "testname", "age": "35", "btnSubmit": "Submit"}
params = urllib.urlencode(data)
request = urllib2.Request(url, params)
response = urllib2.urlopen(request)
page = response.read()
print(page)
parser = myParser()
parser.feed(response.read())

#Proxy
proxyHandler = urllib2.ProxyHandler({"http":"127.0.0.1:8080"})
opener = urllib2.build_opener(proxyHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen("https://www.infiniteskills.com")

print(response.read())