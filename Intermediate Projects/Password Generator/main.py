import random
import PySimpleGUI as gui


class Generator:
    List = []
    def __init__(self, length):
        for i in range(length//2):
            tmp = chr(random.randint(65, 122))
            Generator.List.append(tmp)
        for j in range(length//2):
            tmp_digits = chr(random.randint(48,57))
            Generator.List.append(tmp_digits)

    def log(self):
        random.shuffle(Generator.List)
        tmp = ''.join([str(item) for item in Generator.List])
        Generator.List.clear()
        return tmp

# GUI
gui.theme('Dark')
layout = [
        [gui.Text('Insert the length of password in digits:')],
        [gui.Input(key = '-INPUT-')],
        [gui.Text(size=(40,1), key='-OUTPUT-')],
        [gui.Button('Generate'), gui.Button('Quit')]
]

window = gui.Window('Password Generator', layout)


while True:
    event, value = window.read()
    if event == gui.WINDOW_CLOSED or event == 'Quit':
        break

    try:
        tmp = int(value['-INPUT-'])
        password = Generator(tmp)
        window['-OUTPUT-'].update('Password = ' + password.log())
    except:
        gui.popup('Invalid input.')


