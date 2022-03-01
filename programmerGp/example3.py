from subprocess import call
call(['ls', '-l'])
#--------------------------------------------

import getpass
print(getpass.getuser())
#--------------------------------------------

import socket
print(socket.gethostbyname(socket.gethostname()))