import subprocess as sub


def proc_processor():
    processor = int(sub.check_output(['nproc', '--all'], shell=True))
    return processor


def proc_all():
    return str(proc_processor() + 1)


def proc_meta():

    processor = proc_processor()
    metade_do_processador = f'{processor / 2:.0f}'

    if processor <= 1:
        return processor + 1

    else:
        return int(metade_do_processador) + 1


def type_processor():
    type_proc = str(sub.check_output(['sh', 'check.sh']))

    return type_proc[2:][:-3]
