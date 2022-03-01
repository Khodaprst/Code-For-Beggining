z=dict()
x=int(input())
for i in range(x):
    y=input()
    l=y.split()
    z[l[0]]=l[1]
m=[]
b=input()
b=b.split()
for j in b:
    m.append(z.get(j,j))
print(' '.join(m))