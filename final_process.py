import shutil
from backup_restore import backup
from os import path


def resource_path(relative_path):
    return path.realpath(relative_path)


def apply_system():
    while True:
        if path.exists(f'{HOME}.makepkg.conf.bk'):
            shutil.copy(resource_path('make_base'), f'{HOME}.makepkg.conf')
            break

        else:
            backup()


HOME = path.expanduser("~/")
