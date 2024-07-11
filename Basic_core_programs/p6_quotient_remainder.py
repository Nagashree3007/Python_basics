'''
@Author: Nagashree C R
@Date: 2024-07-11
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11
@Title : find quotient and remainder for given number.
'''

def calculate_quotient_remainder(dividend, divisor):
  dividend=int(dividend)
  divisor=int(divisor)
  quotient = dividend // divisor
  remainder = dividend % divisor
  return quotient, remainder


dividend, divisor=input().split(',')
calculate_quotient_remainder(dividend, divisor)