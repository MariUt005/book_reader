import eel
from os.path import join
from os import getcwd
from glob import glob

@eel.expose
def get_txt(path):
    paths = list(glob(join(path, '*.txt')))
    books = []
    for path in paths:
        books.append(path.split('\\')[-1])
    return books

@eel.expose
def get_path():
    print(getcwd())
    return getcwd()

eel.init("web")

eel.start("main.html")