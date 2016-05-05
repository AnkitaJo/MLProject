import codecs
import itertools

correctly_classified = 0.0
incorrectly_classified = 0.0
false_neg = 0.0
false_pos = 0.0
true_pos = 0.0
true_neg = 0.0
total = 0.0

with open("../SVM/GroundTruth.txt","r") as a, open("NBResult.txt","r") as b:
	for line1,line2 in itertools.izip(a,b):
		l1 = line1.split(",")
		l2 = line2.split(",")
		total += 1.0
		if(float(l1[0]) == 0 and float(l2[0]) == 0):
			true_neg += 1.0
		if(float(l1[0]) == 1 and float(l2[0]) == 0):
			false_neg += 1.0
		if(float(l1[0]) == 1 and float(l2[0])== 1):
			true_pos += 1.0
		if(float(l1[0]) == 0 and float(l2[0]) == 1):
			false_pos += 1.0
		total += 1.0
			
print("Fscore:", float(2*true_pos)/(2*true_pos + false_pos + false_neg))
print("Test Error = ", float(false_neg + false_pos)/total)
#print("correct%: ", correctly_classified/total*100)
#print("incorrect%: ",incorrectly_classified/total*100)
