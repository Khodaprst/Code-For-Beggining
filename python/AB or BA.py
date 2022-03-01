c = input()
c = c.upper()
tool = len(c)
count = 0
dount = 0
for a in c:
    if a == 'A':
        count = count + 1

for b in c:
    if b == 'B':
        dount = dount + 1
for jomle in c:
    if jomle == 'C':
        print('NO')    
if count == dount:
    print('YES')
else:
    print('NO')