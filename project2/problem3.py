import sys

class HuffmanNode():
    '''
    HuffmanNode has properties of doubly linked list and a tree.
    '''
    def __init__(self, char, count):
        self.char = char
        self.count = count
        self.next = None
        self.previous = None
        self.left = None
        self.right = None
        self.huffman_bit = None

    def get_char(self):
        return self.char

    def get_count(self):
        return self.count

    def set_huffman_bit(self, bit):
        self.huffman_bit = bit

    def get_huffman_bit(self):
        return self.huffman_bit

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None


class SortedQueue():
    def __init__(self):
        self.lowest_freq = None
        self.highest_freq = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def insert(self, new_node):
        '''
        Inserts node in order of lowest to highest count. If duplicate count, insert after the last duplicate.
        '''
        if self.lowest_freq is None:
            self.lowest_freq = new_node
            self.highest_freq = self.lowest_freq

        elif self.lowest_freq.count > new_node.count:
            new_node.next = self.lowest_freq
            self.lowest_freq.previous = new_node
            self.lowest_freq = new_node

        elif self.highest_freq.count <= new_node.count:
            self.highest_freq.next = new_node
            new_node.previous = self.highest_freq
            self.highest_freq = new_node

        else:
            current_node = self.lowest_freq
            while current_node.next:
                if current_node.count <= new_node.count and current_node.next.count > new_node.count:
                    latter_node = current_node.next
                    new_node.next = latter_node
                    latter_node.previous = new_node
                    current_node.next = new_node
                    new_node.previous = current_node
                    break
                else:
                    current_node = current_node.next
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.lowest_freq
        self.lowest_freq = self.lowest_freq.next
        if self.lowest_freq is not None:
            self.lowest_freq.previous = None
        self.size -= 1
        return popped_node

def get_frequency_of_chars(data):
    char_count = {}
    for char in data:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def encoding_traverse_helper(node, code_dict, huffman_code):
    '''
    Employs post-order DFS to get to all the leaves and collect the bits along the way.
    '''
    if node:
        # if not the root node, get the huffman bit for the node and add it to the running string.
        if node.get_huffman_bit() is not None:
            huffman_code = huffman_code + str(node.get_huffman_bit())
        # traverse the left subtree
        encoding_traverse_helper(node.get_left_child(),  code_dict, huffman_code)
        # traverse the right subtree
        encoding_traverse_helper(node.get_right_child(), code_dict, huffman_code)
        # at a leaf, log the huffman code and reset it for the next leaf.
        if node.get_char()!='':
            code_dict[node.get_char()] = huffman_code
            huffman_code = ''

        return code_dict

def traverse_tree_for_encoding(root):
    code_dict = {}
    huffman_code = ''
    encoding_traverse_helper(root, code_dict, huffman_code)
    return code_dict

def serialize_encoded_data(code_dict, data):
    encoded_data=''
    for char in data:
        encoded_data = encoded_data + code_dict[char]
    return encoded_data

def huffman_encoding(data):
    char_count = get_frequency_of_chars(data)
    #build sorted list
    sorted_queue = SortedQueue()
    for char, count in char_count.items():
        new_node = HuffmanNode(char, count)
        sorted_queue.insert(new_node)

    if sorted_queue.size == 1:
        root = sorted_queue.pop()

    #build Huffman tree
    while sorted_queue.size > 1:
        lowest_freq_1 = sorted_queue.pop()
        left_child = lowest_freq_1
        left_child.set_huffman_bit(0)

        lowest_freq_2 = sorted_queue.pop()
        right_child = lowest_freq_2
        right_child.set_huffman_bit(1)

        root_count = lowest_freq_1.count + lowest_freq_2.count
        root = HuffmanNode('', root_count)
        root.set_left_child(left_child)
        root.set_right_child(right_child)
        sorted_queue.insert(root)

    code_dict = traverse_tree_for_encoding(root)

    encoded_data = serialize_encoded_data(code_dict, data)


    return encoded_data, root

def huffman_decoding(data, tree):

    decoded_data = ''
    current_node = tree

    # if there are no bits, then we know tree is made up of only one node, ie one character.
    if not data:
        decoded_data = current_node.get_char() * current_node.get_count()
        return decoded_data

    for bit in data:
        if not current_node.has_left_child() and not current_node.has_right_child():
            decoded_data = decoded_data + current_node.get_char()
            current_node = tree

        if bit == '0':
            current_node = current_node.get_left_child()
        elif bit == '1':
            current_node = current_node.get_right_child()

    decoded_data = decoded_data + current_node.get_char()

    return decoded_data

if __name__ == "__main__":

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    #The size of the data is: 69
    print ("The content of the data is: {}\n".format(a_great_sentence))
    #The content of the data is: The bird is the word
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #The size of the encoded data is: 36
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #The content of the encoded data is: 0110111011111100111000001010110000100011010011110111111010101011001010
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #The size of the decoded data is: 69
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: The bird is the word


    another_great_sentence = "Hi my name is Ana Chisholm."

    print ("The size of the data is: {}\n".format(sys.getsizeof(another_great_sentence)))
    #The size of the data is: 76
    print ("The content of the data is: {}\n".format(another_great_sentence))
    #The content of the data is: Hi my name is Ana Chisholm.
    encoded_data, tree = huffman_encoding(another_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #The size of the encoded data is: 40
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #The content of the encoded data is: 1100001000011110010010001001011110100001010100011011100010010011100101101010101011111011111001111111
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #The size of the decoded data is: 76
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: Hi my name is Ana Chisholm.

    a_final_great_sentence = "blabla''blablablablaaaaa"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_final_great_sentence)))
    #The size of the data is: 73
    print ("The content of the data is: {}\n".format(a_final_great_sentence))
    #The content of the data is: blabla''blablablablaaaaa
    encoded_data, tree = huffman_encoding(a_final_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    #The size of the encoded data is: 32
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #The content of the encoded data is: 1111001111001101101111001111001111001111000000
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #The size of the decoded data is: 73
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: blabla''blablablablaaaaa

    an_edge_case = 'aaaaaaaa'

    print ("The size of the data is: {}\n".format(sys.getsizeof(an_edge_case)))
    #The size of the data is: 57
    print ("The content of the data is: {}\n".format(an_edge_case))
    #The content of the data is: aaaaaaaa
    encoded_data, tree = huffman_encoding(an_edge_case)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
    #The size of the encoded data is: 49
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #The content of the encoded data is:
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #The size of the decoded data is: 57
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: aaaaaaaa

    another_edge_case = '.a'

    print ("The size of the data is: {}\n".format(sys.getsizeof(another_edge_case)))
    #The size of the data is: 51
    print ("The content of the data is: {}\n".format(another_edge_case))
    #The content of the data is: .a
    encoded_data, tree = huffman_encoding(another_edge_case)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
    #The size of the encoded data is: 51
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #The content of the encoded data is: 01
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    #The size of the decoded data is: 51
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The content of the encoded data is: .a
