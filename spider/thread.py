#!/usr/bin/env python2

import threading
import spider
import time
import data
import sys
import random
import urllib2
lock = threading.Lock()
proxy_support = urllib2.ProxyHandler({'http':'127.0.0.1:8003'})
opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
proxy_enable = 0
def change_proxy():
	global proxy_enable
	if proxy_enable:
		reload(urllib2)
		proxy_enable = 0
		print 'now use DIRECT'
	else:
		urllib2.install_opener(opener)
		proxy_enable = 1
		print 'now use PROXY'
class myThread(threading.Thread):
	def __init__(self, num, thedata):
		threading.Thread.__init__(self)
		self.num = num
		self.data = thedata
		self.is_running = True
		self.level = 0
	def run(self):
		worker = spider.Spider(self.num, self.data)
		while(self.is_running):
			while not lock.acquire(): pass
			flag = worker.get_url()
			lock.release()
			if not flag:
				continue
			flag = worker.get_content()
			if flag == 403:
				self.level += 1
				delay = 0.1*(2**self.level)
				if delay>10:
					change_proxy()
				if delay>300:
					delay = 300
				print delay
				time.sleep(delay)
				continue
			elif flag == 404:
				continue
			elif flag == 100:
				continue
			elif flag == 503:
				change_proxy()
				continue
			self.level = 0
			while not lock.acquire(): pass
			worker.put_url()
			lock.release()
			#time.sleep(3*random.random())
	def stop(self):
		self.is_running = False
thedata = data.Data()
if len(sys.argv)>1 and sys.argv[1] == '--init':
	print '-----------init-----------'
	thedata.getfromdb()
	thedata.fillurl()
	thedata.show()
else:
	thedata.load()
spiders = []
for i in range(20):
	tmp = myThread(i, thedata)
	tmp.setDaemon(True)
	tmp.start()
	spiders.append(tmp)
while(True):
	try:
		time.sleep(300)
		reload(urllib2)
		proxy_enable = 0
		print 'proxy time up,',
		print 'now use DIRECT'
	except KeyboardInterrupt:
		print 'my keyboard'
		thedata.dump()
		print 'dumped'
		try:
			option = raw_input('what\'s going on? (exit, )\n>>')
		except KeyboardInterrupt:
			option = ''
		if option == 'exit':
			for i in spiders:
				i.stop()
			thedata.dump()
			print 'dumped'
			for i in spiders:
				print i.isAlive()
				while(i.isAlive()):
					time.sleep(0.2)
			thedata.dump()
			print 'dumped'
			exit()
		elif option == 'show':
			print '-'*100
		elif option == 'change':
			change_proxy()
		elif option == 'proxy':
			print proxy_enable
