def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for value in input_list:
        if value == 0:
            count_0 += 1
        elif value == 1:
            count_1 += 1
        elif value == 2:
            count_2 += 1
        else:
            return None

    return [0] * count_0 + [1] * count_1 + [2] * count_2


def test_function(test_case):
    if type(test_case) is not list:
        print('Error! Please input a list of 0,1,2 values.\n')
        return

    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass\n")
    else:
        print("Fail\n")


if __name__ == '__main__':
    # test_function([])
    test_function(None)
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
