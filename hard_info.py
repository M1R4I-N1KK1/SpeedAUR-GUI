import subprocess as sub

def proc_all():
    processor = int(sub.check_output(['nproc', '--all'], shell=True))
    return processor

def proc_info():

    processor = proc_all()
    metade_do_processador = f'{processor / 2:.0f}'

    proc = None

    if processor <= 1:
        proc = processor

    else:
        proc = metade_do_processador

    return str(proc)


def type_processor():
    type_proc = str(sub.check_output(['sh', 'check.sh']))

    return type_proc[2:][:-3]
