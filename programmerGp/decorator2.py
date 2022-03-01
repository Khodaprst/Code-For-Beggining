def mydecorator(msg='message'):
    def decorated(func):
        def wrapper(name):
            print('inside decorator before')
            print(f'your message is: {msg}')
            func(name)
            print('inside decorator after')

        return wrapper
    return decorated

@mydecorator('this is a message')
def printname(name):
    print(name)

#printname = mydecorator(printname)
printname('AmirHosein')


