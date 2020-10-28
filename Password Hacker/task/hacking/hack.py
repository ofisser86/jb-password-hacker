import sys
import itertools
from socket import socket
import json

with socket() as client:
    host = sys.argv[1]
    port = int(sys.argv[2])
    # data = sys.argv[3]

    address = (host, port)
    client.connect(address)
    i = 1
    with open('logins.txt', 'r') as f:
        login = f.readlines()
        password = [' ']
        for _ in range(25):
            for i in itertools.product(login, password):
                data = {
                    "login": i[0].replace('\n', ""),
                    "password": i[1]
                }
                json_data = json.dumps(data).encode('utf8')
                client.send(json_data)
                response = client.recv(1024)
                if json.loads(response.decode('utf8'))['result'] == "Wrong password!":
                    new_data = {
                    "login": data['login'],
                    "password": 'abc'
                }
                    json_new_data = json.dumps(new_data).encode('utf8')
                    client.send(json_new_data)
                    response = client.recv(1024)
                    print(json_new_data.decode())
                    sys.exit()
                elif json.loads(response.decode('utf8'))['result'] == "Wrong login!":
                    continue
                elif json.loads(response.decode('utf8'))['result'] == "Connection success!":
                    print('Connection success!')

    # with open('passwords.txt', 'r') as f:
    #     password = f.readlines()
    #     l_pass = []
    #     for i in password:
    #         l_pass.append(i.replace('\n', ''))
    #     while True:
    #         for j in l_pass:
    #             x = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in j)))
    #             for m in x:
    #                 data = m.encode()
    #                 client.send(data)
    #                 response = client.recv(1024)
    #                 if response.decode() == 'Connection success!':
    #                     print(data.decode())
    #                     sys.exit()
    #         i = i + 1
