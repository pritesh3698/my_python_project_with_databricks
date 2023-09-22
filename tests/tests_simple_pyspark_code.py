import unittest
from pyspark.sql import SparkSession
from my_module.simple_pyspark_code import your_function  # Import the function you want to test

class TestYourCode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize a Spark session for testing
        cls.spark = SparkSession.builder \
            .appName("TestYourCode") \
            .getOrCreate()

    @classmethod
    def tearDownClass(cls):
        # Stop the Spark session after all tests
        cls.spark.stop()

    def test_your_function(self):
        # Define your test data
        test_data = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]
        columns = ["id", "name"]

        # Create a DataFrame from the test data
        test_df = self.spark.createDataFrame(test_data, columns)

        # Call the function you want to test
        result = your_function(test_df)

        # Assert that the result meets your expectations
        self.assertEqual(result.count(), 3)  # Example assertion

if __name__ == "__main__":
    unittest.main()
