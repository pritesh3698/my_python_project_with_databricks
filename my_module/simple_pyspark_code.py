# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize a Spark session
spark = SparkSession.builder.appName("SimplePySparkExample").getOrCreate()

# Create a sample data
data = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("David", 28)]

# Define the schema for the DataFrame
schema = ["Name", "Age"]

# Create a DataFrame from the data and schema
df = spark.createDataFrame(data, schema=schema)

# Show the DataFrame
df.show()

# Perform a basic operation - Filter and show people aged 30 or older
filtered_df = df.filter(col("Age") >= 30)
filtered_df.show()

# Stop the Spark session
spark.stop()
