#!/usr/bin/env python2
import time
from Queue import Queue
import urllib2
import re,os
from termcolor import colored

class Spider():
	def __init__(self, num, data):
		self.num = num
		self.data = data
		self.subject = []
		self.cele = ''
	def get_url(self):
		if self.data.url:
			self.url = self.data.url.pop()
			return True
		else:
			return False
	def _is_exist(self):
		filename = self._getfilename()
		return os.path.exists(filename)
	def _getcontentfromfile(self):
		filename = self._getfilename()
		return open(filename).read()
	def get_content(self):
		if self._is_exist():
			print colored('exist','cyan','on_white')
			return 404
		print colored('new','magenta'),
		try:
			content = urllib2.urlopen(self.url).read()
		except Exception as e:
			print colored('%d: a http error'%self.num, 'red'),
			print e
			if '404' in str(e):
				return 404
			if '403' in str(e):
				self.data.url.append(self.url)
				return 403
			if '503' in str(e) or '502' in str(e):
				self.data.url.append(self.url)
				return 503
			return 100
		print self.num,
		if 'celebrity' in self.url:
			self.subject = self._parsesubject(content)
			self.cele = self._parsenext(content)
			self._download(content)
			print colored('celebrity','green'),
		elif 'subject' in self.url:
			self._download(content)
			print colored('subject','blue'),
		print 'visiting: '+self.url,
		print colored('url:','yellow'),len(self.data.url)
		return True
	def put_url(self):
		for i in self.subject:
			filename = self._getsubjectfilename(i)
			if not os.path.exists(filename):
				self.data.url.append('http://movie.douban.com'+i)
		self.subject = []
		if self.cele:
			_id = re.compile('/\d+/').findall(self.url)[0][1:-1]
			self.data.url.append('http://movie.douban.com/celebrity/'+_id+'/movies?start='+self.cele)
		self.cele = ''
	def _parsesubject(self, content):
		return re.compile('/subject/\d+/').findall(content)
	def _parsenext(self, content):
		tmp = re.compile('<link\ rel="next".*').findall(content)
		if tmp:
			return re.compile('=\d+&').findall(tmp[0])[0][1:-1]
		else: return ''
	def _download(self, content):
		filename = self._getfilename()
		writer = open(filename, 'w')
		writer.write(content)
		writer.close()
	def _getfilename(self):
		_id = re.compile('/\d+/').findall(self.url)[0][1:-1]
		if 'subject' in self.url:
			filename = '../save/subject/'+_id+'.html'
		elif 'celebrity' in self.url:
			try:
				startpage = self.url.split('=')[1]
			except:
				startpage = ''
			filename = '../save/celebrity/'+_id+'_'+startpage+'.html'
		return filename
	def _getsubjectfilename(self, text):
		_id = re.compile('\d+').findall(text)[0]
		return '../save/subject/'+_id+'.html'
