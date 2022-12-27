import random
class Generator:
    List = []

    def __init__(self):
        for i in range(lengthOfPassword//2):
            tmp = chr(random.randint(65, 122))
            Generator.List.append(tmp)
        for j in range(lengthOfPassword//2):
            tmp_digits = chr(random.randint(48,57))
            Generator.List.append(tmp_digits)

    def log(self):
        random.shuffle(Generator.List)
        tmp = ''.join([str(item) for item in Generator.List])
        print(tmp)


lengthOfPassword = int(input('Insert the length of the password: '))
s = Generator()
s.log()
