import hashlib
from time import gmtime


class Block:

    def __init__(self, data=''):
      self.timestamp = gmtime()
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
        if self.tail is None:
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
    # 4
    print(my_blockchain.to_list())
    # time values will be variable:
    # [time.struct_time(tm_year=2022, tm_mon=9, tm_mday=12, tm_hour=15, tm_min=29, tm_sec=8, tm_wday=0, tm_yday=255, tm_isdst=0), time.struct_time(tm_year=2022, tm_mon=9, tm_mday=12, tm_hour=15, tm_min=29, tm_sec=8, tm_wday=0, tm_yday=255, tm_isdst=0), time.struct_time(tm_year=2022, tm_mon=9, tm_mday=12, tm_hour=15, tm_min=29, tm_sec=8, tm_wday=0, tm_yday=255, tm_isdst=0), time.struct_time(tm_year=2022, tm_mon=9, tm_mday=12, tm_hour=15, tm_min=29, tm_sec=8, tm_wday=0, tm_yday=255, tm_isdst=0)]


    my_blockchain_2 = Blockchain()
    my_blockchain_2.append(Block('1'))
    my_blockchain_2.append(Block('2'))

    print(my_blockchain_2.get_size())
    # 2
    print(my_blockchain_2.to_list())
    # time values will be variable:
    # [time.struct_time(tm_year=2022, tm_mon=9, tm_mday=12, tm_hour=15, tm_min=32, tm_sec=10, tm_wday=0, tm_yday=255, tm_isdst=0), time.struct_time(tm_year=2022, tm_mon=9, tm_mday=12, tm_hour=15, tm_min=32, tm_sec=10, tm_wday=0, tm_yday=255, tm_isdst=0)]

    my_blockchain_3 = Blockchain()
    my_blockchain_3.append(Block())

    print(my_blockchain_3.get_size())
    # 1
    print(my_blockchain_3.to_list())
    # time values will be variable:
    # [time.struct_time(tm_year=2022, tm_mon=9, tm_mday=12, tm_hour=15, tm_min=34, tm_sec=27, tm_wday=0, tm_yday=255, tm_isdst=0)]

    my_blockchain_4 = Blockchain()
    my_blockchain_4.append(Block(1))

    print(my_blockchain_4.get_size())
    # 1
    print(my_blockchain_4.to_list())
    # time values will be variable:
    # [time.struct_time(tm_year=2022, tm_mon=9, tm_mday=12, tm_hour=15, tm_min=35, tm_sec=40, tm_wday=0, tm_yday=255, tm_isdst=0)]
