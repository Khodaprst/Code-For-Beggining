def bozorgtarin(a,b,c):
       bozorg = a if a > b else b
       bozorg = c if c > b else b
       return(bozorg)

aval = int(input())
dovom = int(input())
sevom = int(input())
max = bozorgtarin(aval, dovom, sevom)
print(max)