from anonymousBrowser import *

ab = anonymousBrowser(
		proxies = [],\
		user_agents = [('User-agent', 'Anonymous Browser')]

	)

for attempt in range(1, 5):

	ab.anonymize()
	print 'Fetching the Page'
	response = ab.open('http://kittenwar.com')
	for cookie in ab.cookie_jar:
		print cookie
