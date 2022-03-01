while True:
    try:
        a = int(input('enter number : '))
        break
    except ValueError:
        print('\n this is not a number . try again...')
        print()

#----------------------------------------------------
import socket
adr = '127.0.0.256'        
try:
    socket.inet_aton(adr)
    print('valid ip')

except socket.error:
    print('invailid ip')

    
