n = int(input())
x = []
count = 0
pazir = 0
while count != n:
       z = int(input())
       count = count + 1
       if z % 2 == 0:
              x.append(z)
              pazir = pazir + 1
if pazir == 1:
       print(pazir,'adad bakhsh pazir bud va un adad',x ,'hast')
else:
       print(pazir,'adad bakhsh pazir budan va adad ha shamele',x ,'hastand')
print('SnoopDog!!!')