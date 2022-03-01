string = 'hey, amir is here to learn python for job'

counter = dict()

for letter in string:
    print(letter)
    if letter in counter:
        counter[letter] += 1
    else:
        counter[letter] = 1

for this_one in (counter.keys()):
    print('%s appeared %s times' % (this_one, counter[this_one]))