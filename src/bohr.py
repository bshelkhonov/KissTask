from typing import Optional


class TaskBohr:
    """
    Bohr for lower Latin letters a-z
    """

    class Node:
        def __init__(self, info: Optional[dict] = None):
            self.next = dict()
            self.info = info

    def __init__(self):
        self.root = self.Node()

    def add_word(self, word: str, info: dict = None):
        current_node = self.root
        for letter in word:
            if letter in current_node.next:
                current_node = current_node.next[letter]
            else:
                new_node = self.Node(info)
                current_node.next[letter] = new_node
                current_node = new_node

    def find_word(self, key: str):
        if len(key) == 0:
            raise ValueError("key must not be empty")
        current_node = self.root

        for letter in key:
            if letter in current_node.next:
                current_node = current_node.next[letter]
            else:
                return False, None

        return True, current_node.info
