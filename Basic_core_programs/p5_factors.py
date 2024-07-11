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