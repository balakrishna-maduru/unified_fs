"""This module contains the tests for the file_system module and its operations. """
import os
import unittest
from file_system.file_system import FileSystem
from . import resources_path

class TestFileSystem(unittest.TestCase):

    def setUp(self):
        # Set up the FileSystem object
        self.file_system = FileSystem()
        # Set the source file system to local and destination file system to S3
        self.file_system.source_fs = "file"
        self.file_system.destination_fs = {"type":"s3", "key":os.getenv("AWS_ACCESS_KEY_ID"), "secret":os.getenv("AWS_SECRET_ACCESS_KEY")}

    def test_copy_file(self):
        # Set the source file system to local and destination file system to S3
        self.file_system.source_fs = "file"
        self.file_system.destination_fs = {"type":"s3", "key":os.getenv("AWS_ACCESS_KEY_ID"), "secret":os.getenv("AWS_SECRET_ACCESS_KEY")}
        self.file_system.copy(f"{resources_path}/test.txt", "s3://my-test-1124/file.txt")
        # Assert that the file exists in the destination
        self.assertTrue(self.file_system.exists("s3://my-test-1124/file.txt", target_fs=True))

    def test_move_file(self):
        # Set the source file system to local and destination file system to S3
        self.file_system.source_fs = "file"
        self.file_system.destination_fs = "file"
        self.file_system.copy(f"{resources_path}/test_move_copy.txt", f"{resources_path}/test_move.txt")
        self.file_system.destination_fs = {"type":"s3", "key":os.getenv("AWS_ACCESS_KEY_ID"), "secret":os.getenv("AWS_SECRET_ACCESS_KEY")}
        # Perform the move operation
        self.file_system.move(f"{resources_path}/test_move.txt", "s3://my-test-1124/file1.txt")

        # Assert that the file exists in the destination
        self.assertTrue(self.file_system.exists("s3://my-test-1124/file1.txt", target_fs=True))

    def test_remove_file(self):
        # Set the source file system to S3
        self.file_system.source_fs = {"type":"s3", "key":os.getenv("AWS_ACCESS_KEY_ID"), "secret":os.getenv("AWS_SECRET_ACCESS_KEY")}
        
        # Perform the remove operation
        self.file_system.rm("s3://my-test-1124/file1.txt")

        # Assert that the file does not exist
        self.assertFalse(self.file_system.exists("s3://my-test-1124/file1.txt"))

    def test_make_directory(self):
        # Set the destination file system to S3
        self.file_system.source_fs = 'file'

        # Perform the make directory operation
        self.file_system.mkdir(f"{resources_path}/new_directory")

        # Assert that the directory exists
        self.assertTrue(self.file_system.exists(f"{resources_path}/new_directory"))

    def test_list_directory(self):
        # Set the source file system to S3
        self.file_system.source_fs = "file"
        
        # List the contents of the directory
        contents = self.file_system.ls(resources_path)

        # Assert that the directory contains expected items
        for item in contents:
            if item.get("name") == f"{resources_path}/test.txt":
                self.assertTrue(item.get("type") == "file")
            if item.get("name") == f"{resources_path}/new_directory":
                self.assertTrue(item.get("type") == "directory")

    def test_read_text_file(self):
        # Set the source file system to S3
        self.file_system.source_fs = "file"
        
        # Read the contents of a text file
        content = self.file_system.read_text(f"{resources_path}/test.txt")
        
        # Assert that content is not empty
        self.assertTrue(content)

    def test_write_text_file(self):
        # Set the destination file system to S3
        self.file_system.destination_fs = "file"
        
        # Write content to a text file
        content = "Hello, world!"
        self.file_system.write_text(f"{resources_path}/new_file.txt", content)

        # Read the contents of the written file
        read_content = self.file_system.read_text(f"{resources_path}/new_file.txt")

        # Assert that the written content matches the read content
        self.assertEqual(content, read_content)

    def test_walk_directory(self):
        # Set the source file system to S3
        self.file_system.source_fs = "file"
        
        # Walk through the directory
        walk_result = self.file_system.walk(resources_path)

        # Assert that the walk result is not empty
        self.assertTrue(walk_result)

    def test_find_file(self):
        # Set the source file system to S3
        self.file_system.source_fs = "file"
        
        # Find a specific file
        found_files = self.file_system.find(resources_path, detail=True)

        # Assert that the found_files list is not empty
        self.assertTrue(found_files)


if __name__ == "__main__":
    unittest.main()
