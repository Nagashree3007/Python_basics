'''
@Author: Nagashree C R
@Date: 2024-07-11
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11
@Title : find harmonic sum of  number in range(1,N)
'''

def harmonic(n):
  sum=0
  for i in range(1,n+1):
    sum+=(1/i)
    print(sum)
  return sum

n=int(input())

if n>0:
  print(f'harmonic sum of numbers is {harmonic(n)}')
else:
  print("N must be greater than zero")