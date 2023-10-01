'''
Binary, decimal, octal, and hexadecimal are different numeral systems used to represent numbers. Each system has a base that determines the number of unique digits it uses. Here's a brief explanation of each:

Binary (Base-2):
Base: 2
Digits: 0, 1
Example: Binary representation of 13 is 1101 (1 * 2^3 + 1 * 2^2 + 0 * 2^1 + 1 * 2^0).

Decimal (Base-10):
Base: 10
Digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
Example: Decimal representation of 13 is 13 (1 * 10^1 + 3 * 10^0).

Octal (Base-8):
Base: 8
Digits: 0, 1, 2, 3, 4, 5, 6, 7
Example: Octal representation of 13 is 15 (1 * 8^1 + 5 * 8^0).

Hexadecimal (Base-16):
Base: 16
Digits: 0-9, A (10), B (11), C (12), D (13), E (14), F (15)
Example: Hexadecimal representation of 13 is D (13 in decimal).
These numeral systems are used in computing for various purposes:

Binary: Fundamental in computer science and digital electronics, where information is represented using bits (0s and 1s).
Decimal: Commonly used in everyday life. It is the standard numeral system for denoting integer and non-integer numbers.
Octal: Less common but used in some programming contexts. For example, Unix file permissions are often represented in octal.
Hexadecimal: Widely used in computing, especially in programming and digital electronics. It's more compact than binary and is often used to represent memory addresses and color values.
Converting between these bases involves understanding the place value system for each. For instance, in binary, each position represents a power of 2; in octal, a power of 8; and in hexadecimal, a power of 16. Decimal, being the most familiar base, uses powers of 10. Conversion is done by considering the place values of digits in each system.
'''

def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

def decimal_to_octal(decimal):
    octal = ""
    while decimal > 0:
        remainder = decimal % 8
        octal = str(remainder) + octal
        decimal //= 8
    return octal

def decimal_to_hexadecimal(decimal):
    hexadecimal = ""
    hex_digits = "0123456789ABCDEF"
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        decimal //= 16
    return hexadecimal

# List of binary numbers
binary_list = ['1010', '1101', '1111', '1001']

# Convert binary to decimal, octal, and hexadecimal without using built-in functions
decimal_list = [binary_to_decimal(binary) for binary in binary_list]
octal_list = [decimal_to_octal(decimal) for decimal in decimal_list]
hex_list = [decimal_to_hexadecimal(decimal) for decimal in decimal_list]

# Display the results
print("Binary List:", binary_list)
print("Decimal List:", decimal_list)
print("Octal List:", octal_list)
print("Hexadecimal List:", hex_list)
