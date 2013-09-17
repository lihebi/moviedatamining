#!/usr/bin/env python2.7
from sgmllib import SGMLParser
class URLLister(SGMLParser):
	#self.urls = []
	urls = []
	def start_a(self,attrs):
		href = [v for k,v in attrs if k=='href']
		if href:
			self.urls.extend(href)
data = """<a href="shglsfj"</a>"""
lister = URLLister()
lister.feed(data)
print lister.urls
