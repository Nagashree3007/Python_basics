'''
@Author: Nagashree C R
@Date: 2024-07-11 
@Last Modified by: Author Name
@Last Modified: 2024-07-10 
@Title : Find the perfect number
'''

def perfect(n):
  sum_n=0
  for i in range(1,n+1):
    if i % n==0:
      sum_n +=i
    if sum_n==n:
      print("perfect number")
    elif sum_n>n:
      print("not perfect number")
n=int(input())
perfect(n)

