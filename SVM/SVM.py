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


sc=SparkContext("local","dd")
sqlContext = SQLContext(sc)

lines = sc.textFile("/home/ankita/MLProject/data/OriginalTraining.txt")

parts = lines.map(lambda l: l.split(","))
indexedTweets = parts.zipWithIndex()
f = indexedTweets.map(lambda p: Row(tindex=int(p[1]),tweet=p[0][0], label= int(float(p[0][1]))))
#f = parts.map(lambda p: Row(tweet=p[0],label=int(p[1])))

schemaTweets = sqlContext.createDataFrame(f)

schemaTweets.registerTempTable("data")

tokenizer = Tokenizer(inputCol="tweet", outputCol="words")
wordsData = tokenizer.transform(schemaTweets)

hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures")
featurizedData = hashingTF.transform(wordsData)


idf = IDF(inputCol="rawFeatures", outputCol="features")



idfModel = idf.fit(featurizedData)
rescaledData = idfModel.transform(featurizedData)

wordsvectors = rescaledData["label","features"].map(lambda row: LabeledPoint(row[0], row[1]))
model = SVMWithSGD.train(wordsvectors, iterations=100)

labelsAndPreds = wordsvectors.map(lambda p: (p.label, model.predict(p.features)))
trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(wordsvectors.count())
print("Training Error = " + str(trainErr))
model.save(sc, "/home/ankita/MLProject/SVM/myModelPath")
