# A trie is a tree-like data structure that stores a dynamic set of strings.
# Tries are commonly used to facilitate operations like predictive text
# or autocomplete features on mobile phones or web search.

## Represents a single node in the Trie
from typing import List, Dict


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children: Dict[str, TrieNode] = {}

    def suffixes(self, suffix='') -> List[str]:
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        suffixes = []

        if self.is_word:
            suffixes.append(suffix)

        if self.children == {}:
            return [suffix]

        for key, node in self.children.items():
            child_subfixes = node.suffixes(suffix + key)
            suffixes.extend(child_subfixes)

        return suffixes


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix) -> TrieNode:
        if type(prefix) != str:
            print('Error: a prefix must be a string.')
            return

        ## Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                print(prefix + " not found")
                return
            current_node = current_node.children[char]

        print('\n'.join(current_node.suffixes()))


if __name__ == '__main__':
    my_trie = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in wordList:
        my_trie.insert(word)

    print('\n---------- Test 1 -----------')
    prefix = ""
    print('prefix: ', prefix)
    my_trie.find(prefix)

    print('\n---------- Test 2 -----------')
    prefix = None
    print('prefix: ', prefix)
    my_trie.find(prefix)

    print('\n---------- Test 3 -----------')
    prefix = "d"
    print('prefix: ', prefix)
    my_trie.find(prefix)

    print('\n---------- Test 4 -----------')
    prefix = "tri"
    print('prefix: ', prefix)
    my_trie.find(prefix)