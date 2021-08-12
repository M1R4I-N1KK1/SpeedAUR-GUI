import json
import process
import hard_info
from os import path
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class MainWindow(object):
    def __init__(self, *args, **kwargs):
        self.style_css()

        self.window_msg = builder.get_object("msg")

        self.entry_arquitetura_da_cpu = builder.get_object("entry_arquitetura_da_cpu")
        self.entry_core_da_cpu = builder.get_object("entry_core_da_cpu")

        self.arch_auto_button = builder.get_object("arch_auto_button")
        self.core_auto_button = builder.get_object("core_auto_button")

        self.on_manager = builder.get_object("curl_manager")
        self.on_core = builder.get_object("core_auto_button")
        self.on_arch = builder.get_object("arch_auto_button")

        self.core_manual_button = builder.get_object("core_manual_button")
        self.spin_core_list = builder.get_object("spin_core_list")
        self.adjustment_list = builder.get_object("adjustment_list")

        self.mod = self.make = self.open_file(real_path="make_base.txt", modo="rt")
        with open(self.resource_path("manager.json")) as download_manager:
            self.manager_dl = json.load(download_manager)

    ############################# Creator File #############################
    def resource_path(self, relative_path):
        return path.realpath(relative_path)

    def open_file(self, real_path, modo):
        with open(self.resource_path(real_path), modo) as base:
            return base.read()

    def write_file(self, modif, base):
        with open(self.resource_path("make_base.txt"), "wt") as base:
            base.write(modif)

    ############################# Style App #############################
    def style_css(self, *args):
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path("ui/editor_style.css")
        screen = Gdk.Screen()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    ############################# Close APP and Dialog #############################
    def close_confirm_dialog_clicked(self, *args):
        self.window_msg.hide()

    def main_window_destroy(self, *args):
        Gtk.main_quit()

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
                    return str(self.spin_core_list.get_value_as_int() + 1)

    def off_core_manual_button(self, *args):
        self.spin_core_list.set_visible(False)
        self.spin_core_list.set_value(2)

    def on_core_manual_button_pressed(self, *args):
        self.spin_core_list.set_visible(True)
        self.adjustment_list.set_upper(int(hard_info.proc_all()) - 1)

    ############################# Arch Process #############################
    def arch_process(self, *args):
        arch_buttons = self.on_arch.get_group()
        for arch_but in arch_buttons:
            if arch_but.get_active():
                if arch_but.get_name() == "auto":
                    return hard_info.type_processor()
                elif (
                    arch_but.get_name() == "default"
                    or self.entry_arquitetura_da_cpu.get_text() == ""
                ):
                    return "generic"
                elif arch_but.get_name() == "manual":
                    return str(self.entry_arquitetura_da_cpu.get_text())

    def on_arch_manual_button_pressed(self, *args):
        self.entry_arquitetura_da_cpu.set_visible(self.arch_auto_button)

    def off_arch_manual_button(self, *args):
        self.entry_arquitetura_da_cpu.set_visible(False)
        self.entry_arquitetura_da_cpu.set_text("")

    ############################# Button OK #############################
    def bt_ok_clicked(self, *args):

        modification = (
            self.mod.replace("CORECPU", self.core_process())
            .replace("MANAGER", self.manager_dl[self.manager_select()][0])
            .replace("ARCHCPU", self.arch_process())
        )

        self.write_file(modification, "make_base")
        process.apply_system()
        self.write_file(self.make, "make_default")

        self.window_msg.show_all()


############################# Init App #############################
builder = Gtk.Builder()
builder.add_from_file("ui/editor_ui.glade")
builder.connect_signals(MainWindow())
window = builder.get_object("main_window").show_all()

try:
    Gtk.main()
except KeyboardInterrupt:
    pass
