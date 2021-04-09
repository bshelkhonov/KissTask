from typing import TextIO
from collections import deque

from src.bohr import TaskBohr
from src.reader import Reader


class Solver:
    MAX_KEY_SIZE = 5
    STOP_KEY = "!exit"

    def __init__(self, filename: TextIO):
        self.file = filename
        self._build_bohr()

    def _build_bohr(self):
        self.bohr = TaskBohr()
        reader = Reader(self.file)

        words = deque()

        for index, word in enumerate(reader.read_words()):
            words.append((index, word))
            if len(words) >= self.MAX_KEY_SIZE:
                self._add_word(words)
                words.popleft()

        while len(words) > 0:
            self._add_word(words)
            words.popleft()

    def _add_word(self, words: deque):
        char_list = []
        word_idx = words[0][0] + 1
        for index, value in enumerate(words):
            _, word = value
            if index >= len(word):
                break
            char_list.append(word[index])
        self.bohr.add_word("".join(char_list), {"index": word_idx})

    def run(self):
        while True:
            print("Enter the key | Enter !exit to exit:", end=" ")
            key = input()
            if key == self.STOP_KEY:
                break

            found, info = self.bohr.find_word(key)

            if found:
                print("Success! Position:", info["index"])
            else:
                print("Fail! Try another key!")
