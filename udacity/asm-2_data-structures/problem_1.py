from typing import Dict


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node = None
        self.previous: Node = None


class LruCache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.head: Node = None
        self.tail: Node = None
        self.cache: Dict[any, Node] = {}
        self.capacity: int = capacity
        self.size = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        node = self.cache.get(key)
        if node is None:
            return -1

        # ------- Re-order the cache ------
        previous_node = node.previous
        next_node = node.next

        # Link the previous node to the next node
        if next_node is None:
            return node.value

        if previous_node is None:
            self.head = next_node
            self.head.previous = None

            self.cache[self.head.value] = self.head
        else:
            previous_node.next = next_node
            next_node.previous = previous_node

            self.cache[previous_node.value] = previous_node
            self.cache[next_node.value] = next_node

        # Move the current node to the tail
        node.previous = self.tail
        node.next = None
        self.tail.next = node
        self.cache[self.tail.value] = self.tail

        self.tail = self.tail.next
        self.cache[key] = self.tail

        return node.value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.cache.get(key) is None:
            # Add new node to the head and tail
            if self.head is None:
                self.head = Node(value)
                self.tail = Node(value)
                self.head.next = self.tail
                self.tail.previous = self.head

                self.cache.update({key: self.head})

            else:
                # Add new node to the tail
                new_node = Node(value)
                if self.head.value == self.tail.value:
                    new_node.previous = self.head
                    self.head.next = new_node
                    self.tail = new_node
                    self.cache[self.head.value] = self.head
                    self.cache[self.tail.value] = self.tail
                else:
                    new_node.previous = self.tail
                    self.tail.next = new_node
                    self.cache[self.tail.value] = self.tail

                    self.tail = self.tail.next
                    self.cache.update({key: self.tail})
            self.size += 1

            if self.size > self.capacity:
                self.cache.pop(self.head.value)
                self.head = self.head.next
                self.head.previous = None
                self.size -= 1
        else:
            print(f'Caching failed. The key {key} already exists in the cache.')


if __name__ == '__main__':
    our_cache = LruCache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))  # returns 1
    print(our_cache.get(2))  # returns 2
    print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    # Add your own test cases: include at least three test cases
    # and two of them must include edge cases, such as null, empty or very large values

    # Test Case 1
    our_cache.set(7, '')
    print('\n1. Empty value ', our_cache.get(7))
    # Expected result: 1. Empty value

    # Test Case 2
    our_cache.set(8, None)
    print('\n2. None value: ', our_cache.get(8))
    # Expected result: 2. None value:  None

    # Test Case 3
    our_cache.set(9, pow(9, 100))
    print('\n3. Large value: ', our_cache.get(9), '\n')
    # Expected result: 3. Large value:  265613988875874769338781322035779626829233452653394495974574961739092490901302182994384699044001

    # Test Case 4: key already exist
    our_cache.set(9, 9)
    print('Current value at key = 9: ', our_cache.get(9))
    # Expected result:
        # Caching failed. The key 9 already exists in the cache.
        # Current value at key = 9:  265613988875874769338781322035779626829233452653394495974574961739092490901302182994384699044001
