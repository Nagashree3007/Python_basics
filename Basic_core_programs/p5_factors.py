'''
@Author: Nagashree C R
@Date: 2024-07-11
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11
@Title : the prime factorization of N using brute force.
'''

def prime_fact(n):
  fact=[]
  divisor=2
  while n>1:   
    while n % divisor==0:
      fact.append(divisor)
      n//=divisor
    divisor+=1
  return fact
n=int(input())
result=set(prime_fact(n))
print(f"prime factors of {n} is")
for i in result:
  print(i,end=' ')