def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min = None
    max = None
    for value in ints:
        if min is None:
            min = value
        if max is None:
            max = value
            
        if value < min:
            min = value
        if value > max:
            max = value
    return (min, max)


## Example Test Case of Ten Integers
import random

if __name__ == '__main__':
    print('\n---------- Test 1 -----------')
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

    print('\n---------- Test 2 -----------')
    l = []  # a list containing 0 - 9
    random.shuffle(l)
    print("Pass" if ((None, None) == get_min_max(l)) else "Fail")

    print('\n---------- Test 3 -----------')
    l = [3, 3]  # a list containing 0 - 9
    random.shuffle(l)
    print("Pass" if ((3, 3) == get_min_max(l)) else "Fail")