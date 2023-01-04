import PySimpleGUI as gui

gui.theme('DarkBlue1')
score = 0
layout = [[gui.Text(f'Score: {score}', key='_score_')],
          [gui.Button('', key='_test_')]
]
window = gui.Window('Test', layout)
while True:
    event,value = window.read()
    if event == gui.WINDOW_CLOSED:
        break
    if event == '_test_':
        score +=1
        window['_score_'].update(f'Score: {score}')


window.close()