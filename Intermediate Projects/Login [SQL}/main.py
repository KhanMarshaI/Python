import mysql.connector
import PySimpleGUI as gui


class Login:
    def __init__(self):
        self.database = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='testdatabase'
        )
        self.myCursor = self.database.cursor(buffered=True) # if buffer is set to False on clicking the Login button twice the program will crash due to results being loaded in the cursor

    def addUser(self, username, password):
        try:
            validateUsername = self.getUser(username)
            if validateUsername == 0:
                window['_error_'].update('User already exists, proceed to login!')
            else:
                self.myCursor.execute('INSERT INTO user (username, password) VALUES (%s,%s)', (str(username), str(password)))
                self.database.commit()
                gui.popup('Successfully registered!')
        except:
            window['_error_'].update('Either username already exists, or an error occured.')

    def getUser(self, username):  # Check whether username already exists in the database or not
        self.myCursor.execute('SELECT * FROM user')
        for x in self.myCursor:
            if x[0] == username:
                return 0  # if user exists we return 0
        return 1 # else we return 1

    def loginUser(self, username, password):
        self.myCursor.execute('SELECT * FROM user')
        for x in self.myCursor:
            if x[0] == username and x[1] == password:
                gui.popup('Login successful!')
                break
        else:
            window['_error_'].update('Incorrect credentials.')

login = Login()

# login.addUser('test1', 'test')
# print(login.getUser())
# login.myCursor.execute('CREATE TABLE user (username VARCHAR(12), password VARCHAR(16))')

CustomGUITheme = {'BACKGROUND': '#282930',
                  'TEXT': '#FDFFFF',
                  'INPUT': '#383942',
                  'TEXT_INPUT': '#FFFFFF',
                  'SCROLL': '#c7e78b',
                  'BUTTON': ('white', '#383942'),
                  'PROGRESS': ('#01826B', '#D0D0D0'),
                  'BORDER': 1,
                  'SLIDER_DEPTH': 0,
                  'PROGRESS_DEPTH': 0
}
gui.theme_add_new('LoginTheme', CustomGUITheme)
gui.theme('LoginTheme')
layout = [[gui.Text('Login Menu', size=(20,1),justification='center')],
          [gui.Text('Username:')],
          [gui.InputText(size=(21,1), key='_username_')],
          [gui.Text('Password:')],
          [gui.InputText(size=(21,1), key='_password_', password_char='*')],
          [gui.Button('Login'), gui.Button('Register')],
          [gui.Text(key='_error_', size=(21,2))]
]
window = gui.Window('Menu',layout, auto_size_buttons=False, default_button_element_size=(8,1), margins=(50,50))

while True:
    event, value = window.read()
    if event == gui.WINDOW_CLOSED:
        break
    if event=='Login':
        login.loginUser(value['_username_'], value['_password_'])
    if event=='Register':
        login.addUser(value['_username_'], value['_password_'])

window.close()