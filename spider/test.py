#!/usr/bin/env python2

from Queue import Queue
import pickle
import os

for a,b,files in os.walk('../newsave/'):
	for f in files:
		print f.split('.')[0]
