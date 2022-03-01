def multiplication(vertical, horizontal):
    
    for a in range(1, vertical+1):
        for b in range(1, horizontal+1):
            print('{:^10}' .format(a*b), end=' ')
            if a*b == (vertical+1)*(horizontal+1):
                break

        print( )

vertical = int(input())
horizontal = int(input())
print(multiplication(vertical, horizontal))