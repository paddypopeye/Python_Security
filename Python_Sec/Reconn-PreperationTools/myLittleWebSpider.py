import Queue
import threading
import os
import urllib2

threads = 10
target = "**********"
directory = "/var/www/html/Joomla-3-8-3"
filters = [".jpg",".css",".png",".gif"]

os.chdir(directory)
web_paths = Queue.Queue()

for r, f, d in os.walk():
	for files in f:
		remote_path = "%s/%s" %(r,files)
		if remote_path.startswith("."):
			remote_path = remote_path[1:]
			if os.path.splitext(files)[1] not in filters:
				web_paths.put(remote_path)

def test_remote():
	while not web_paths.empty():
		path = web_paths.get()
		url = "%s/%s" %(r,files)
		request = urllib2.Request(url)
		try:
			response = urllib2.open(request)
			content =  response.read()
			print "[%d] => %s" %(response.code, path)
			response.close()
		except urllib2.HTTPError as error:
			print "Failed %s" %error.code
			pass

		for i in range(threads):
			print "Spawning thread: %d" %i

			t = threading.Thread(target=test_remote)
			t.start()