string = input()
point = sum((int(input())).to_bytes(2, 'little'))

for i in bytes(string, encoding='UTF-8'):
    print(end=f'{chr(i + point)}')
