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
        self.nodes = [self.Node()]

    def add_word(self, word: str, word_index: int):
        current_node = self.nodes[0]
        for letter in word:
            if letter in current_node.next:
                current_node = current_node.next[letter]
            else:
                self.nodes.append(self.Node({"index": word_index}))
                self.nodes[-2].next[letter] = self.nodes[-1]

    def find_word(self, key: str):
        if len(key) == 0:
            raise ValueError("key must not be empty")
        current_node = self.nodes[0]

        for letter in key:
            if letter in current_node.next:
                current_node = current_node.next[letter]
            else:
                return False, None

        return True, current_node.info["index"]
