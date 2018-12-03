import mechanize 
import cookielib
import random 

class anonymousBrowser(mechanize.Browser):
	def __init__ (self, proxies=[], user_agents=[]):
		mechanize.Browser.__init__(self)
		self.set_handle_robots(False)
		self.proxies = proxies
		self.user_agents = user_agents + [('User-agent', 'Mozilla/5.0 (X11; U;'+\
		'Linux 2.4.2-2 1586; en-US; m18) Gecko/20010132 Netscape6/6.01')]
		self.cookie_jar = cookielib.LWPCookieJar()
		self.set_cookiejar(self.cookie_jar)
		self.anonymize()

	def clear_cookies(self):
		self.cookie_jar = cookielib.LWPCookieJar()
		self.set_cookiejar(self.cookie_jar)

	def changeUserAgent(self, userAgent):
		index = random.randrange(0, len(self.user_agents))
		self.addheaders = [('User-agent', (self.user_agents[index]))]


	def changeProxy(self):
		if self.proxies:
			index = random.randrange(0, len(self.proxies))
			self.set_proxies({'http': self.proxies[index]})

	def anonymize(self, sleep=False):
		self.clear_cookies()
		self.changeProxy()
		if sleep:
			time.sleep(60)