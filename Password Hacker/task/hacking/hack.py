import sys
import itertools
from socket import socket

alpha = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(48, 58)]

with socket() as client:

    host = sys.argv[1]
    port = int(sys.argv[2])
    # data = sys.argv[3]

    address = (host, port)
    client.connect(address)
    i = 1
    while True:
        x = itertools.product(alpha, repeat=i)
        for j in range(len(alpha) ** i):
            try_pass = "".join((next(x)))
            data = try_pass.encode()
            client.send(data)
            response = client.recv(1024)
            if response.decode() == 'Connection success!':
                print(data.decode())
                sys.exit()
        i = i + 1
