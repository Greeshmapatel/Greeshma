a=int(input())
r=0
x=a
while(a>0):
  n=a%10
  r=r*10+n
  a=a//10
if(x==r):
  print("yes")
else:
  print("no")
