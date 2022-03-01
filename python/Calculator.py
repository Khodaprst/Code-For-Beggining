a = float(input())
b = float(input())
op = input('op: ')
if op == '+':
    print('%.3f %s %.3f = %.3f' % (a, op, b, a+b))
elif op == '-':
    print('%.3f %s %.3f = %.3f' % (a, op, b, a-b))
elif op == '*':
    print('%.3f %s %.3f = %.3f' % (a, op, b, a*b))
elif op == '/':
    print('%.3f %s %.3f = %.3f' % (a, op, b, a/b))
else:
    print('not defined in data my dear, try again.')