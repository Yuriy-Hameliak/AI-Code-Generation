"""q"""
import unittest
from all_prefixes import all_prefixes

class TestPrefixes(unittest.TestCase):
    """d"""
    def test_all_prefixes(self):
        """A"""
        self.assertEqual(all_prefixes('lead'),{"l", "le", "lea", "lead"})
        self.assertEqual(all_prefixes(''),'Empty line')
        self.assertEqual(all_prefixes('авангард'),{"а", "ав", "ава", "аван", "аванг", "аванга",
        "авангар", "авангард", "ан", "анг", "анга", "ангар", "ангард", "ар", "ард"})
        with self.assertRaises(TypeError):
            all_prefixes(2)

if __name__ == "__main__":
    unittest.main()
