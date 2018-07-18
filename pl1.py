m=int(input())
r=0
while(m>0):
     n=m%10
     r=r*10+n
     m=m//10
print(r)
