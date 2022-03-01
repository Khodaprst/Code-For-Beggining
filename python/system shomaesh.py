x=int(input())
counter=dict()
for i in range(x):
    y=input()
    counter[y]=counter.get(y,0)+1
x1=list(counter.keys())
x1.sort()
for j in x1:
    print(j,counter[j])