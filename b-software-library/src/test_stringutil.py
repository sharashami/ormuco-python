import unittest
import stringutils

class TestStringUtils(unittest.TestCase):

    def test_compare(self):
        self.assertEqual(stringutils.compare("1.2", "1.1"), 1)
        self.assertEqual(stringutils.compare("1.1", "1.2"), -1)
        self.assertEqual(stringutils.compare("", ""), 0)
        self.assertEqual(stringutils.compare("1.1", "1.10"), -1)
        self.assertEqual(stringutils.compare("1.2", "1.10"), 1)
        self.assertEqual(stringutils.compare("2.1", "1"), 1)
        self.assertEqual(stringutils.compare("1", "2.1"), -1)
        self.assertEqual(stringutils.compare("A", "a"), -1)
        self.assertEqual(stringutils.compare("a", "A"), 1)
        self.assertEqual(stringutils.compare("Asd", "Avd"), -1)
        self.assertEqual(stringutils.compare("Ab", "A"), 1)
        
        with self.assertRaises(ValueError):
            stringutils.compare(None, None)

if __name__ == "__main__":
    unittest.main()