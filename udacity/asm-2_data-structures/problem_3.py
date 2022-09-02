import sys
from typing import List


class Node:
    def __init__(self, character: str = None, frequency: int = None):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None
        self.bit: int = None


class PriorityQueue:
    def __init__(self, value):
        self.value = value
        self.head: Node = None


class MinHeap:
    def __init__(self, initial_size):
        self.cbt: List[Node] = [None for _ in range (initial_size)]
        self.next_index = 0

    def size(self):
        return self.next_index

    def pop(self):
        """
        Returns: the element at the top of the heap

        """
        if self.size() == 0:
            return None
        self.next_index -= 1

        lowest_frequency_node = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # place last element of the cbt at the root
        self.cbt[0] = last_element

        # we do not remove the elements,
        # rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = lowest_frequency_node
        self._down_heapify()

        return lowest_frequency_node

    def insert(self, node: Node):
        # insert element at the next index
        self.cbt[self.next_index] = node

        # heapify
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

    def _up_heapify(self):
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element.frequency > child_element.frequency:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            min_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                min_element = min(parent, left_child, key=lambda n: n.frequency)

            # compare with right child
            if right_child is not None:
                min_element = min(min_element, right_child, key=lambda n: n.frequency)

            # check if parent is rightly placed
            if min_element == parent:
                return

            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = left_child
                parent_index = left_child_index

            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = right_child
                parent_index = right_child_index


class HuffmanTree:
    def __init__(self, node: Node = None):
        self.root = node
        self.codes: dict = {}

    def get_root(self):
        return self.root

    def set_root(self, node: Node):
        self.root = node

    def generate_binary_code(self, node: Node, code: str = '') -> None:
        if node.left is None and node.right is None:
            self.codes[node.character] = code
            return

        if node.left is not None:
            code += '0'
            self.generate_binary_code(node.left, code)

        if node.right is not None:
            code += '1'
            self.generate_binary_code(node.right, code)


def huffman_encoding(data):

    if type(data) != str:
        return None

    # 1. Determine the frequency/priority of each character/Node
    characters_dict = {}
    for char in data:
        if characters_dict.get(char) is None:
            characters_dict[char] = Node(char, 1)
        else:
            characters_dict[char].frequency += 1

    # 2. Add to min heap
    min_heap = MinHeap(len(characters_dict))
    for _, node in characters_dict.items():
        min_heap.insert(node)
    # print(f'min heap: \n'
    #       f'{[node.character + " - " + str(node.frequency) if node.character else "None - " + str(node.frequency) for node in min_heap.cbt]}\n')

    # Create Huffman Tree
    huffman_tree = HuffmanTree()

    # remove every 2 lowest priority node
    while min_heap.size() > 1:
        min_node_1 = min_heap.pop()
        min_node_2 = min_heap.pop()

        # set new node and assign a bit for child node
        new_root_node = Node(character=None,
                             frequency=min_node_1.frequency + min_node_2.frequency)
        new_root_node.left = min_node_1
        new_root_node.left.bit = 0
        new_root_node.right = min_node_2
        new_root_node.right.bit = 1

        huffman_tree.set_root(new_root_node)

        # Add new node to the min heap
        min_heap.insert(new_root_node)

    huffman_tree.set_root(min_heap.pop())

    # 7. Generate encoded data
    huffman_tree.generate_binary_code(huffman_tree.get_root())

    encoded_data = ''
    for char in data:
        print(f'char: {char} - {huffman_tree.codes.get(char)}')
        encoded_data += huffman_tree.codes.get(char)

    return encoded_data, huffman_tree


def huffman_decoding(data, tree):
    pass


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    # print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print("The content of the encoded data is: {}\n".format(encoded_data))
    #
    # decoded_data = huffman_decoding(encoded_data, tree)
    #
    # print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3
