from pyspark import SparkContext

sc = SparkContext("local", "Simple App")

rdd1 = sc.textFile("data/demo100.csv")
rdd1.cache()
print(type(rdd1))
#print("get all", rdd1.collect())
# copy python.exe python3.exe
# for FIX this warm
print("get how many lines", rdd1.count())
print("first line", rdd1.first())
print("get first n line", rdd1.take(3))

sc.stop()