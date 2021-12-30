import logging

class Node():

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class Queue():

    def __init__(self):
        #head will be used as the LRU pointer
        self.head = None
        #tail will be used as the MRU pointer
        self.tail = None
        self.num_elements = 0
    #enqueue MRU item on the tail
    def enqueue(self, node):
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = self.tail.next
        self.num_elements += 1
    #dequeue LRU item from the head.
    def dequeue(self):
        if self.is_empty():
            return None
        key = self.head.key
        self.head = self.head.next
        self.head.previous = None
        self.num_elements -= 1
        return key

    def remove(self, node):
        assert not self.is_empty(), 'Queue is empty, nothing to remove.'

        if self.head == node:
            self.head = self.head.next
            self.head.previous = None
            self.num_elements -= 1

        elif self.tail == node:
            #this case wont ever be used in the LRU cache implementation, but for including for completeness of the queue object.
            self.tail = self.tail.previous
            self.tail.next = None
            self.num_elements -= 1

        else:
            previous_node = node.previous
            next_node = node.next
            previous_node.next = next_node
            next_node.previous = previous_node
            node.next = None
            node.previous = None
            self.num_elements -= 1

    def is_empty(self):
        return self.num_elements == 0


class LRU_Cache(object):

    def __init__(self, capacity):
        #dictionary of key:node pairs.
        self.cache = dict()
        self.size = 0
        self.capacity = capacity
        self.usage_tracker = Queue()


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            #bring to the front of the queue.
            node = self.cache[key]

            if self.usage_tracker.tail == node:
                return self.cache[key].value

            self.usage_tracker.remove(node)
            self.usage_tracker.enqueue(node)

            return self.cache[key].value

        return int('-1')

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key not in self.cache:
            if self.size == self.capacity:
                logging.info('Cache at capacity, removing the least recently used node')
                lru_key = self.usage_tracker.dequeue()
                self.cache.pop(lru_key)
                self.size -= 1

            new_node = Node(key, value)
            self.cache[key] = new_node
            self.usage_tracker.enqueue(new_node)
            self.size += 1

    def __repr__(self):
        printed_str=''
        for key, node in self.cache.items():
            printed_str += '{}:[key:{}, value:{}], '.format(key, node.key, node.value)
        return '{'+printed_str+'}'


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
print(our_cache)

print(our_cache.get(1))
# returns 1

print(our_cache.get(2))
# returns 2

print(our_cache.get(9))
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache)

print(our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
our_cache.set(7, 7)
print(our_cache)

print(our_cache.get(4))
# returns -1 because the cache reached it's capacity and 4 was the least recently used entry

our_cache.set(9, 5)
#doesnt set 9 because key 9 is already in the cache.
print(our_cache)

print(our_cache.get(100))
#returns -1 because the cache does not contain the key 100.
