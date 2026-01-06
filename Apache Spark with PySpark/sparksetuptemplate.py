from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MySparkApp").getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("WARN")
print("Spark Context initialized with app name:", sc.appName)
