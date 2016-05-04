#Code to read the hash tags and follow the trends on twitter

#import pylab as plt
import matplotlib.pyplot as plt
from matplotlib import pylab as p
import codecs
import numpy as np
import sys  
import operator

hashtags ={}
with open("file1.txt") as f:
	for line in f:
		tweet = line.split(",")
		t = tweet[1].split()
		for i in range (0, len(t)):
			if t[i].startswith('#'):
				if t[i] in hashtags:
					hashtags[t[i]]+=1.0
				else:
					hashtags[t[i]]=1.0
"""
for keys,values in hashtags.items():
	print(keys+": "+str(values))
"""
reload(sys)
sys.setdefaultencoding('utf8')

newA = dict(sorted(hashtags.iteritems(), key=operator.itemgetter(1), reverse=True)[:10])
#plot
"""
names = hashtags.keys()
counts = hashtags.values()
p.figure(1)
x = range(len(hashtags.keys()))
#plt.xticks(names, LABELS)
p.plot(x,hashtags.values(),'b')
p.show()
"""

import pylab as plt

hashes = range(len(newA.keys()))
counts = newA.values()

LABELS = newA.keys()

plt.bar(hashes, counts, align ='center')
plt.xticks(hashes, LABELS)
plt.show()

