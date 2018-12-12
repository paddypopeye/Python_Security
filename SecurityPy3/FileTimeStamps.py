import os, datetime

rootdir = "/Users/username"
srchdate = datetime.date.today() - datetime.timedelta(days=2)

for current, dirs, files in os.walk(rootdir):
	for file in files:
        try:
            path = "%s/%s" % (current, file)
            time = datetime.date.fromtimestamp(os.path.getmtime(path))
            if (time > srchdate):
                print("Found date %s on file %s" % (time,file))
        except Exception as e:
        	print(e)
            no_op = 0