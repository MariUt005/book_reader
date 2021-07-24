from os.path import abspath
from os.path import join
from glob import glob


def get_txt(path):
    return list(glob(join(path, '*.txt')))
