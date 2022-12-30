import time
import datetime
import winsound
import PySimpleGUI as gui

def countdown(hour, minute, second):
    convertedTime = hour * 3600 + minute * 60 + second

    while convertedTime > 0:
        global timer
        timer = datetime.timedelta(seconds = convertedTime) # converting the seconds into timer format 0:00:00
        time.sleep(1)
        convertedTime -= 1
    # (frequency, duration)
    winsound.Beep(2500, 5)


gui.theme('DarkBlack')
layout = [[gui.Text('Set a countdown. (Hour):(Minute):(Seconds)')],
          [gui.Input(key = '_hour_', size=(3, 1)), gui.Input(key='_minute_', size=(3, 1)), gui.Input(key = '_second_', size=(3,1))],
          [gui.Text(key='_output_', size=(40,1))],
          [gui.Button('Enter'), gui.Button('Exit')]
]
window = gui.Window('Countdown', layout)
while True:
    event, value = window.read()
    if event in (gui.WINDOW_CLOSED, 'Exit'):
        break
    try:
        hour, minute, second = int(value['_hour_']), int(value['_minute_']), int(value['_second_'])
        countdown(hour,minute,second)
        window['_output_'].update(timer)
    except:
        gui.popup('Invalid input.')

window.close()
