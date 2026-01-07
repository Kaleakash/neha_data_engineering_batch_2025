from pyspark.sql import SparkSession
from pyspark.sql.functions import col
spark = SparkSession.builder.appName("Spark DataFrame Module").getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("WARN")
print("Spark Context initialized with app name:", sc.appName)

data = [("Alice", 34), ("Bob", 45), ("Cathy", 29), ("David", 67), 
        ("Eva", 23), ("Frank", 72)]
column = ["Name", "Age"]
df = spark.createDataFrame(data, column)
#df.show()          # name and age 

# display the dataframe schema details 
#df.printSchema()

# display the particular column
#df.select("Name").show()

# apply filter on dataframe
#df.filter(df.Age > 30).show()

# adding new column to dataframe
#df2 = df.withColumn("Senior Citizen", df.Age > 60)
#df2.show()
# adding new column with default value 
df.withColumn("Added Age", col('age')+10).show()
#df.withColumn("County", "USA").show()