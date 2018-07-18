a=int(input())
c=0
for k in range(2,a):
   if(a%k==0):
     c=c+1
if(c==0):
  print("yes")
else:
     print("no")
