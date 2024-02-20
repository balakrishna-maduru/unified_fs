import unittest
from . import resources_path
from file_system.file_system import FileSystem

class TestFileSystem(unittest.TestCase):

    def setUp(self):
        # Set up the FileSystem object
        self.file_system = FileSystem("file")

    def test_read_text_file(self):
        
        test_file_path = f"{resources_path}/test.txt"
        with open(test_file_path, 'r') as file:
            expected_content = file.read()
        
        # Test reading a text file
        file_content = self.file_system.read(test_file_path)
        self.assertEqual(file_content, expected_content)

if __name__ == "__main__":
    unittest.main()
