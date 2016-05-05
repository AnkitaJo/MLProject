#import pylab as plt
import matplotlib.pyplot as plt
from matplotlib import pylab as p
import codecs
import numpy as np
import sys
import operator

candidate = [0,0,0,0]

trumpstring = "trump donald donaldtrump"
berniestring = "sanders bernie berniesanders"
hillarystring = "hillary clinton hillaryclinton"
cruzstring = "cruz ted tedcruz"

with open("../originalWithoutHashtags1.txt") as f:
        for l in f:
		line = l.lower()
		s = line.split()
		for s1 in s: 
                	if s1 in trumpstring:
                		candidate[0] += 1
			if s1 in berniestring:
				candidate[1] += 1
			if s1 in hillarystring:
				candidate[2] += 1
			if s1 in cruzstring:
				candidate[3] += 1

print(candidate)

reload(sys)
sys.setdefaultencoding('utf8')

#plot
import pylab as plt

x = np.array([1,2,3,4])
y = np.array(candidate)
LABELS = ["trump", "bernie","hillary","cruz"]
plt.bar(x, y,align = 'center',width = 0.005)
plt.xticks(x, LABELS)
plt.show()



