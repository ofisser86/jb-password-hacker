import sys
from socket import socket

client = socket()

host = sys.argv[1]
port = int(sys.argv[2])
data = sys.argv[3]

address = (host, port)
client.connect(address)
data = data.encode()
client.send(data)
response = client.recv(1024)

print(response.decode())

client.close()
