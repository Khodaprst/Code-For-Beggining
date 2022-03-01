n=int(input('please enter number:'))
b=[]
f=0
for i in range(2,n+1):
 for j in range(2,i):
  if i%j==0:
   f=1
   
 if f==0:
  b.append(i)
 f=0

print(b)