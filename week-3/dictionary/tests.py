'''
Module for testing dictionary module.
'''
import unittest
from dictionary import dict_reader_tuple, dict_reader_dict, dict_invert


class TestDictReaderTuple(unittest.TestCase):
    def test_empty_file(self):
        """Tests reading an empty file."""
        with open("empty_file.txt", 'w') as f:
            pass  # Create an empty file
        result = dict_reader_tuple("empty_file.txt")
        self.assertEqual(result, [])

    def test_single_line(self):
        """Tests reading a file with a single line."""
        with open("single_line.txt", 'w') as f:
            f.write("WORD 1 TRANSLATION")
        result = dict_reader_tuple("single_line.txt")
        self.assertEqual(result, [("WORD", 1, ["TRANSLATION"])])

    def test_multiple_lines(self):
        """Tests reading a file with multiple lines."""
        with open("multiple_lines.txt", 'w') as f:
            f.write("WORD1 2 TRANS1 TRANS2\n")
            f.write("WORD2 1 ANOTHER_TRANSLATION\n")
        result = dict_reader_tuple("multiple_lines.txt")
        self.assertEqual(result, [
            ("WORD1", 2, ["TRANS1", "TRANS2"]),
            ("WORD2", 1, ["ANOTHER_TRANSLATION"])
        ])

    def test_invalid_file_type(self):
        """Tests handling of non-string file path."""
        self.assertIsNone(dict_reader_tuple(10))  # Pass an integer instead of string


class TestDictReaderDict(unittest.TestCase):
    def test_empty_file(self):
        """Tests reading an empty file."""
        with open("empty_file.txt", 'w') as f:
            pass  # Create an empty file
        result = dict_reader_dict("empty_file.txt")
        self.assertEqual(result, {})

    def test_single_line(self):
        """Tests reading a file with a single line."""
        with open("single_line.txt", 'w') as f:
            f.write("WORD 1 TRANSLATION")
        result = dict_reader_dict("single_line.txt")
        self.assertEqual(result, {"WORD": {("TRANSLATION",)}})

    def test_multiple_lines_same_word(self):
        """Tests reading a file with multiple lines for the same word."""
        with open("multiple_lines_same_word.txt", 'w') as f:
            f.write("WORD 2 TRANS1 TRANS2\n")
            f.write("WORD 2 ANOTHER_TRANSLATION\n")
        result = dict_reader_dict("multiple_lines_same_word.txt")
        self.assertEqual(result, {
            "WORD": {("TRANS1", "TRANS2"), ("ANOTHER_TRANSLATION",)}
        })

    def test_multiple_lines_different_words(self):
        """Tests reading a file with multiple lines for different words."""
        with open("multiple_lines_different_words.txt", 'w') as f:
            f.write("WORD1 2 TRANS1 TRANS2\n")
            f.write("WORD2 1 ANOTHER_TRANSLATION\n")
        result = dict_reader_dict("multiple_lines_different_words.txt")
        self.assertEqual(result, {
            "WORD1": {("TRANS1", "TRANS2")},
            "WORD2": {("ANOTHER_TRANSLATION",)},
        })

    def test_invalid_file_type(self):
        """Tests handling of non-string file path."""
        self.assertRaises(TypeError, dict_reader_dict, 10)  # Pass an integer instead of string


class TestDictInvert(unittest.TestCase):
    def test_empty_dict(self):
        """Tests inverting an empty dictionary."""
        result = dict_invert({})
        self.assertEqual(result, {})

    def test_single_entry(self):
        """Tests inverting a dictionary with a single entry."""
        input_dict = {"WORD": {("1", "TRANSLATION")}}
        result = dict_invert(input_dict)
        self.assertEqual(result, {1: {("WORD", ("1", "TRANSLATION"))}})

    def test_multiple_entries_same_pronunciation_count(self):
        """Tests inverting a dictionary with entries having the same pronunciation count."""
        input_dict = {
            "WORD1": {("2", "TRANS1", "TRANS2")},
            "WORD2": {("2", "ANOTHER1", "ANOTHER2")},
        }
        result = dict_invert(input_dict)
        self.assertEqual(result, {1: {('WORD2', ('2', 'ANOTHER1', 'ANOTHER2'))}})

    def test_multiple_entries_different_pronunciation_count(self):
        """Tests inverting a dictionary with entries having different pronunciation counts."""
        input_dict = {
            "WORD1": {("2", "TRANS1", "TRANS2")},
            "WORD2": {("1", "ANOTHER_TRANSLATION")},
        }
        result = dict_invert(input_dict)
        self.assertEqual(result, {1: {('WORD2', ('1', 'ANOTHER_TRANSLATION'))}})

    def test_list_input(self):
        """Tests inverting with a list input (converted to dict first)."""
        input_list = [("WORD", 1, ["TRANSLATION"])]
        result = dict_invert(input_list)
        self.assertEqual(result, {1: {("WORD", ("TRANSLATION",))}})

    def test_invalid_input_type(self):
        """Tests handling of non-list or non-dict input."""
        self.assertRaises(TypeError, dict_invert, 10)  # Pass an integer instead of list or dict

if __name__ == "__main__":
    unittest.main()
