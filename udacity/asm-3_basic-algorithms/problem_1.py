def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number in [0, 1]:
        return number

    min = 1
    max = number
    result = None
    while min < max:
        half = (min + max) // 2
        square = half * half
        if square == number:
            return half
        elif square < number:
            min += 1
            result = half
        else:
            max -= 1

    return result


if __name__ == '__main__':
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (1 == sqrt(2)) else "Fail")
    print("Pass" if (1 == sqrt(3)) else "Fail")
    print("Pass" if (2 == sqrt(8)) else "Fail")
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")
