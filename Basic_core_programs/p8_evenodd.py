'''
@Author: Nagashree C R
@Date: 2024-07-11
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11
@Title : find given number is odd or even
'''


def finding(num):
  if num % 2==0:
    print(f"{num} is even number")
  else:
    print(f"{num} is odd number")
    
num=int(input())
finding(num)