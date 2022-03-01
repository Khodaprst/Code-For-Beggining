c=dict()
x=int(input())
for i in range(x):
 y=input()
 l=y.split()
 c[l[0]]=l[1]
m=[]
t=input()
t=t.split()
for j in t:
 m.append(c.get(j,j))
print(' '.join(m))