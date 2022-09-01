import sys


    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None


class PriorityQueue:
    def __init__(self, value):
        self.value = value
        self.head: Node = None


class HuffmanTree:
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def set_root(self, node: Node):
        self.root = node

    def add_node(self, node: Node, new_node: Node):
        if new_node.frequency <= node.frequency:
            if node.left is not None:
                self.add_node(node.left, new_node)
            else:
                node.left = new_node
        else:
            if node.right is not None:
                self.add_node(node.right, new_node)
            else:
                node.right = new_node

    def merge_min_priority_node(self, node: Node, node1: Node, node2: Node):
        if node1 is None:
            if node.left is None:
                node1 = node.left
                self.merge_min_priority_node(node.right, node1, None)
            else:
                self.merge_min_priority_node(node.left, None, None)
        elif node2 is None:
            if node.left is None:
                node2 = node.left
                self.merge_min_priority_node(node.right, node1, node2)
            else:
                self.merge_min_priority_node(node.left, node1, None)
        else:
            new_node = Node()
            new_node.frequency = node1.frequency + node2.frequency
            self.add_node(new_node, no1)
            self.add_node(self.root, new_node)



def huffman_encoding(data):

    # 1. Determine the frequency/priority of each character/Node

    characters = {}
    for char in data:
        if characters.get(char) is None:
            characters[char] = Node(char)
        else:
            characters[char].frequency += 1

    # 2. Sort by frequency
    tree = Tree()
    for _, node in characters.items():
        if tree.get_root().value is None:
            tree.set_root(node)
        else:
            tree.add_node(node=tree.get_root(), new_node=node)

    # 3. Pop-out two nodes with the minimum frequency and create a new node
    # with a frequency equal to the sum of that two nodes

    tree.merge_min_priority_node(tree.root, None, None)
    return tree


def huffman_decoding(data, tree):
    pass


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    # encoded_data, tree = huffman_encoding(a_great_sentence)
    test = huffman_encoding(a_great_sentence)

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
