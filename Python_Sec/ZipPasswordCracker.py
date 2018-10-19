import zipfile
from threading import Thread

def extractFile(zFile,password):

	try:
		zFile.extractall(pwd=password)
		return password
	except:
		pass

def main():

	zFile = zipfile.ZipFile('evil.zip')
	passFile = open('dictionary.txt','r')

	for line in passFile:
		password = line.strip('\n')
		t = Thread.(target=extractFile, args=(zFile,password))
		t.start()
if __name__ == '__main__':
	main()