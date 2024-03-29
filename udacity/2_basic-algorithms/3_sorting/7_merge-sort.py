def mergesort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    # Otherwise, find the midpoint and split the list
    midpoint = len(items) // 2
    left = items[:midpoint]
    right = items[midpoint:]

    # Call mergesort recursively with the left and right half
    left = mergesort(left)
    right = mergesort(right)

    # Merge our two halves and return
    return merge(left, right)


def merge(left, right):
    # Given two ordered lists, merge them together in order,
    # returning the merged list.
    merged = []
    left_index = 0
    right_index = 0

    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        # If left's item is larger, append right's item and increment the index
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        # Otherwise, append left's item and increment
        else:
            merged.append(left[left_index])
            left_index += 1

    # Append any leftovers. Because we've broken from the while loop.
    # We know at least one is empty, and the remaining:
    # - are already sorted
    # - all sort past our last element in merged
    merged += left[left_index:]
    merged += right[right_index:]

    # return the ordered, merged list
    return merged


if __name__ == '__main__':
    # Test this out
    merged = merge([1, 3, 7], [2, 5, 6])
    print(merged)

    test_list_1 = [8, 3, 1, 7, 0, 10, 2]
    test_list_2 = [1, 0]
    test_list_3 = [97, 98, 99]
    print('{} to {}'.format(test_list_1, mergesort(test_list_1)))
    print('{} to {}'.format(test_list_2, mergesort(test_list_2)))
    print('{} to {}'.format(test_list_3, mergesort(test_list_3)))