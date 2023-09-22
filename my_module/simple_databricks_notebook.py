from pyspark.sql import SparkSession

# create a SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()

# create a DataFrame from a list of tuples
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
df = spark.createDataFrame(data, ["name", "age"])

# show the DataFrame
df.show()

# filter the DataFrame
filtered_df = df.filter(df.age > 30)

# show the filtered DataFrame
filtered_df.show()

# stop the SparkSession
spark.stop()