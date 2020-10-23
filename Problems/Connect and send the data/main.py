def submit_data(data, client, address):
    client.connect(address)
    b_data = data.encode()
    client.send(b_data)
