#Explanation of Approach
The blockchain is just a linked list with extra attributes and hashing. I implemented a basic singly linked list, with previous pointers connecting each node or block. Each block contains data, a timestamp of creation, and a hash. This hash is a sha 256 hash of the timestamp and data strings concatenated together. This way the hash has a good guarantee of being unique, since you cant create two blocks at the same exact time.

#Time complexity
The time complexity of creating a blockchain using my class is O(1). We just need to consider the calculation time of the hash value and the addition of values to a linked list which both take constant time. The to_list method of my blockchain class is O(n) however, since we loop through and access each of the blocks.

#Space complexity
The space complexity is O(n)?
