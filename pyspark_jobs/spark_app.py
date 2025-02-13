# dags/spark_app.py
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
    data = [("Alice", 34), ("Bob", 45), ("Catherine", 29)]
    df = spark.createDataFrame(data, ["Name", "Age"])
    df.show()
    spark.stop()
