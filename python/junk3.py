tedad = int(input())

l2=[]

e2p = dict()

for english in range(tedad):
    english,persion = input ('').split(' ')
    e2p[english] = persion

text_enghlishi = input('')
l1 = text_enghlishi.split(' ')


for i in l1:
    loghat=(e2p[i])
    l2.append(loghat)

text_farsi=' '.join(l2)

print(text_farsi)