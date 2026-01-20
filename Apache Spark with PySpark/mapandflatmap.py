from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MySparkApp").getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("WARN")
print("Spark Context initialized with app name:", sc.appName)

data = [1, 2, 3, 4, 5,6,7,8,9,10] # python list     one to one ie 1 to 1 mapping 
data1 = [[1,2,3,4],[5,6,7,8],[9,10]] # nested python list   one to many ie 1 to n mapping
rdd = sc.parallelize(data) # create RDD from python list
rdd1 = sc.parallelize(data1) # create RDD from nested python list
# map transformation
squared_rdd = rdd.map(lambda x: x * x)
# flatMap transformation    
squared_rdd1 = rdd1.flatMap(lambda x: [i * i for i in x])
print("Squared values using map:", squared_rdd.collect())
print("Squared values using map on nested list:", squared_rdd1.collect())