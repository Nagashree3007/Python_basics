'''
@Author: Nagashree C R
@Date: 2024-07-10 
@Last Modified by: Nagashree C R 
@Last Modified: 2024-07-10 
@Title : program to impliment stopwatch functionality
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
