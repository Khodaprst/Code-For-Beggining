x = input()
tool = len(x)
x = x.lower()

if x[:1] == x[-1:] :
    print('palindrome')
else:
    print('not palindrome')