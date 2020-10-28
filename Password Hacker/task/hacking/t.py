import itertools
import json


with open('logins.txt', 'r') as f:
    login = f.readlines()
    print(login)
    password = ['']
    for _ in range(12):
        for i in itertools.product(login, password):
            x = {
                "name": i[0].replace('\n', ""),
                "password": i[1]
            }
            y = json.dumps(x)
            print(y)




        while True:
            for i in itertools.product(login, password):
                data = {
                    "name": i[0].replace('\n', ""),
                    "password": i[1]
                }
                json_data = json.dumps(data).encode()
                print(json_data)
                client.send(json_data)
                response = client.recv(1024)
                print(response)
                if response.decode() == {"result": "Wrong password!"}:
                    print(json_data)
                    sys.exit()
