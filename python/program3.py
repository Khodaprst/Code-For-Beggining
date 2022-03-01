string = 'salam. amir is here'
counter = dict()
for letter in string:

    if letter in counter:
        counter[letter] += 1
    else:
        counter[letter] = 1

for this in list(counter.keys()):
    print('%s appered %s times' %(this, counter[this]))