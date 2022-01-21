import hashlib
import time
from time import gmtime

class Block:

    def __init__(self, data):
      self.timestamp = time.gmtime()
      self.data = data
      self.previous_hash = None
      self.hash = self.calc_hash()
      self.previous = None

    def calc_hash(self):
      sha = hashlib.sha256()
      hash_str = str(self.timestamp) + str(self.data)
      hash_str = hash_str.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

    def get_hash(self):
        return self.hash

class Blockchain:

    def __init__(self):
        self.tail = None
        self.size = 0

    def append(self, block):
        if self.tail == None:
            self.tail = block
        else:
            block.previous_hash = self.tail.get_hash()
            block.previous = self.tail
            self.tail = block

        self.size += 1

    def get_size(self):
        return self.size

    def to_list(self):
        out_list = []
        block = self.tail
        while block:
            out_list.append(block.timestamp)
            block = block.previous
        return out_list

if __name__ == "__main__":

    my_blockchain = Blockchain()
    my_blockchain.append(Block('$100'))
    my_blockchain.append(Block('$101'))
    my_blockchain.append(Block('$102'))
    my_blockchain.append(Block('$103'))


    print(my_blockchain.get_size())
    print(my_blockchain.to_list())
