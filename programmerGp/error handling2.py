import random
class Error(Exception):
    pass

class BigNumber(Error):
    pass

class SmallNumber(Error):
    pass

adad = random.randint(0, 100)
while True:
    try:
        hads = int(input('what is your hads: '))
        if hads > adad:
            raise BigNumber
        elif hads < adad:
            raise SmallNumber
        break
    except BigNumber:
        print('try again, this time enter a smaller value.')
    except SmallNumber:
        print('try again, this time enter a bigger value.')

print('you did it!')