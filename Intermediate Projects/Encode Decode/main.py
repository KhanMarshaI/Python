import base64
import PySimpleGUI as gui


def encode(str):
    # global bytes_to_string # unnecessary to have a global var
    str_bytes = str.encode('ascii') # converting the input into a bytes-like object
    encodedStr =  base64.standard_b64encode(str_bytes)
    bytes_to_string = encodedStr.decode('ascii')
    return bytes_to_string


def decode(encodedVar):
    decoded = base64.standard_b64decode(encodedVar)
    decode_bytes = decoded.decode('ascii') # converting the bytes-like object back to a string
    return decode_bytes


gui.theme('DarkGrey15')

encode_layout = [[gui.Text('Encode Message: (Input)')],
          [gui.Multiline(key='_encode_', s=(30,2))],
          [gui.Text('Encoded Message: (Output)')],
          [gui.Multiline(key='_encodeOut_', size=(30,2), disabled=True)],
          [gui.Button('Encode')]
]

decode_layout = [[gui.Text('Decode String: (Input)')],
                 [gui.Multiline(s=(30,2), key='_decodeIn_')],
                 [gui.Text('Decoded String: (Output)')],
                 [gui.Multiline(s=(30,2), key='_decodeOut_', disabled=True)],
                 [gui.Button('Decode')]
]

tab_layout = [[gui.Tab('Encoder', encode_layout, key='_tab1_')],
              [gui.Tab('Decoder', decode_layout, key='_tab2_')]
]

layout = [[gui.TabGroup(tab_layout, enable_events=True, key='_tabgroup_')]]
window = gui.Window('Encoder/Decoder', layout)

while True:
    event, value = window.read()
    if event == gui.WINDOW_CLOSED:
        break
    if event == 'Encode':
        window['_encodeOut_'].update(encode(value['_encode_']))
    if event == 'Decode':
        window['_decodeOut_'].update(decode(value['_decodeIn_']))

window.close()
