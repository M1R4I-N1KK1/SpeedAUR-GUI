import json
from os import path
from PySimpleGUI import PySimpleGUI as sg


def resource_path(relative_path):
    return path.realpath(relative_path)


with open(resource_path('manager.json')) as download_manager:
    manager = json.load(download_manager)

with open(resource_path('base.conf'), 'r') as base:
    base_make = base.read()


sg.theme("reddit")

layout = [
    [sg.Image('speedaur-head.png')],
    [sg.Text('DOWNLOAD MANAGER')],
    [sg.Radio('Curl (Default)', "RADIO1", key='curl', default=True)],
    [sg.Radio('Aria2', "RADIO1", key='aria2', default=False)],
    [sg.Radio('Axel', "RADIO1", key='axel', default=False)],
    [],
    [sg.Text('CORE NUMBER')],
    [sg.Input('', key='core'),
     sg.Text('AUTO'), sg.Checkbox('', default=True, key='auto')],
    [sg.Button('append'), sg.Button('exit')],
    [sg.Text('')],
    [sg.Text('by M1R41 N1KK1', justification='right', size=(60, 1))]
]

window = sg.Window('Speed AUR', layout)

new_make = ''
core = ''
manager_select = ''

while True:
    events, values = window.read()

    if events == 'append':
        if values["curl"]:
            manager_select = 'curl'
        elif values["aria2"]:
            manager_select = 'aria2'
        elif values["axel"]:
            manager_select = 'axel'

    if values["auto"]:
        core = '$(($(nproc)+1)'
        sg.Popup("AUTO SELECT")
        break

    else:
        try:
            if int(values["core"]):
                core = int(values["core"])
                break

        except ValueError:
            sg.Popup("Digite o numero de core do processador",
                     "ou marque a caixinha \"AUTO\"")

    if events == sg.WIN_CLOSED or events == "exit":
        break

new_make = base_make.replace('MANAGER', str(manager[manager_select][0])).replace('CORE', str(core + 1))

with open(resource_path('new_make_core.conf'), 'w+') as make:
    make.write(new_make)

sg.Popup('Aplicado com sucesso')

window.close()
