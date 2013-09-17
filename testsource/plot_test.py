#!/usr/bin/env python2.7
import matplotlib.pyplot as plt
import numpy as np
import pylab
#x=[477,1574,2282,2674,2997,3126,3313,3561,3765,4247,4860,5785]
#y=[1.4,1.35,1.30,1.25,1.2,1.1,1,0.9,0.8,0.7,0.6,0.5]
#x=[506,886,1247,1825,2936,3945,4272,4855]
#y=[108,220,312,455.6,732.1,982.5,1064,1208]
x=[156
k,b = pylab.polyfit(x,y,1)
o = [i*k for i in x]
#plt.plot(x,o,'r+')
plt.plot([x[0],x[-1]],[k*x[0]+b,k*x[-1]+b])
plt.plot(x,y,'*')
#plt.plot(x,y)
plt.grid(True)
plt.show()
print k,b
