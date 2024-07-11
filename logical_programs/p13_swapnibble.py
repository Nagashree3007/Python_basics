'''
@Author: Nagashree C R
@Date: 2024-07-11 
@Last Modified by: Author Name
@Last Modified: 2024-07-11 
@Title : Program Aim
'''


def toBinary(decimal_number):
    if decimal_number == 0:
        return '00000000'

    binary_representation = format(decimal_number, '08b')
    return binary_representation



def swapNibbles(decimal_number):
    binary_string = toBinary(decimal_number)
    binary_string = binary_string.zfill(8)
    swapped_binary = binary_string[4:] + binary_string[:4]
    swapped_decimal = int(swapped_binary, 2)
    
    return swapped_decimal


def isPowerOfTwo(number):
    return (number != 0) and ((number & (number - 1)) == 0)

# Main program

if __name__ == "__main__":
    decimal_number = int(input("Enter a decimal number: "))
    binary_representation = toBinary(decimal_number)
    print(f"Binary representation of {decimal_number} is: {binary_representation}")
    swapped_number = swapNibbles(decimal_number)
    print(f"After swapping nibbles, the resultant number is: {swapped_number}")
    if isPowerOfTwo(swapped_number):
        print("The resultant number is a power of 2.")
    else:
        print("The resultant number is not a power of 2.")