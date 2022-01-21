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

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]
print(set(element_1).union(set(element_2)))
print(set(element_1).intersection(set(element_2)))

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1,linked_list_2))
print(intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]
print(set(element_1).union(set(element_2)))
print(set(element_1).intersection(set(element_2)))

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
