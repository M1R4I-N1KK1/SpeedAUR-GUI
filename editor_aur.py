import json
import final_process
import hard_info
from os import path
from gi.repository import Gtk
import gi
gi.require_version("Gtk", "3.0")


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
        self.entry_core_da_cpu = builder.get_object('entry_core_da_cpu')

        self.arch_auto_button = builder.get_object('arch_auto_button')
        self.core_auto_button = builder.get_object('core_auto_button')

        self.on_manager = builder.get_object('curl_manager')
        self.on_core = builder.get_object('core_auto_button')
        self.on_arch = builder.get_object('arch_auto_button')

        self.core_manual_button = builder.get_object('core_manual_button')

    ############################# Close APP and Dialog #############################
    def close_confirm_dialog_clicked(self, *args):
        self.window_msg.hide()

    def main_window_destroy(self, *args):
        Gtk.main_quit()

    def bt_cancel_clicked(self, *args):
        self.main_window_destroy()

    ############################# Manager Download #############################
    def manager_select(self, *args):
        radio_buttons = self.on_manager.get_group()
        for radio in radio_buttons:
            if radio.get_active():
                return radio.get_name()

    ############################# Core Process #############################
    def core_process(self, *args):
        core_buttons = self.on_core.get_group()
        for cores in core_buttons:
            if cores.get_active():
                if cores.get_name() == "auto":
                    return hard_info.proc_all()
                elif cores.get_name() == "default":
                    return hard_info.proc_meta()
                elif cores.get_name() == "manual":
                    try:
                        return str(int(self.entry_core_da_cpu.get_text()) + 1)
                    except ValueError:
                        return hard_info.proc_meta()

    def off_core_manual_button(self, *args):
        value = False
        value_box = ''
        self.entry_core_da_cpu.set_visible(value)
        self.entry_core_da_cpu.set_text(value_box)
        self.entry_core_da_cpu.set_editable(value)

    def on_core_manual_button_pressed(self, *args):
        if self.core_auto_button:
            value = self.core_auto_button
            self.entry_core_da_cpu.set_visible(value)

    ############################# Arch Process #############################
    def arch_process(self, *args):
        arch_buttons = self.on_arch.get_group()
        for arch_but in arch_buttons:
            if arch_but.get_active():
                if arch_but.get_name() == 'auto':
                    return hard_info.type_processor()
                elif arch_but.get_name() == 'default' or self.entry_arquitetura_da_cpu.get_text() == '':
                    return 'generic'
                elif arch_but.get_name() == 'manual':
                    return str(self.entry_arquitetura_da_cpu.get_text())

    def on_arch_manual_button_pressed(self, *args):
        if self.arch_auto_button:
            value = self.arch_auto_button
            self.entry_arquitetura_da_cpu.set_visible(value)
            self.entry_arquitetura_da_cpu.set_editable(value)

    def off_arch_manual_button(self, *args):
        value = False
        value_box = ''
        self.entry_arquitetura_da_cpu.set_visible(value)
        self.entry_arquitetura_da_cpu.set_text(value_box)

    ############################# Button OK #############################
    def bt_ok_clicked(self, *args):

        modification = mod.replace('CORECPU', self.core_process())\
            .replace('MANAGER', manager[self.manager_select()][0]).replace('ARCHCPU', self.arch_process())

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
