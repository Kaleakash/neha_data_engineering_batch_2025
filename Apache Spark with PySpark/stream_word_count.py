from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split

spark = SparkSession.builder.appName("StructuredStreaming").getOrCreate()

df = spark.readStream.format("socket") \
    .option("host","localhost") \
    .option("port",9999) \
    .load()

words = df.select(explode(split(df.value," ")).alias("word"))

counts = words.groupBy("word").count()

query = counts.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
