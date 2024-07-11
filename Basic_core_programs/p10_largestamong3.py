'''
@Author: Nagashree C R
@Date: 2024-07-11
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11
@Title : find the largest ammong three given numbers
'''

def largest(f,s,t):
  if f>s and f>t:
    print(f'{f} is largest')
  elif f<s and s>t:
    print(f'{s} is largest')
  else:
    print(f'{t} is largest')
    
    
largest(10,50,60)