from burp import IBurpExtender
from burp import IContextMenuFactory
from javax.swing import JMenuItem
from java.util import List, ArrayList
from java.net import URL
import socket, urllib, json, re, base64

bing_api_key = "<BING_API_KEY>"

class BurpExtender(IBurpExtender, IContextMenuFactory):
	
	def registerExtenderCallbacks(self, callbacks):
		self._callbacks = callbacks
		self._helpers = callbacks.getHelpers()
		self.context = None

		callbacks.setExtensionName("Bing Scraper")
		callbacks.registerContextMenuFactory(self)

		return

	def createMenuItems(self, context_menu):
		slef.context = context_menu
		menu_list = ArrayList()
		menu_list.add(JMenuItem("Send to Bing", actionPerformed=slef.bing_menu))

		return menu_list