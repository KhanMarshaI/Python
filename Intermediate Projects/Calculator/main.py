import PySimpleGUI as gui

gui.theme('DarkBlack1')
layout = [[gui.Input(default_text='',size=(23,1), background_color='White', key='_input_')],
          [gui.Text(size=(20,1), key='_output_'), gui.Button('=')],
          [gui.Button('1'),gui.Button('2'), gui.Button('3'), gui.Button('/')],
          [gui.Button('4'),gui.Button('5'),gui.Button('6'), gui.Button('*')],
          [gui.Button('7'),gui.Button('8'),gui.Button('9'), gui.Button('-')],
          [gui.Button('C'), gui.Button('0'), gui.Button('.'),gui.Button('+')]
]

window = gui.Window('Calculator', layout, auto_size_buttons=False, default_button_element_size=(5,2))

userInput = ''
while True:
    event, value = window.read()
    if event == gui.WINDOW_CLOSED:
        break
    if event == 'C':
        userInput = ''
    if event in '0123456789+-/*.':
        userInput += event

    window['_input_'].update(userInput)


window.close()