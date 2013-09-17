#!/usr/bin/env python2.7
import urllib2
from sgmllib import SGMLParser
class URLLister(SGMLParser):
	urls = []
	def start_a(self, attrs):
		href = []
		is_tmp = False
		for k,v in attrs:
			if k=='class' and v=='z-movie-playlink':
				is_tmp = True
			if k=='href' and is_tmp:
				print(v)
		if href:
			self.urls.extend(href)
proxy_support = urllib2.ProxyHandler({'http':'127.0.0.1:8087'})
opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
content = urllib2.urlopen('http://dianying.fm').read()
outfile = open('out.txt','w')
for char in content:
	outfile.write(char)
lister = URLLister()
lister.feed(content)
#print lister.urls
