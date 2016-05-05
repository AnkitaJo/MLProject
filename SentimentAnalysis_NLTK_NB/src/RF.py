from tempfile import NamedTemporaryFile
from fileinput import input
from pyspark.mllib.regression import LabeledPoint
from glob import glob
from pyspark.mllib.util import MLUtils
from pyspark.mllib.tree import RandomForest, RandomForestModel
from pyspark.mllib.util import MLUtils
#>>> examples = [LabeledPoint(1.1, Vectors.sparse(3, [(0, 1.23), (2, 4.56)])),                         LabeledPoint(0.0, Vectors.dense([1.01, 2.02, 3.03]))]
#>>> tempFile = NamedTemporaryFile(delete=True)
#>>> tempFile.close()
#>>> MLUtils.saveAsLibSVMFile(sc.parallelize(examples), tempFile.name)



from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.feature import HashingTF, IDF
from pyspark import SparkContext

sc=SparkContext("local","dd")
train = sc.parallelize(open("/home/madhura/ML_Spring16/MLProject/data/OriginalTraining.txt").read().splitlines()).map(lambda x: x.split(","))
trainlabels = train.map(lambda(a,b): int(b))
traintf = HashingTF().transform(train.map(lambda(a,b): a.split()))
trainidf = IDF().fit(traintf)
traintfidf = trainidf.transform(traintf)
#densetrain = traintfidf.map(lambda x: pyspark.mllib.linalg.DenseVector(x.toArray()))
#zippeddata = trainlabels.zip(densetrain)
#new = zippeddata.map(lambda (a,vec) : (a,vec.toArray()))
training = trainlabels.zip(traintfidf).map(lambda x : LabeledPoint(x[0], x[1]))
MLUtils.saveAsLibSVMFile(training.coalesce(1),"/home/madhura/ML_Spring16/MLProject/data/libsvmfile")
data = MLUtils.loadLibSVMFile(sc, "/home/madhura/ML_Spring16/MLProject/data/libsvmfile/part-00000")
(trainingData, testData) = data.randomSplit([0.7, 0.3])
model = RandomForest.trainClassifier(data, numClasses=2, categoricalFeaturesInfo={},
                                     numTrees=3, featureSubsetStrategy="auto",
                                     impurity='gini', maxDepth=4, maxBins=32)
model.save(sc, "/home/madhura/ML_Spring16/MLProject/SentimentAnalysis_NLTK_NB/src/myRandomForestClassificationModel")
