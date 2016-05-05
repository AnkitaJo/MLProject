import codecs
import numpy as np
neg = 0.0
pos = 0.0

candidatepos = [0,0,0,0]
candidateneg = [0,0,0,0]

trumpstring = "trump donald donaldtrump"
berniestring = "sanders bernie berniesanders"
hillarystring = "hillary clinton hillaryclinton"
cruzstring = "cruz ted tedcruz"


with open("GroundTruth.txt","r") as f:
	for line in f:
		l = line.split(",")
		s = l[1].split()
		if float(l[0]) == 0:
			neg += 1.0
			for s1 in s:
                        	if s1 in trumpstring:
                                	candidateneg[0] += 1
                        	if s1 in berniestring:
                                	candidateneg[1] += 1
                        	if s1 in hillarystring:
                                	candidateneg[2] += 1
                        	if s1 in cruzstring:
                                	candidateneg[3] += 1
	
		if float(l[0]) == 1:
			pos += 1.0
			for s1 in s:
               			if s1 in trumpstring:
                        		candidatepos[0] += 1
                		if s1 in berniestring:
                        		candidatepos[1] += 1
                		if s1 in hillarystring:
                        		candidatepos[2] += 1
                		if s1 in cruzstring:
                        		candidatepos[3] += 1
f.close()


with open("OriginalTraining.txt","r") as f:
	for line in f:
		l = line.split(",")
		s = l[0].split()	
		if float(l[1]) == 1:
			pos += 1.0
			for s1 in s:
                                if s1 in trumpstring:
                                        candidatepos[0] += 1
                                if s1 in berniestring:
                                        candidatepos[1] += 1
                                if s1 in hillarystring:
                                        candidatepos[2] += 1
                                if s1 in cruzstring:
                                        candidatepos[3] += 1
	
		if float(l[1]) == 0:
			neg += 1.0
			for s1 in s:
                                if s1 in trumpstring:
                                        candidateneg[0] += 1
                                if s1 in berniestring:
                                        candidateneg[1] += 1
                                if s1 in hillarystring:
                                        candidateneg[2] += 1
                                if s1 in cruzstring:
                                        candidateneg[3] += 1

f.close()

"""
print("Pos: ",pos)
print("Neg: ",neg)
print("total: ",pos+neg)


print("Positive about trump", candidatepos[0])
print("positive about bernie",candidatepos[1])	
print("Positive about hillary",candidatepos[2])
print("Positive about cruz", candidatepos[3])

print("Negative about trump", candidateneg[0])
print("Negative about bernie",candidateneg[1])  
print("Negative about hillary",candidateneg[2])
print("Negative about cruz", candidateneg[3])
"""

candidate = candidatepos + candidateneg
#print(candidate)
import pylab as plt

x = np.array([1,2,3,4,5,6,7,8])
y = np.array(candidate)
LABELS = ["trumppos", "berniepos","hillarypos","cruzpos","trumpneg", "bernieneg","hillaryneg","cruzneg"]
plt.bar(x, y,align = 'center',width = 0.5)
plt.xticks(x, LABELS)
plt.show()

