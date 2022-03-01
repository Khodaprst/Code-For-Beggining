def even(n):
    if n%2 == 0:
        return True
    else:
        return False

first = 1
second = 2
sum = 0
while (first  < 4*10**6):
    print('my number is: ', first)
    if even(first):
        print("oh it's even, here we go")
        sum = sum + first
        print('the sum is: ', sum)
    first, second = second, first+ second

print(sum)