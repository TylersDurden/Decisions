import os


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def execute(cmd, save_output):
    os.system(cmd+' >> output.txt')
    if save_output:
        return swap('output.txt', False)
    else:
        return swap('output.txt', True)