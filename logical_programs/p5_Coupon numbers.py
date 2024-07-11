'''
@Author: Nagashree C R
@Date: 2024-07-10 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-10 
@Title : Find distinct coupon numbers using random function
'''
import random
def coupon(n):
  count=0
  existing=[]
  for i in range(1,100):
    coupon=random.randint(1,n)
    count+=1
    existing.append(coupon)
    set(existing)
    if len(existing)==n:
      print(f'no of cupon count{count},distinct coupon are {existing}')

coupon(10)
