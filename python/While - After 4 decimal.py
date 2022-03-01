x = []
count = 0
pazir = 0
while count != 10:
       z = int(input())
       count = count + 1
       if z % 4 == 0:
              x.append(z)
              pazir = pazir + 1
if pazir == 1:
       print(pazir,'adad bakhsh pazir bud va un adad',x ,'hast')
else:
       print(pazir,'adad bakhsh pazir budan va aedad shamel',x ,'hastand')
print('SnoopDog!!!')