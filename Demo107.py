from pyspark import SparkConf, SparkContext

from pyspark.sql import SparkSession
from pprint import pprint
spark = SparkSession.builder.appName("hello spark2").getOrCreate()
pprint(spark.sparkContext.getConf().getAll())
spark.sparkContext.stop()