import PySimpleGUI as gui
from time import sleep
from random import choice

MAX_ROW = MAX_COL = 5
NO_OF_TILES = 3
button_keys = [[(row, col) for col in range(MAX_COL)] for row in range(MAX_ROW)] # creating keys for the button element

List = [element for i in button_keys for element in i] # converting the nested lists to a Flat List
arr = [] # I know I know, so many arrays but this was the only approach I could think of

def generateTiles():
    for i in range(NO_OF_TILES): # generating random tiles
        tmp = choice(List)
        if tmp not in arr: # TO ENSURE THERE ARE NO DUPLICATE TILES
            arr.append(tmp)
        else:
            tmp = choice(List)
            arr.append(tmp)
        window[tmp].update(button_color='red')
        window.refresh()
    sleep(1)
    for i in arr: # changing the color of those buttons back to inital color
        window[i].update(button_color='snow')

gui.theme('DarkBlue1')
score = 0
layout = [[gui.Text(f'Score: {score}', key='_score_')],
          [gui.Text(key='_output_')]
]
layout += [[gui.Button(button_color='snow',key=(row,col)) for col in range(MAX_COL)] for row in range(MAX_ROW)] # generating buttons using List Comprehension


window = gui.Window('Memory Tiles', layout, auto_size_buttons=False,default_button_element_size=(5,2), finalize=True)

generateTiles()
while True:
    event,value = window.read()
    if event == gui.WINDOW_CLOSED:
        break
    if event in arr:
        arr.remove(event)
        score += 1
        window['_score_'].update(f'Score: {score} (+1)')
        window['_output_'].update('Correct!')
        if len(arr) == 0:
            generateTiles()
    else:
        if score > 0:
            score -= 1
        window['_score_'].update(f'Score: {score} (-1)')
        window['_output_'].update('You suck.')

window.close()