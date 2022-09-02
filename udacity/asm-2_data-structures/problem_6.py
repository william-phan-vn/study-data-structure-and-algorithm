from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head: Node = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def find_union(llist: LinkedList, union_dict: dict, union_llist: LinkedList):
    node: Node = llist.head
    while type(node) == Node:
        if union_dict.get(node.value) is None:
            union_dict[node.value] = 1
            union_llist.append(Node(node.value))
        node = node.next


def union(llist_1: LinkedList, llist_2: LinkedList):
    union_dict = {}
    union_llist = LinkedList()

    find_union(llist_1, union_dict, union_llist)
    find_union(llist_2, union_dict, union_llist)

    return union_llist


def intersection(llist_1, llist_2):
    union_dict = {}
    intersection_llist = LinkedList()

    node: Node = llist_1.head
    while type(node) == Node:
        union_dict[node.value] = 1
        node = node.next

    node: Node = llist_2.head
    while type(node) == Node:
        if union_dict.get(node.value) is not None:
            temp = node.next
            node.next = None
            intersection_llist.append(node)
            node = temp
        else:
            node = node.next

    return intersection_llist


if __name__ == '__main__':

    # Test case 1
    print(f'---------- Test 1 ----------- ')

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print('Union: ', union(linked_list_1, linked_list_2))
    print('Intersection: ', intersection(linked_list_1, linked_list_2))

    # Test case 2
    print(f'---------- Test 2 ----------- ')

    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print('Union: ', union(linked_list_3, linked_list_4))
    print('Intersection: ', intersection(linked_list_3, linked_list_4))

    # Test Case 3
    print(f'---------- Test 3 ----------- ')
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print('Union: ', union(linked_list_1, linked_list_2))
    print('Intersection: ', intersection(linked_list_1, linked_list_2))

    # Test Case 4
    print(f'---------- Test 4 ----------- ')
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = []
    element_2 = [5]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print('Union: ', union(linked_list_1, linked_list_2))
    print('Intersection: ', intersection(linked_list_1, linked_list_2))
