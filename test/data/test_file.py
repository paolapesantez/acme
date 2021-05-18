import unittest
import os
from src.data.file import get_file_path, read_file_lines


class TestFile(unittest.TestCase):

    def setUp(self):
        # Check if OS is Windows
        if os.name == 'nt':
            self.input_file_path = 'src\\data\\input.txt'
            self.empty_input_file_path = 'src\\data\\empty_input.txt'
        else:
            self.input_file_path = 'src/data/employees.txt'
            self.empty_input_file_path = 'src/data/empty_file.txt'
    

    def test_get_file_path(self):
        current_dir = os.getcwd()
        expected_file_path = os.path.join(current_dir, self.input_file_path)

        file_path = get_file_path(self.input_file_path)

        self.assertEqual(file_path, expected_file_path)

    def test_read_store_file_lines(self):
        file_path = get_file_path(self.input_file_path)
        lines = read_file_lines(file_path)

        with open(file_path) as file:
            expected_content = file.readlines()

        self.assertEqual(lines, expected_content)

    def test_read_file_lines_empty(self):

        file_path = get_file_path(self.empty_input_file_path)

        with self.assertRaises(SystemExit) as ae:
            read_file_lines(file_path)

        self.assertEqual(ae.exception.code, 1)
