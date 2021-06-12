import subprocess as sub


def backup():
    sub.call(['pkexec', 'cp', '/etc/makepkg.conf', '/etc/makepkg.conf.bk'])


def restore():
    sub.call(['pkexec', 'cp', '/etc/makepkg.conf.bk', '/etc/makepkg.conf'])
