import tempfile
import unittest

from src.reader import Reader


class TestReader(unittest.TestCase):
    def test_read_words(self):
        words = ["This", "is", "words,", "Anthony!"]
        with tempfile.TemporaryFile(mode="w+") as tmp:
            tmp.write(" ".join(words))
            tmp.seek(0)
            reader = Reader(tmp)
            self.assertEqual(words, [w for w in reader.read_words()])


if __name__ == '__main__':
    unittest.main()
