import PySimpleGUI as gui

gui.theme('DarkBlack1')
layout = [[gui.Input(default_text='',size=(23,1), background_color='White', key='_input_', enable_events=True)],
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
    if event == '=':
        window['_output_'].update(eval(value['_input_'])) # eval can be dangerous as it treats everything like a command
    if event == 'C':
        userInput = ''
    if event in '0123456789+-/*.':
        userInput += event
        # if last char entered not a digit
    if event == '_input_' and len(value['_input_']) and value['_input_'][-1] not in ('0123456789+-/*.'):
        # delete last char from input
        window['_input_'].update(value['_input_'][:-1])
    window['_input_'].update(userInput)


window.close()