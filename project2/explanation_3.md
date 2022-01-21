#Explanation of Approach
I knew I wanted to create nodes that could be both in the sorted queue and in the tree at once.

#Time complexity
get_frequency_of_chars O(n)
building the sorted queue O(n^2) - iterating through the dict, insert func in class can potentially iterate through mostly all the nodes before inserting into the list.
traversing the tree for encoding O(n) because we touch every node.
#Space complexity
The space complexity of the solution is O(2n-1) or just O(n). This is because we are creating a linked list that contains 2n-1 nodes where n is the number of characters in the input string.
