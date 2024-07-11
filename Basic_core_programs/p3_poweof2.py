'''
@Author: Nagashree C R
@Date: 2024-07-11
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11
@Title : print 2 power of N,N is taken as input
'''

def power(n):
  for i in range(1,n+1):
    print(f'2^{i}={2**i}')
    
    
n=int(input())
if n<31:
  power(n)
else:
  print("enter value under 31...it is causing owerflow")