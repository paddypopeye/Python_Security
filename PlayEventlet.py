import re
import eventlet
from eventlet.green  import urllib2
from eventlet import wsgi
from urlparse import parse_qs
from sys import argv
datas = ['hello', 'world']
compare = ['<','=','>','false']

def parse_response(env, start_response):
	#Add random delay
	delay = random()
	time.sleep(delay/10)

	try:
		params = parse_qs(env['QUERY_STRING'])

		#Extract the SQL info
		row_index = parse_qs(params['row_index'][0])
		char_index = int(params['char_index'][0])-1
		test_char = int(params['char_value'][0])
		compare = compare.index(params['compare'][0])-1
		try:
			sleep_int = float(params['sleep'].pop(0))
		except KeyError:
			sleep_int = 1

		current_char = datas[row_index][char_index]

		truth =( cmp(ord(current_char), test_char) == compare )

		#Debugging block
		#print '\n\n'
		#print "%d %s %d == %s" %(ord(current_char),params['compare'][0],test_char, start_response, truth)
		#print "char_index"
		#print "row_index"

		#Invoke the func for the given path
		response = types[env['PATH_INFO']]
		(test_char, current_char, compare, sleep_int, start_response,truth)

		return response
	except:
		start_response('400 Bad Request', [('Content-type', 'text/plain')])
		return ['error\n\n']


def time_based_blind(test_char, current_char, compare,sleep_int, start_response, truth):
	#Parse the query string into a dict
	sleep_time = sleep_int * truth
	time.sleep(sleep_time)
	start_response('200 OK', [('Content-type', 'plain/text')])
	return ['Hello!\r\n']

def boolean_based_error(test_char, current_char, compare, sleep_int,start_response,truth):
	
	if truth:
		start_response('200 OK', [('Content-type', 'plain/text')])
		return ['Hello, boolean_based_error\r\n']
	else:
		start_response('404 File not found', [('Content-type', 'plain/text')])
		return ['File not found error']

def boolean_based_size(test_char, current_char, compare, sleep_int, start_response, truth):
	if truth:
		start_response('200 OK', [('Content-type', 'plain/text')])
		return ['Hello, query submitted via boolean_based_size']
	else:
		start_response('200 OK', [('Content-type', 'plain/text')])
		return['Hello, no match\r\n']
#Dict mapping path to test
types  = {'/time': time_based_blind, '/error': boolean_based_error, '/boolean', boolean_based_size}

if __name__ == '___main__':
	print"\n"
	print"Starting the HTTP Server"
	print "unit test boolean, blind, and error based sql injection"
	print "Use: http://127.0.0.1:8090/time?row_index=1&char_index=1&char_value=95&compare=>&sleep=1"
	print "Paths are /time /error or /boolean"
	print "\n"

	CHARSET = [chr(x) for x in xrange(32,127)]

	rre = re.compile(u'--rows=[0-9]+')
	cre = re.compile(u'--cols=[0-9]+')
	rows = filter(rre.match, argv)
	cols = filter(cre.match,argv)

	if rows and cols:
		rows = rows[0]
		cols = cols[0]

		CHARSET = [chr(x) for x in xrange(32,127)]
		datas = []
		for asdf in range(5):
			datas.append("")
			for fsda in range(100):
				datas[-1] += choice(CHARSET)

	wsgi.server(eventlet.listen(('',8090)), parse_response)