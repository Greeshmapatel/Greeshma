a=int(input())
r=0
x=a
while(a>0):
     n=a%10
     r=r+n**3
     a=a//10
if(x==r):
  print("yes")
else:
     print("no")

    
