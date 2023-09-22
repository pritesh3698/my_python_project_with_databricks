from pyspark.sql import SparkSession

def main():
    # Initialize a Spark session
    spark = SparkSession.builder.appName("SimpleSparkExample").getOrCreate()

    # Sample data
    data = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]
    columns = ["id", "name"]

    # Create a Spark DataFrame
    df = spark.createDataFrame(data, columns)

    # Perform a simple transformation
    transformed_df = df.withColumn("greeting", df.name + " says hello!")

    # Show the transformed DataFrame
    transformed_df.show()

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    main()
