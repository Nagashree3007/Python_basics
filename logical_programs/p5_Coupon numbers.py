'''
@Author: Nagashree C R
@Date: 2024-07-11 
@Last Modified by: Author Name
@Last Modified: 2024-07-11 
@Title : Program Aim
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