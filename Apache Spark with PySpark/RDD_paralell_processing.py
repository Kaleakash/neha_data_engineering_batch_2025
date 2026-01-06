from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MySparkApp").getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("WARN")
print("Spark Context initialized with app name:", sc.appName)

data = [1, 2, 3, 4, 5,6,7,8,9,10] # python list 
rdd = sc.parallelize(data) # create RDD from python list
# we can perform parallel processing on RDD
double = rdd.map(lambda x: x * 2) # double each element in RDD
print("Original RDD data:", double.collect())  # is a lazy operation
even = rdd.filter(lambda x: x % 2 == 0) # filter even numbers from RDD
print("Even numbers in RDD:", even.collect())  # is a lazy operation
odd = rdd.filter(lambda x: x % 2 != 0) # filter odd numbers from RDD
print("Odd numbers in RDD:", odd.collect())  # is a lazy operation
sum_all = rdd.reduce(lambda x, y: x + y) # sum all elements in RDD
print("Sum of all elements in RDD:", sum_all)  # action operation