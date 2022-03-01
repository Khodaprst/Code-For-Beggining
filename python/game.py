import random
x = random.randint(1,100)
count = 1
name = input("enter your name: ")
question = input('Hi %s, ready to play? \n' % (name))
print('the answer is:',x)
if question == 'yes' or 'no':
    hads = int(input('enter your hads: '))
    while hads!=x:
        if hads > x:
            print('smaller, try again')
        else:
            print('bigger, try again')
        hads = int(input('enter your hads: '))
        count += 1
        print(count, 'times appeared.')
    print('You did it %s!!!' % (name))
else:
    print('OK, See you later.')