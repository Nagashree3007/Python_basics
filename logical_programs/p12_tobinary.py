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

    binary_representation = []
    
    # Determine the maximum power of 2 we need
    max_power = 31  # 4 bytes -> 32 bits, counting from 0 to 31 (2^0 to 2^31)

    # Find the highest power of 2 that fits into the decimal_number
    while 2 ** max_power > decimal_number:
        max_power -= 1

    # Construct the binary representation
    for power in range(max_power, -1, -1):
        if decimal_number >= 2 ** power:
            binary_representation.append('1')
            decimal_number -= 2 ** power
        else:
            binary_representation.append('0')

    # Join the list into a string
    binary_string = ''.join(binary_representation)

    # Ensure the string is 32 characters long (4 bytes)
    binary_string = binary_string.zfill(32)

    return binary_string


decimal_number = 106
binary_representation = toBinary(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_representation}")
