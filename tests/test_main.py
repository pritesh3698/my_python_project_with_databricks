
import unittest
from pyspark.sql import SparkSession
from my_module.main import main

class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder.appName("TestSimpleSparkExample").getOrCreate()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_main(self):
        # Redirect stdout to capture output
        import sys
        from io import StringIO
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        # Run the main function
        main()

        # Get the captured output
        output = sys.stdout.getvalue()

        # Restore stdout
        sys.stdout = original_stdout

        # Assert that the output contains "Alice says hello!"
        self.assertIn("Alice says hello!", output)

if __name__ == "__main__":
    unittest.main()
