from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MySparkApp").getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("WARN")
print("Spark Context initialized with app name:", sc.appName)

rdd = sc.textFile("industry.csv") # create RDD from text file
print("RDD created from file 'industry.csv'")
print("First 5 lines in RDD:", rdd.take(5))  # action operation to take first 5 lines
print("Total number of lines in RDD:", rdd.count())  # action operation to count lines
print("Rdd collect ",rdd.collect())  # action operation to collect all lines