from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, to_date, avg
from pyspark.sql.window import Window

# ---------------------------
# 1. Spark Session
# ---------------------------
spark = SparkSession.builder \
    .appName("LogAnalyticsPipeline") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# ---------------------------
# 2. Read Logs
# ---------------------------
logs_df = spark.read.option("header", True).option("inferSchema", True) \
    .csv("data/application_logs.csv")

# ---------------------------
# 3. Preprocessing
# ---------------------------
logs_df = logs_df.withColumn(
    "log_date",
    to_date(col("timestamp"))
)

# ---------------------------
# 4. Filter Error Logs
# ---------------------------
error_logs = logs_df.filter(col("level") == "ERROR")

# ---------------------------
# 5. Daily Error Count Per Service
# ---------------------------
daily_errors = error_logs.groupBy("log_date", "service") \
    .agg(count("*").alias("error_count"))

# ---------------------------
# 6. Anomaly Detection (Error Spike)
# ---------------------------
window = Window.partitionBy("service")

avg_errors = daily_errors.withColumn(
    "avg_error_count",
    avg("error_count").over(window)
)

anomalies = avg_errors.filter(
    col("error_count") > col("avg_error_count") * 1.5
)

# ---------------------------
# 7. Optimized Writes
# ---------------------------
daily_errors.write \
    .mode("overwrite") \
    .partitionBy("log_date") \
    .parquet("output/daily_errors")

anomalies.write \
    .mode("overwrite") \
    .partitionBy("log_date") \
    .parquet("output/anomaly_services")

print("Log Analytics ETL Completed 🚀")
