from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MySparkApp").getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("WARN")
print("Spark Context initialized with app name:", sc.appName)

df = spark.read.csv("employee.csv", header=True, inferSchema=True)
#df.show()         #   it display all information of csv file
#df.select("first_name", "salary").show()   # it display only first_name and salary column from csv file

#df.filter(df.SALARY > 12000).show()   # it display all information of employee whose salary is greater than 50000

# group by department and calculate sum salary 
#df.groupBy("DEPARTMENT_ID").sum("SALARY").show()

# order by column salary in descending order
df.orderBy(df.SALARY.desc()).show()