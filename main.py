import json
import webbrowser
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
    [sg.Radio('Curl (Default)', "RADIO1", default=True)],
    [sg.Radio('Aria2', "RADIO1", default=False)],
    [sg.Radio('Axel', "RADIO1", default=False)],
    [sg.Text('PROCESSOR ARCHITECTURE')],
    [sg.Input('', key='arch'), sg.Text('AUTO'),
     sg.Checkbox('', default=True, key='processor')],

    [sg.Text('CORE NUMBER')],
    [sg.Input('', key='core'),
     sg.Text('AUTO'), sg.Checkbox('', default=True, key='auto')],

    [sg.Button('append'), sg.Button('exit')],
    [sg.Text('')],
    [sg.Graph((30, 30), graph_bottom_left=(0, 30), graph_top_right=(30, 0),
              key="telegram", change_submits=True, drag_submits=False),
     sg.Graph((30, 30), graph_bottom_left=(0, 30), graph_top_right=(30, 0),
              key="github", change_submits=True, drag_submits=False),
     sg.Text('by M1R41 N1KK1', justification='right', size=(60, 1))]
]

window = sg.Window('Speed AUR', layout, size=(450, 380))

telegram = window.Finalize().Element("telegram").DrawImage(filename="icon-telegram.png", location=(2, 1))
github = window.Finalize().Element("github").DrawImage(filename="icon-github.png", location=(2, 1))

new_make = ''
core = ''
manager_select = ''

while True:

    events, values = window.read()

    if events == sg.WIN_CLOSED or events == "exit":
        exit()
        break

    # grupo do telegram
    if events == 'telegram':
        webbrowser.open_new_tab("https://t.me/LinuxLabo")
        pass

    if events == 'github':
        webbrowser.open_new_tab("https://github.com/M1R4I-N1KK1/SpeedAUR-GUI")
        pass

    # Vericando a opçao do gerenciador de download
    if events == 'append':
        for x in range(1, 4):
            if str(values[x]) in 'True':
                manager_select = str(x)

        if values["auto"]:
            core = '$(($(nproc)+1)'
            break

        else:
            try:
                if int(values["core"]):
                    core = str(int(values["core"]) + 1)
                    break

            except ValueError:
                sg.Popup("Digite o numero de core's do processador",
                         "ou marque a caixinha \"AUTO\"")
                pass

# escrevendo as modifições em um arquivo temporario

new_make = base_make.replace('MANAGER', str(manager[manager_select][0])).replace('CORE', core)

with open(resource_path('new_make_core.conf'), 'w+') as make:
    make.write(new_make)

sg.Popup('Aplicado com sucesso')

window.close()
