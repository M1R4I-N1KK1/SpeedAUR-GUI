import os
import subprocess as sub
from backup_restore import backup
from os import path


def resource_path(relative_path):
    return path.realpath(relative_path)


def apply_system():
    while True:
        if os.path.exists('/etc/makepkg.conf.bk'):
            sub.run(['pkexec', 'cp', resource_path('makepkg.conf'), '/etc/makepkg.conf'])
            break

        else:
            backup()
