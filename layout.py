from PySimpleGUI import PySimpleGUI as sg


def layout_window():
    sg.theme("reddit")
    sg.set_options(font=("Ubuntu", 12, 'bold'))

    layout = [
        [sg.Image('icon/head.png')],
        [sg.Text('DOWNLOAD MANAGER')],
        [sg.Radio('Curl (Default)', "RADIO1", default=True),
         sg.Radio('Aria2', "RADIO1", default=False),
         sg.Radio('Axel', "RADIO1", default=False)],

        [sg.Text('PROCESSOR ARCHITECTURE')],
        [sg.Input('', size=(30, 30), key='arch'), sg.Text('auto'),
         sg.Checkbox('', default=True, key='processor')],

        [sg.Text('CORE NUMBER')],
        [sg.Input('', size=(30, 30), key='core'),
         sg.Text('auto'), sg.Checkbox('', default=True, key='auto')],

        [sg.Button('OK'), sg.Button('Cancel', key='exit')],
        [sg.Text('')],
        [sg.Graph((30, 30), graph_bottom_left=(0, 30), graph_top_right=(30, 0),
                  key="telegram", change_submits=True, drag_submits=False),
         sg.Graph((30, 30), graph_bottom_left=(0, 30), graph_top_right=(30, 0),
                  key="github", change_submits=True, drag_submits=False),
         sg.Graph((175, 30), graph_bottom_left=(0, 60), graph_top_right=(60, 0),
                  key="space", change_submits=True, drag_submits=False),
         sg.Graph((140, 25), graph_bottom_left=(0, 30), graph_top_right=(30, 0),
                  key="dev", change_submits=True, drag_submits=False)],
    ]

    window = sg.Window('Speed AUR', layout)

    return window
