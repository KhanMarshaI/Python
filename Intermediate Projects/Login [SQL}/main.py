import mysql.connector
import PySimpleGUI


class Login:
    def __init__(self):
        self.database = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='testdatabase'
        )
        self.myCursor = self.database.cursor()

    def addUser(self, username, password):
        try:
            validateUsername = self.getUser(username)
            if validateUsername == 0:
                print('Username already exists!')
            else:
                self.myCursor.execute('INSERT INTO user (username, password) VALUES (%s,%s)', (str(username), str(password)))
                self.database.commit()
        except:
            print('Either username already exists, or an error occured.')

    def getUser(self, username):  # Check whether username already exists in the database or not
        self.myCursor.execute('SELECT * FROM user')
        for x in self.myCursor:
            if x[0] == username:
                return 0  # if user exists we return 0
        return 1 # else we return 1

x = Login()
x.addUser('test1', 'test')
# print(x.getUser())
# x.myCursor.execute('CREATE TABLE user (username VARCHAR(12), password VARCHAR(16))')