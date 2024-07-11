'''
@Author: Nagashree C R
@Date: 2024-07-11 
@Last Modified by: Author Name
@Last Modified: 2024-07-11 
@Title : Program Aim
'''


import time

s=input("start/stop ")

if s =='Start':
  start_time=time.time()
#print(start_time)

e=input("start/stop ")
if e=="stop":
  end_time=time.time()
#print(end_time)


print(f'elapse time is {(end_time-start_time)*10**6:.6f}sec')
#s=str(round((end_time-start_time)*10**6))
#print(f'elapse time is {s[:2]} sec')
