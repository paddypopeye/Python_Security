import httplib

host = "www.infiniteskills.com"

request = httplib.HTTP(host)

request.putrequest("HEAD", "/")
request.putheader("Host", host)
request.endheaders()
request.send("")
statusCode, statusMsg, headers = request.getreply()
print("Status Code", statusCode)
print(headers)
