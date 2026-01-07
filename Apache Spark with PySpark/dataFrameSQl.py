from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MySparkApp").getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("WARN")
print("Spark Context initialized with app name:", sc.appName)

df = spark.read.csv("employee.csv", header=True, inferSchema=True)
df.createOrReplaceTempView("employee")  # we can use createOrReplaceTempView instead of registerTempTable
#spark.sql("SELECT FIRST_NAME, SALARY FROM employee WHERE SALARY > 12000").show()
spark.sql("select job_id,count(*) from employee where group by job_id").show();
