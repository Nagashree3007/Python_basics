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

