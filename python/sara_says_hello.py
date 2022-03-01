inpt=input()
h1=inpt.find('h')
h2=inpt.find('e',h1+1)
h3=inpt.find('l',h2+1)
h4=inpt.find('l',h3+1)
h5=inpt.find('o',h4+1)
TF=h1>=0 and h2>h1 and h3>h2 and h4>h3 and h5>h4
if TF:
 print('YES')
else:
 print('NO')