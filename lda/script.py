import codecs


trumpstring = "trump donald donaldtrump"
berniestring = "sanders bernie berniesanders"
hillarystring = "hillary clinton hillaryclinton"
cruzstring = "cruz ted tedcruz"


with open("../SVM/GroundTruth.txt","r") as f:
        for line in f:
                l = line.split(",")
                s = l[1].split()
                if float(l[0]) == 1:
                        for s1 in s:
                                if s1 in trumpstring:
					with open("trumppos.txt","a") as q:
						q.write(l[1])
						q.close()

with open("../data/OriginalTraining.txt","r") as f:
        for line in f:
                l = line.split(",")
                s = l[0].split()
                if float(l[1]) == 1:
                        for s1 in s:
                                if s1 in trumpstring:
                                        with open("trumppos.txt","a") as q:
                                                q.write(l[0])
                                                q.close()



