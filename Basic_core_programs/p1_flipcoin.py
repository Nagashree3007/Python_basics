'''
@Author: Nagashree C R
@Date: 2024-07-11
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11
@Title : find the peercentage of head and tail after fliping a coin n number of time.
'''

import random
import math
n=int(input())
head=0
tail=0
def count_val(n):
  head=0
  tail=0
  for val in range(n):
    random_number = random.random()
    print(f'random number between 1 and 0 is {random_number}')
    if(random_number<0.5):
      tail+=1
      print(f" no of tail {tail}")
    else:
      head+=1
      print(f"no of head {head}")
  print(f'tatal number of heads abd tails {head},{tail}')
  sum=head+tail
  #sum
  print(sum)
  #calculating percentage
  tail_percentage=(tail/sum)*100
  head_percentage=(head/sum)*100
  print(f"percentage of Head is{head_percentage} and Tail is {tail_percentage}")
count_val(n)