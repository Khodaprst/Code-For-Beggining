def mydecorator(func):


    print('inside decorator before')
    func()
    print('inside decorator after')

    return func

def printname():
    print('4mirdeist@gmail.com')

printname = mydecorator(printname)
printname()