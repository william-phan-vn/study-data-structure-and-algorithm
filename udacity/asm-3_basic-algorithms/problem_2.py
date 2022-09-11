def rotated_array_search(array, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    pivot_index = find_pivot_point(input_list=array, index_test=0)
    if pivot_index == None:
        pivot_index = len(array) - 1
    result = binary_search(input_list=array[:pivot_index], target=target)
    if result == -1:
        result = binary_search(input_list=array[pivot_index:], target=target)
        if result != -1:
            result = result + pivot_index
    return result


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def binary_search(input_list, target, start=0, end=None):
    if end is None:
        end = len(input_list) - 1
    if start > end:
        return -1

    center_index = start + (end - start) // 2
    value = input_list[center_index]
    if value == target:
        return center_index
    elif value > target:
        return binary_search(input_list, target, start, center_index - 1)
    else:
        return binary_search(input_list, target, center_index + 1, end)


def find_pivot_point(input_list, index_test):
    if len(input_list) == 1:
        return index_test
    if len(input_list) == 2:
        if input_list[1] < input_list[0]:
            return index_test + 1
        else:
            return None

    mid_index = len(input_list) // 2

    # assume there are no duplicates in the array
    if input_list[mid_index] > input_list[mid_index - 1] and input_list[mid_index] > input_list[mid_index + 1]:
        return index_test + mid_index + 1
    elif input_list[mid_index] < input_list[mid_index - 1] and input_list[mid_index] < input_list[mid_index + 1]:
        return index_test + mid_index
    elif input_list[mid_index] > input_list[mid_index - 1]:
        index_test += mid_index
        find_pivot_point(input_list[mid_index + 1:], index_test)
    else:   # array[mid_index] < array[mid_index - 1]:
        index_test -= mid_index
        find_pivot_point(input_list[:mid_index], index_test)


def test_function(test_case):
    input_list = test_case[0]
    if type(input_list) is not list:
        print('Error! Please input a list of integers.')
        return
    if len(input_list) == 0:
        print('The list must contain at least one element.')
        return
    number = test_case[1]

    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_function([[], 0])
    test_function([None, 0])
    test_function([[2, 1], 0])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
