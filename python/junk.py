string = 'salam amir is here and testing python for fun'

counter = dict()

for letter in string:

    if letter in counter:
        counter[letter] += 1
    else:
        counter[letter] = 1

for this in list(counter.keys()):
    print('%s appeared %s times' %(this, counter[this]))