The following hash "cd0894152aa5eec36ec79eb2bcb90ca40f056804530f40732b4957a496b23dc8" was leaked from a database. On further investigation it was deducted that the database was using 
an SHA-256 encryption. Using the wordlist "rockyou.txt" available on internet we were able to crack the encryption.
Since there were more than a million password in the wordlist we had to automate the task of cracking the encryption. Using python we encrypt all the passwords and match it with the leaked hash,
once the hash matches we return the string at that position.

![image](https://github.com/KhanMarshaI/Python/assets/108894019/4d51ade1-c005-41da-806e-53061dd73ac5)

[Code]https://github.com/KhanMarshaI/Python/blob/master/Project/Cryptography/hash.py
