'''
@Author: Nagashree C R
@Date: 2024-07-10 
@Last Modified by: Author Name
@Last Modified: 2024-07-10 
@Title : Find the fibonnaci of a number
'''

def fibonnacci(n):
  a=0
  b=1
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    for i in range(n):
      print(a,end=',')
      a,b=b,a+b
fibonnacci(5)

