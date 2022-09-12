class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return

        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2): #O(n)

    current_node_1 = llist_1.head
    union_elements = {}
    while current_node_1:
        if current_node_1.value not in union_elements:
            union_elements[current_node_1.value] = True
        current_node_1 = current_node_1.next

    current_node_2 = llist_2.head
    while current_node_2:
        if current_node_2.value not in union_elements:
            union_elements[current_node_2.value] = True
        current_node_2 = current_node_2.next

    union_list = LinkedList()
    for element in union_elements:
        union_list.append(element)

    return union_list

def intersection(llist_1, llist_2): #O(n)
    intersection_elements = {}
    llist_1_elements = {}

    current_node_1 = llist_1.head
    while current_node_1:
        if current_node_1.value not in llist_1_elements:
            llist_1_elements[current_node_1.value] = True
        current_node_1 = current_node_1.next

    current_node_2 = llist_2.head
    while current_node_2:
        if current_node_2.value in llist_1_elements and current_node_2.value not in intersection_elements:
            intersection_elements[current_node_2.value] = True
        current_node_2 = current_node_2.next

    intersection_list = LinkedList()
    for element in intersection_elements:
        intersection_list.append(element)

    return intersection_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

list_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
list_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
print(set(list_1).union(set(list_2)))
# set([32, 65, 2, 3, 4, 6, 1, 9, 11, 35, 21])
print(set(list_1).intersection(set(list_2)))
# set([4, 21, 6])

for i in list_1:
    linked_list_1.append(i)

for i in list_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
# 32 -> 65 -> 2 -> 35 -> 4 -> 6 -> 1 -> 9 -> 11 -> 3 -> 21 ->
print(intersection(linked_list_1, linked_list_2))
# 4 -> 21 -> 6 ->

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

list_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
list_2 = [1, 7, 8, 9, 11, 21, 1]
print(set(list_1).union(set(list_2)))
# set([65, 2, 3, 4, 6, 1, 8, 9, 7, 11, 35, 21, 23])
print(set(list_1).intersection(set(list_2)))
# set([])
for i in list_1:
    linked_list_3.append(i)

for i in list_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
# 65 -> 2 -> 35 -> 4 -> 6 -> 1 -> 8 -> 9 -> 7 -> 11 -> 3 -> 21 -> 23 ->
print(intersection(linked_list_3, linked_list_4))
# None

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

list_1 = []
list_2 = []
print(set(list_1).union(set(list_2)))
# set([])
print(set(list_1).intersection(set(list_2)))
# set([])
for i in list_1:
    linked_list_5.append(i)

for i in list_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
# None
print(intersection(linked_list_5, linked_list_6))
# None
