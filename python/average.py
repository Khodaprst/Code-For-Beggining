def printlist(lst):
    for x in lst:
        print(x, ' ', end = ' ')
    print()
stlist = []
while True:
    ave = float(input('enter an average: '))
    if ave == 0.0:
        break
    else:
        stlist.append(ave)
ave = float(input('enter an ave to count it: '))
print('the count of', ave, 'in list is:',stlist.count(ave))
print('contents of the list is: ')
printlist(stlist)
stlist.sort()
print('sorted list is: ' ,stlist)
