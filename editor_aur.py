## M1R4I
import json
import final_process
import hard_info
from os import path
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def resource_path(relative_path):
    return path.realpath(relative_path)


with open(resource_path('manager.json')) as download_manager:
    manager = json.load(download_manager)

with open(resource_path('make_base'), 'rt') as base:
    data = base.read()

builder = Gtk.Builder()
builder.add_from_file('window_gtk_aur.glade')
mod = make = data


class MainWindow(object):

    def __init__(self, *args, **kwargs):

        self.window_msg = builder.get_object('msg')

        self.entry_arquitetura_da_cpu = builder.get_object('entry_arquitetura_da_cpu')
        self.arch_auto_button = builder.get_object('arch_auto_button')

        self.entry_core_da_cpu = builder.get_object('entry_core_da_cpu')
        self.core_auto_button = builder.get_object('core_auto_button')

        self.aria2_manager = builder.get_object('aria2_manager')
        self.curl_manager = builder.get_object('curl_manager')
        self.axel_manager = builder.get_object('axel_manager')

        self.core = self.arch = self.manager_select = ''

    def close_confirm_dialog_clicked(self, *args):
        self.window_msg.hide()

    def main_window_destroy(self, *args):
        Gtk.main_quit()

    def bt_cancel_clicked(self, *args):
        Gtk.main_quit()

    def bt_ok_clicked(self, *args):

        if self.curl_manager.get_active():
            self.manager_select = 'curl'
        elif self.aria2_manager.get_active():
            self.manager_select = 'aria2'
        elif self.axel_manager.get_active():
            self.manager_select = 'axel'

        if self.entry_arquitetura_da_cpu.get_text() == '':
            if self.arch_auto_button.get_active():
                self.arch = hard_info.type_processor()

            else:
                self.arch = 'generic'

        else:
            self.arch = str(self.entry_arquitetura_da_cpu.get_text())

        if self.entry_core_da_cpu.get_text() == '':
            if self.core_auto_button.get_active():
                self.core = '$(($(nproc)+1)'
            else:
                self.core = hard_info.proc_info()

        else:
            self.core = str(int(self.entry_core_da_cpu.get_text()) + 1)

        modification = mod.replace('CORECPU', self.core).replace('MANAGER', manager[self.manager_select][0]) \
            .replace('ARCHCPU', self.arch)

        with open(resource_path('make_base'), 'wt') as base_make:
            base_make.write(modification)

        final_process.apply_system()

        with open(resource_path('make_base'), 'wt') as make_default:
            make_default.write(make)

        self.window_msg.show_all()


builder.connect_signals(MainWindow())
window = builder.get_object('main_window').show_all()

if __name__ == '__main__':
    Gtk.main()
