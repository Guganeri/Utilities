import socket,sys

for ports in range(1,65535):

                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                        if s.connect_ex((sys.argv[1], ports)) == 0:

                                   print (f'PORTA”, {ports},  “ABERTA')

                                   s.close()