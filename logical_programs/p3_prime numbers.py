'''
@Author: Nagashree C R
@Date: 2024-07-11 
@Last Modified by: Author Name
@Last Modified: 2024-07-11 
@Title : Program Aim
'''

import math

def prime(n):
  if n==2:
    return f'{n} is a prime number'
  e=math.ceil(n**0.5)
  for i in range(2,e+1):
    if n%i==0:
      print("not a prime number")
      break
    else:
      print("is a prime number")
      break
    
    
n=int(input())
prime(n)