from burp import IBurpExtender
from burp import IContextMenuFactory
from javax.swing import JMenuItem
from java.util import List, ArrayList 
from java.net import URL
import re
from datetime import datetime
from HTMLParser import HTMLParser

class TagStripper(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.page_text = []

	def handleData(self,data):
		self.page_text.append(data)

	def handelComment(self, data):
		self.handleData(data)

	def strip(self,html):
		self.feed(html)
		return "".join(self.page_text)


class BurpExtender(IBurpExtender,IContextMenuFactory):

	def registerExtenderCallbacks(self, callbacks):
		self._callbacks = callbacks
		self._helpers = callbacks.getHelpers()
		self.context = None
		self.hosts = set()
		self.wordlist = set(["password"])

		callbacks.setExtensionName("Wordlist Create")
		callbacks.registerContextMenuFactory(self)
		return

	def createMenuItems(self, context_menu):
		self.context = context_menu
		menu_list = ArraList()
		menu_list.add(JMenuItem("Create Worldlist", actionPerformed=self.wordlist_menu))
		return menu_list	

	def wordlist_menu(self,event):
		#grab details from user's clicks
		http_traffic = self.context.getSelectedMessages()

		for traffic in http_traffic:
			http_service = traffic.getHttpService()
			host = http_service.getHost()
			self.hosts.add(host)
			http_response = traffic.getHttpResponse()
			if http_response:
				self.get_words(http_response)
				self.display_wordlist()
			return
	def get_words(self, http_response):
		headers, body = http_response.tostring().split('\r\n\r\n',1)
		if headers.lower().find("content-type: text") == -1:
			return 

		tag_stripper = TagStripper()
		page_text = tag_stripper.strip(body)
		words = re.findall("[a-zA-z]\w{2,}", page_text)
		for word in words:
			if len(word) <= 12:
				self.wordlist.add(word.lower())
				return

	def mangle(self, word):
		year = datetime.now().year
		suffixes = ["","1","!",year]
		mangled = []
		for password in (word, word.capitalize()):
			for suffix in suffixes:
				mangled.append("%s%s" %(password, suffix))
		return mangled

	def display_word(self):
		print "#!comment: Worldlist for site(s) %s" %",".join(self.hosts)
		for word in sorted(self.wordlist):
			for password in self.mangled(word):
				print password
		return