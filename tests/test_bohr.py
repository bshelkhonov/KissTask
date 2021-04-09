import tempfile
import unittest

from src.bohr import TaskBohr


class TestBohr(unittest.TestCase):
    def setUp(self):
        self.bohr = TaskBohr()
        self.bohr.add_word("hello", {"test": "test"})

    def test_add_words(self):
        self.bohr.add_word("world", {"test2", "test2"})
        self.assertTrue("w" in self.bohr.root.next)

    def test_find_word(self):
        found, info = self.bohr.find_word("hello")
        self.assertTrue(found)
        self.assertTrue(info["test"] == "test")

        found, info = self.bohr.find_word("not_in_bohr")
        self.assertFalse(found)
        self.assertIsNone(info)


if __name__ == '__main__':
    unittest.main()
