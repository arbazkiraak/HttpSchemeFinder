import urllib2
import ssl,sys

valid_domains = []

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

if sys.argv[1]:
	fileofdomains = sys.argv[1] 
else:
	sys.exit(1)

with open(fileofdomains,'r') as f:
	for i in f.readlines():
		i = i.strip('\n')
		i = i.strip('\r')
		try:
			content = urllib2.urlopen('http://'+str(i),context=ctx,timeout = 1.5)
			URL1 = content.url
			Status1 = str(content.getcode())
			if Status1 == '200':
				if URL1.endswith('/'):
					valid_domains.append(URL1)
					print(URL1)
				else:
					URL1 = URL1+'/'
					valid_domains.append(URL1)
					print(URL1)
		except urllib2.URLError as e:
			pass
			# if str(e) == '<urlopen error timed out>':
			# 	print('connection refused maybe/Timeout')
			# elif str(e) == '<urlopen error [Errno -2] Name or service not known>':
			# 	print('doesnt exist or protocal mismatch/NameServiceNotKnown')
		try:
			content1 = urllib2.urlopen('https://'+str(i),context=ctx,timeout = 1.5)
			URL2 = content1.url
			Status2 = str(content1.getcode())
			if Status2 == '200':
				if URL2.endswith('/'):
					valid_domains.append(URL2)
					print(URL2)
				else:
					URL2 = URL2+'/'
					valid_domains.append(URL2)
					print(URL2)
		except Exception as ee:
			#print(ee)
			pass
			
domains_iter = (set(valid_domains))
with open('output.txt','w') as l:
	for i in domains_iter:
		l.write(str(i)+'\n')
l.close()
