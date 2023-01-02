import random
import PySimpleGUI as gui
import os

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

    def copyToClipboard(self, string):
        command = 'echo | set /p nul=' + string.strip() + '| clip'
        os.system(command)

# GUI
gui.theme('Dark')
layout = [
        [gui.Text('Length: '), gui.Input(key = '-INPUT-', size=(3,1))],
        [gui.Text(size=(40,1), key='-OUTPUT-')],
        [gui.Button('Generate'), gui.Button('Copy'),gui.Button('Quit')]
]

window = gui.Window('Password Generator', layout, element_justification='l')


while True:
    event, value = window.read()
    if event == gui.WINDOW_CLOSED or event == 'Quit':
        break
    try:
        tmp = int(value['-INPUT-'])
        if event=='Generate':
            password = Generator(tmp)
            generatedPass = password.log()
            window['-OUTPUT-'].update('Password = ' + generatedPass)
        if event == 'Copy':
            password.copyToClipboard(generatedPass)
            gui.popup('Copied to clipboard.')
    except:
        gui.popup('Invalid input.')


