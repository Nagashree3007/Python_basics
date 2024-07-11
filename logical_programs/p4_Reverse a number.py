def reverseing(n):
  while n>1:
    r=n%10
    print(r,end='')
    n=n//10
    reverseing(n)
    return
n=int(input())
reverseing(n)