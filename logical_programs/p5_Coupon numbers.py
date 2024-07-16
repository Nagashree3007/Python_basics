'''
@Author: Nagashree C R
@Date: 2024-07-10 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-10 
@Title : Find distinct coupon numbers using random function

'''
import random

def coupon(n):
  lucky_number=[]
  for i in range(0,n):
    number=random.randint(1111,5555)
    lucky_number.append(number)
  check=int(input("Enter your coupon number"))
  x=','.join(str(i) for i in lucky_number)
  print(f'the lucky coupon numbers are  {x}')
  print(f'your coupon number {check}')
  if check in lucky_number:
    print("congratulations you won the lucky coupon")
  else:
    print("opps!!!..you lost,better luck next time")

numberofcoupons=int(input("enter the number of coupons to be generated"))

coupon(numberofcoupons)
