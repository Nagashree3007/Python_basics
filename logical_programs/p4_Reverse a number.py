'''
@Author: Nagashree C R
@Date: 2024-07-10 
@Last Modified by: Author Name
@Last Modified: 2024-07-10 
@Title : reversing a number
'''
def reverseing(n):
  while n>1:
    r=n%10
    print(r,end='')
    n=n//10
    reverseing(n)
    return


n=int(input())
reverseing(n)
