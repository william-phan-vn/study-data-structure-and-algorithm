

class MinHeap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]
        self.next_index = 0     # denotes next index where new element should go

    def size(self):
        return self.next_index

    def is_empty(self):
        return self.size() == 0

    def get_minimum(self):
        return None if self.size() == 0 else self.cbt[0]

    def insert(self, data):
        # insert element at the next index
        self.cbt[self.next_index] = data

        # heapify
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

        # double the array and copy elements if nex_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def remove(self):
        """
        Returns: the element at the top of the heap

        """
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # place last element of the cbt at the root
        self.cbt[0] = last_element

        # we do not remove the elements,
        # rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = to_remove
        self._down_heapify()

        return to_remove

    def _up_heapify(self):
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            min_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                min_element = min(parent, left_child)

            # compare with right child
            if right_child is not None:
                min_element = min(min_element, right_child)

            # check if parent is rightly placed
            if min_element == parent:
                return

            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent_index = left_child_index

            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent_index = right_child_index


if __name__ == '__main__':
    heap_size = 5
    min_heap = MinHeap(heap_size)

    elements = [1, 2, 3, 4, 1, 2]

    for element in elements:
        min_heap.insert(element)

    print(f'Inserted elements: {min_heap.cbt}')
    print(f'Size of heap: {min_heap.size()}')

    for _ in range(4):
        print(f'Call remove: {min_heap.remove()}')

    print(f'Call get_minimum: {min_heap.get_minimum()}')

    for _ in range(2):
        print(f'Call remove: {min_heap.remove()}')

    print(f'Size of heap: {min_heap.size()}')
    print(f'Call remove: {min_heap.remove()}')
    print(f'Call is_empty: {min_heap.is_empty()}')
