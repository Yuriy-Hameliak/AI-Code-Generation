"""d"""
import unittest
from all_prefixes import all_prefixes

class TestAllPrefixes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), 'Empty line')
        # self.assertEqual(all_prefixes(''), {'Empty line'})

    def test_single_character_string(self):
        self.assertEqual(all_prefixes('a'), {'a'})

    def test_multiple_characters_string(self):
        self.assertEqual(all_prefixes('abc'), {'a', 'ab', 'abc'})

    def test_prefix_with_repeated_characters(self):
        self.assertEqual(all_prefixes('abbccc'), {'a', 'ab', 'abb', 'abbc', 'abbcc', 'abbccc'})

    def test_non_string_argument(self):
        with self.assertRaises(TypeError):
            all_prefixes(10)

if __name__ == '__main__':
    unittest.main()