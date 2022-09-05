def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Sort elements
    input_list = merge_sort(input_list)
    if len(input_list) % 2 == 0:
        number_1_length = int(len(input_list) / 2)
        number_2_length = int(len(input_list) / 2)
    else:
        number_1_length = len(input_list) // 2 + 1
        number_2_length = len(input_list) - number_1_length


    index = len(input_list) - 1
    number_1 = 0
    number_2 = 0
    while index >= 0:
        number_1 += pow(10, number_1_length - 1) * input_list[index]
        index -= 1
        number_1_length -= 1

        if index >= 0:
            number_2 += pow(10, number_2_length - 1) * input_list[index]
            index -= 1
            number_2_length -= 1

    print(number_1, number_2)
    return number_1, number_2


def merge_sort(array):
    if len(array) <= 1:
        return array

    midpoint = len(array) // 2
    left = array[:midpoint]
    right = array[midpoint:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':

    test_function([[4, 5, 3, 1, 2], [542, 31]])
    test_function([[5, 2, 1, 4], [52, 41]])
    test_function([[8, 1, 9, 4, 3, 2], [942, 831]])
    test_function([[3, 7, 8, 9, 1, 2], [972, 831]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
