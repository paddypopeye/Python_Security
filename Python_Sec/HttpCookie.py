#!/usr/bin/env python
import webapp2
import random
from paste import httpserver
import sys

def GetAllHeaders(headers):
    header_response = 'HTTP Headers Received:\n'
    for k, v in headers.items():
        header_response += "%s : %s" %(k, v)
    return header_response

class RootCookie(webapp2.RequestHandler):
    def get(self):
        self.response.content_type= 'text/plain'
        header_response = GetAllHeaders(self.request.headers)
    
        self.response.set_cookie(
            'root_session_id',
            str(random.getrandbits(128)),
            max_age = 1200,
            path = '/')
        
        self.response.set_cookie(
            'blog_session_id',
            str(random.getrandbits(128)),
            max_age = 1800,
            path = '/blog')
        
        self.response.write(header_response)

class BlogCookie(webapp2.RequestHandler):

    def get(self):
        self.response.content_type = 'text/plain'
        header_response = GetAllHeaders(self.request.heaedrs)
        self.response.write(header_response)

class ForumCookie(webapp2.RequestHandler):

    def get(self):
        self.response.content_type = 'text/plain'
        header_response = GetAllHeaders(self.request.headers)
        self.response.write(header_response)

class BloggingCoookie(webapp2.RequestHandler):
    def get(self);
    self.response.content_type = 'text/plain'
    header_response = GetAllHeaders(self.request.headers)
    self.response.write(header_response)

app = webapp2.WSGIApplication([
    ('/', RootCookie),
    ('/blog', BlogCookie),
    ('/blogging', BloggingCoookie),
    ('/forum', ForumCookie)
])

try:
    def startServer():
        httpserver.serve(app, host="0.0.0.0", port= '8080')

except KeyboardInterrupt:
    sys.exit(0)

if __name__ == '__main__':
    startServer()