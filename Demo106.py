import pyspark
from pyspark import SparkContext, SparkConf
from pprint import pprint

print(pyspark.__version__)

config1 = SparkConf().setAppName("hello pyspark").setMaster("local")
sc = SparkContext(conf=config1)
pprint(sc.getConf().getAll())
sc.stop()