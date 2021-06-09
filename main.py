import json
import webbrowser
import layout
from os import path
from PySimpleGUI import PySimpleGUI as sg


def resource_path(relative_path):
    return path.realpath(relative_path)


with open(resource_path('manager.json')) as download_manager:
    manager = json.load(download_manager)

with open(resource_path('base.conf'), 'r') as base:
    base_make = base.read()

window = layout.layout_window()

element_icon = window.Finalize().Element("telegram").DrawImage(filename="icon/telegram.png", location=(2, 1)),\
           window.Finalize().Element("github").DrawImage(filename="icon/github.png", location=(2, 1)),\
           window.Finalize().Element("dev").DrawImage(filename="icon/dev.png", location=(3, 1))

new_make = core = manager_select = ''

while True:
    events, values = window.read()

    if events == sg.WIN_CLOSED or events == "exit":
        exit()
        break

    # grupo do telegram and github
    if events == 'telegram':
        webbrowser.open_new_tab("https://t.me/LinuxLabo")

    if events == 'github':
        webbrowser.open_new_tab("https://github.com/M1R4I-N1KK1/SpeedAUR-GUI")

    # Vericando a opçao do gerenciador de download
    if events == 'OK':
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

# escrevendo as modifições em um arquivo temporario
#new_make = base_make.replace('MANAGER', str(manager[manager_select][0])).replace('CORE', core)

with open(resource_path('new_make_core.conf'), 'w+') as make:
    make.write(base_make.replace('MANAGER', str(manager[manager_select][0])).replace('CORE', core))

sg.Popup('Aplicado com sucesso')

window.close()
