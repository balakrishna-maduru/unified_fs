from io import StringIO
import unittest
from unittest.mock import MagicMock
from file_system.readers.text_readers import ReadText, ReadJson, ReadYaml, ReadCsv

class TestTextReaders(unittest.TestCase):

    def setUp(self):
        self.file_system_mock = MagicMock()

    def test_read_text(self):
        # Mock the file system read_text method
        self.file_system_mock.read_text.return_value = "Hello, world!"

        # Initialize ReadText object
        text_reader = ReadText()

        # Call the read method
        result = text_reader.read("path/to/text_file.txt", self.file_system_mock)

        # Assert that the result is as expected
        self.assertEqual(result, "Hello, world!")

    def test_read_json(self):
        # Mock the file system read_text method
        self.file_system_mock.read_text.return_value = '{"key": "value"}'

        # Initialize ReadJson object
        json_reader = ReadJson()

        # Call the read method
        result = json_reader.read("path/to/json_file.json", self.file_system_mock)

        # Assert that the result is as expected
        self.assertEqual(result, {"key": "value"})

    def test_read_yaml(self):
        # Mock the file system read_txt method
        self.file_system_mock.read_text.return_value = "key: value\n"

        # Initialize ReadYaml object
        yaml_reader = ReadYaml()

        # Call the read method
        result = yaml_reader.read("path/to/yaml_file.yaml", self.file_system_mock)

        # Assert that the result is as expected
        self.assertEqual(result, {"key": "value"})

    def test_read_csv(self):
        # Mock the file system read_text method
        self.file_system_mock.read_text.return_value = StringIO("1,John\n2,Jane\n")

        # Initialize ReadCsv object
        csv_reader = ReadCsv()

        # Call the read method
        result = csv_reader.read("path/to/csv_file.csv", self.file_system_mock)
        rows = [row for row in result]
        # Assert that the result is as expected
        self.assertEqual(rows, [["1", "John"], ["2", "Jane"]])
            

if __name__ == "__main__":
    unittest.main()
