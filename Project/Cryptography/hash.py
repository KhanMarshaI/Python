import hashlib

hash = 'cd0894152aa5eec36ec79eb2bcb90ca40f056804530f40732b4957a496b23dc8'
with open('rockyou.txt', 'r', encoding='ISO-8859-1') as file:
    string = file.read()

list = string.split()
for i in range(len(list)):
    m = hashlib.sha256(list[i].encode('UTF-8'))
    if m.hexdigest() == hash:
        print(list[i])
        break

