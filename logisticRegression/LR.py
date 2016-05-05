from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark import SparkContext
from fileinput import input
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint
from glob import glob
from pyspark.mllib.util import MLUtils
from pyspark.sql import SQLContext, Row
from pyspark.sql.types import *
from pyspark.ml.feature import HashingTF,IDF,Tokenizer
from pyspark import SparkContext
from pyspark.mllib.classification import LogisticRegressionWithLBFGS, LogisticRegressionModel

sc=SparkContext("local","dd")
sqlContext = SQLContext(sc)

lines = sc.textFile("/home/ankita/MLProject/data/OriginalTraining.txt")

parts = lines.map(lambda l: l.split(","))
indexedTweets = parts.zipWithIndex()
trainingCount=parts.count()
f = indexedTweets.map(lambda p: Row(tindex=int(p[1]),tweet=p[0][0], label= int(float(p[0][1])), training=1))
#f = parts.map(lambda p: Row(tweet=p[0],label=int(p[1])))

linest = sc.textFile("/home/ankita/MLProject/SVM/GroundTruth.txt")

partst = linest.map(lambda l: l.split(","))
indexedTweetst = partst.zipWithIndex().map(lambda (a,b): (a,b+trainingCount))
ft = indexedTweetst.map(lambda p: Row(tindex=int(p[1]),tweet=p[0][1], label= int(float(p[0][0])),training=0))
alldata = f.union(ft)

schemaTweets = sqlContext.createDataFrame(alldata)

schemaTweets.registerTempTable("data")

tokenizer = Tokenizer(inputCol="tweet", outputCol="words")
wordsData = tokenizer.transform(schemaTweets)

hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures")
featurizedData = hashingTF.transform(wordsData)


idf = IDF(inputCol="rawFeatures", outputCol="features")



idfModel = idf.fit(featurizedData)
rescaledData = idfModel.transform(featurizedData)
#rescaledData.collect()
wordsvectors = rescaledData.filter(rescaledData.training==1)["label","features"].map(lambda row: LabeledPoint(row[0], row[1]))
model = LogisticRegressionWithLBFGS.train(wordsvectors, iterations=100)

labelsAndPreds = wordsvectors.map(lambda p: (p.label, model.predict(p.features)))
trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(wordsvectors.count())
print("Training Error = " + str(trainErr))
#model.save(sc, "/home/ankita/MLProject/SVM/myModelPath3")
resct=rescaledData.filter(rescaledData.training==0)
labelsAndPreds =resct.map(lambda p: (p.label, model.predict(p.features)))
trueneg = labelsAndPreds.filter(lambda (v,p): v==0 and p==0).count() 
falseneg = labelsAndPreds.filter(lambda (v,p): v==1 and p==0).count() 
truepos = labelsAndPreds.filter(lambda (v,p): v==1 and p==1).count()
falsepos = labelsAndPreds.filter(lambda (v,p): v==0 and p==1).count()

print("false negative:", falseneg)
print("false positive:", falsepos)
print("true negative:", trueneg)
print("true positive:", truepos)
print("Fscore:", float(2*truepos)/(2*truepos + falsepos + falseneg))

print("Test Error = ", float(falseneg + falsepos)/resct.count())
