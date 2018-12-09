import smtplib, poplib, imaplib
from email.mime.text import MIMEText

# ehlo example.com
# mail from: someadd@someadd.com
# rcpt to: another@another.com
# data 

mailObj = smtplib.SMTP("127.0.0.1", 25)
mailObj.login("user", "pswd")
try:
	#If using a MIME message

		# fd = open("file", "r")
		# md = MIMEText(fd.read())
		# fd.close()
		# md['To'] = """"""
		# md['From'] = """"""
		# md['Subject'] = """"""
	msg = "\nThis is a vert short message"
	mailObj.sendmail("to", "from", msg)
	print("Sending Finished")

except Exception as e:
	print("Mail was not sent Error")
mailObj.quit()

#POP3
#pop = poplib.POP3("127.0.0.1", 110)	
pop = poplib.POP3_SSL("127.0.0.1", 995)
print(pop.getwelcome())
pop.user("user")
pop.pass_("password")
print(pop.list())

#IMAP
imp = imaplib.IMAP4("127.0.0.1", 143)
imp.login(getpass.getuser(), getpass.getpass_())
imp.login("user","pswd")
imp.select()
code, lst = imp.list()
print("Response Code: ", code)
print(lst)
code, ids = imp.search(None, "ALL")
print(ids)
code, msg = imp.fetch('1', "(UID BODY[TEXT])")
imp.store()
print(msg)
imp.close()
imp.logout()