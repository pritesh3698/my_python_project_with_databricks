import unittest
from pyspark.sql import SparkSession
from my_module.simple_pyspark_code import process_data

class TestProcessData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create a SparkSession for testing
        cls.spark = SparkSession.builder.appName("TestApp").master("local[*]").getOrCreate()

    @classmethod
    def tearDownClass(cls):
        # stop the SparkSession after testing
        cls.spark.stop()

    def test_process_data(self):
        # define the input data
        input_data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

        # create a DataFrame from the input data
        input_df = self.spark.createDataFrame(input_data, ["name", "age"])

        # process the input DataFrame
        output_df = process_data(input_df)

        # check the schema of the output DataFrame
        expected_schema = "name: string, age: integer, age_squared: double"
        self.assertEqual(str(output_df.schema), expected_schema)

        # check the data of the output DataFrame
        expected_data = [("Bob", 30, 900.0), ("Charlie", 35, 1225.0)]
        actual_data = [(r.name, r.age, r.age_squared) for r in output_df.collect()]
        self.assertEqual(actual_data, expected_data)

if __name__ == '__main__':
    unittest.main()