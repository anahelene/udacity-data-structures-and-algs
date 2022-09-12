#Explanation of Approach
The union of two linked lists combines all elements into one linked list, without repeated elements. First, the solution iterates through each linked list, and each element is added as a key to a dictionary if that element is not already in the dictionary. Aggregating elements in a dictionary allows for efficient O(1) checks before the element is added to the dictionary. Finally, the dictionary is converted to a linked list then returned.

The intersection of two linked lists combines all shared elements into one linked list, without repeated elements. The first linked list is converted to a dictionary to later allow for efficient comparisons. The second linked list is iterated through and each element is added to the intersection dictionary if the element is both present in the first linked list and the element is not already in the intersection dictionary. The intersection dictionary is converted to a linked list then returned.

#Time complexity
The time complexity of my solution is O(n). The intersection and union methods both iterate through each inputted linked list (O(n) time), perform some dictionary lookup (O(1) time), then append to a new linked list (O(1) time). The worst time complexity is therefore O(n).

#Space complexity
The space complexity of the solution is O(n), where n is the number of elements in the union or intersection. The union and intersection are stored temporarily as dictionaries, then are converted to new linked lists. This is a space complexity of O(2n), which reduces to O(n).
