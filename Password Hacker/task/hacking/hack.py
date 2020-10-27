import sys
import itertools
from socket import socket


with socket() as client:
    with open('passwords.txt', 'r') as f:
        f.readlines()
    host = sys.argv[1]
    port = int(sys.argv[2])
    # data = sys.argv[3]

    address = (host, port)
    client.connect(address)
    i = 1
    with open('passwords.txt', 'r') as f:
        password = f.readlines()
        l_pass = []
        for i in password:
            l_pass.append(i.replace('\n', ''))
        while True:
            for j in l_pass:
                x = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in j)))
                for m in x:
                    data = m.encode()
                    client.send(data)
                    response = client.recv(1024)
                    if response.decode() == 'Connection success!':
                        print(data.decode())
                        sys.exit()
            i = i + 1
