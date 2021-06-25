import shutil
from os import path


def resource_path(relative_path):
    return path.realpath(relative_path)


def backup():
    if path.exists(f'{HOME}.makepkg.conf'):
        shutil.copy(f'{HOME}.makepkg.conf', f'{HOME}.makepkg.conf.bk')

    else:
        shutil.copy(resource_path("make_base"), f'{HOME}.makepkg.conf')


def restore():
    if path.exists(f'{HOME}.makepkg.conf.bk'):
        shutil.copy(f'{HOME}.makepkg.conf.bk', f'{HOME}.makepkg.conf')

    else:
        pass


HOME = path.expanduser("~/")
