def fact(i):
    fact = 1
    j = 1
    while j <= i:
        fact *= j
        j += 1
    return fact