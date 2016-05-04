import codecs
import itertools

correctly_classified = 0.0
incorrectly_classified = 0.0
total = 0.0
with open("GroundTruth.txt","r") as a, open("NBResult.txt","r") as b:
	for line1,line2 in itertools.izip(a,b):
		l1 = line1.split(",")
		l2 = line2.split(",")
		total += 1.0
		if(float(l1[0]) == float(l2[0])):
			correctly_classified += 1.0
		else:
			incorrectly_classified += 1.0


print("correct%: ", correctly_classified/total*100)
print("incorrect%: ",incorrectly_classified/total*100)
