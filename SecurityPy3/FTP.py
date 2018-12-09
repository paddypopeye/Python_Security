import ftplib

ftp = ftplib.FTP("user","pswd")

try:
	ftp.login("user","pswd")
	print(ftp.getwelcome())
	ftp.delete("somefile")
	print(ftp.dir())
	ftp.set_pasv(1)
	ftp.storbinary("storeFile", open("somefile","rb"))
	prnt(ftp.dir())
except Exception as e:
	print("Exception" , e)
finally:
	ftp.close()