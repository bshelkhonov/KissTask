from typing import TextIO
import re


class Reader():
    """
    class for reading large files
    """

    def __init__(self, file: TextIO):
        self.file = file

    def read_words(self):
        for line in self.file:
            words = line.split()
            for word in words:
                yield word
