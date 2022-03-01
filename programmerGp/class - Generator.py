def generator():
    while True:
        try:
            n = 1
            print('this is first.')
            yield n

            n += 1
            print('this is second.')
            yield n

            n += 1
            print('this is last.')
            yield n

        except StopIteration:
            print('that would be unough.')
            break

a = generator()
print(next(a))
print(next(a))
print(next(a))