import sys
import heapq  # docs: https://docs.python.org/3/library/heapq.html#module-heapq
from abc import ABC
import string
import random


class Node(ABC):
    """Abstract node class containing one parameter - frequency of the character or a branch of characters.
    Provides magic methods add, lt, gt, eq for comparisons based on frequency."""

    def __init__(self, freq):
        try:
            assert type(freq) == int and freq >= 1
        except Exception:
            raise ValueError("Frequency must be a positive integer")
        self.freq = freq

    def __lt__(self, other):
        """Comparing nodes according to their frequency"""
        if other is None:
            return -1
        elif not isinstance(other, Node):
            return -1
        return self.freq < other.freq

    def __gt__(self, other):
        """Comparing nodes according to their frequency"""
        if other is None:
            return -1
        elif not isinstance(other, Node):
            return -1
        return self.freq < other.freq

    def __eq__(self, other):
        """Comparing nodes according to their frequency"""
        if other is None:
            return -1
        elif not isinstance(other, Node):
            return -1
        return self.freq == other.freq

    def __add__(self, other):
        """Adding two leaf nodes, creates an internal node"""

        # if adding to an empty Node "None"
        if other is None:
            return self

        freq_sum = self.freq + other.freq
        if self.freq > other.freq:
            return InternalNode(freq=freq_sum, left=other, right=self)
        else:
            return InternalNode(freq=freq_sum, left=self, right=other)


class LeafNode(Node):
    """Leaf node containing a character and its frequency. Cannot branch out left or right"""

    def __init__(self, char, freq):
        super().__init__(freq)
        self.char = char

    def __repr__(self):
        return f"({self.char}:{self.freq})"


class InternalNode(Node):
    """Internal node, a branch containing left and right nodes. It holds the combined frequency of both nodes on left
    and right side. It does not hold a character"""

    def __init__(self, freq, left=None, right=None):
        super().__init__(freq)
        self.left = left
        self.right = right

    def __repr__(self):
        return f"I [{self.freq}]\n<l:{self.left}><r:{self.right}>"


def generate_huffman_code(node, code=''):
    """A helper recursive function to generate Huffman Codes from a constructed tree"""

    codes = {}

    if node is None:
        return

    # If we've reached the leaf node, set the code for its character and return
    if type(node) == LeafNode:
        codes[node.char] = code
        return codes

    # We have internal node: recursively traverse the tree looking for a leaf, and update the codes
    codes.update(generate_huffman_code(node.left, code+"0"))
    codes.update(generate_huffman_code(node.right, code+"1"))

    return codes


def huffman_encoding(data):
    """Huffman encoding: given a string, outputs a tuple of encoded data, and a binary Huffman tree used to
    decode the data"""

    # if data is empty or None
    if data is None or len(data)==0:
        return "",LeafNode("",1)

    # Building frequency table (dict)
    frequencies = dict()
    for char in data:  # O(n): n - number of input characters
        frequencies[char] = frequencies.get(char, 0) + 1  # default is 0 if key not present

    # Create a priority heap of Nodes
    #   in worst case scenario, the number of elements in the 'frequency' dictionary is equal to the length
    #   of input data. This happens for singly-occurring characters, i.e. "ABCDEFG...".
    nodes = [LeafNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(nodes)  # in-place, O(n) linear transformation to priority queue / a.k.a. heap queue

    while len(nodes) > 1:  # while we still have some Nodes to add
        n1, n2 = heapq.heappop(nodes), heapq.heappop(nodes)  # pops two elements
        heapq.heappush(nodes, n1+n2)  # adds to elements together, and pushes them onto a priority queue

    tree = heapq.heappop(nodes)     # from a heap of one element extract our tree
    codes = generate_huffman_code(tree)     # generate huffman codes from the tree

    # Encode data with the codes
    encoded_data = ''.join([codes[char] for char in data])
    return encoded_data, tree


def huffman_decoding(data, tree):
    """Given encoded data and a binary Huffman tree used to encode the data, outputs a string containing
    the decoded data."""

    if(data==""):  # empty encoded string, means a single character was encoded, and tree is just a single leaf
        return tree.char * tree.freq

    decoded_data = ""
    curr_node = tree

    for bit in data:
        if type(curr_node) == LeafNode:
            decoded_data += curr_node.char
            curr_node = tree
        if bit == "0":
            curr_node = curr_node.left
        elif bit == "1":
            curr_node = curr_node.right

    # The last bit
    if type(curr_node) == LeafNode:
        decoded_data += curr_node.char

    return decoded_data


if __name__ == "__main__":

    # TEST #0 : provided tests
    print("Test #0")
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # TEST #1: edge case: a single character
    print("-"*10)
    print("Test #1")

    data = "A"
    encoded_data, tree = huffman_encoding(data)

    print(encoded_data == "")  # True
    print(huffman_decoding(encoded_data, tree))  # "A"
    print("-"*10+"\n")

    # TEST #2: a unique set of characters
    print("-"*10)
    print("Test #2")

    data = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded_data, tree = huffman_encoding(data)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))  # 44
    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))  # 75
    print(data == decoded_data)  # True

    print("-"*10+"\n")

    # TEST 3: edge case: a big random string
    print("-"*10)
    print("Test #3")

    N = int(1e6)  # 1 million random string (should take ~1-3s)
    data = ''.join(random.choice(string.ascii_uppercase) for _ in range(N))
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))  # random number
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))  # 1000049
    print(data == decoded_data)  # True

    # TEST 4: edge case: an empty string
    print("-"*10)
    print("Test #4")

    data = ""  # an empty string
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(data,tree)
    print(decoded_data)  # "", an empty string
    print(decoded_data == data)  # True

    # TEST 5: edge case: a single repetitive character
    print("-"*10)
    print("Test #5")

    data = "A"*10
    encoded_data,tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data,tree)

    print(encoded_data)  # "AAAAAAAAAA"
    print(decoded_data == data)  # True
