from nltk.classify import NaiveBayesClassifier
from pyspark.mllib.classification import NaiveBayes, NaiveBayesModel
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.feature import HashingTF, IDF

train = sc.parallelize(open("/home/madhura/ML_Spring16/MLProject/SentimentAnalysis_NLTK_NB/labeled1.txt").read().splitlines()).map(lambda x: x.split(","))
test = sc.parallelize(open("/home/madhura/ML_Spring16/MLProject/withoutHashTag2.txt").read().splitlines()).map(lambda x: x.split(","))
trainlabels = train.map(lambda(a,b): int(b))
testlabels = test.map(lambda(a,b): int(a))
traintf = HashingTF(numFeatures=500).transform(train.map(lambda(a,b): a.split()))
testf = HashingTF(numFeatures=500).transform(test.map(lambda(a,b): b.split()))
trainidf = IDF().fit(traintf)
testidf = IDF().fit(traintf)
traintfidf = idf.transform(traintf)
testtfidf = idf.transform(testtf)
training = trainlabels.zip(traintfidf).map(lambda x : LabeledPoint(x[0], x[1]))
testing = testlabels.zip(testtfidf).map(lambda x : LabeledPoint(x[0], x[1]))
model = NaiveBayes.train(training)
predictionAndLabel = testing.map(lambda p: (model.predict(p.features), p.label))
newlabels = predictionAndLabel.map(lambda(a,b): a)
joined = newlabels.zip(test.map(lambda(a,b): b))
joined.coalesce(1).saveAsTextFile("/home/madhura/ML_Spring16/MLProject/SentimentAnalysis_NLTK_NB/testedData.txt")
