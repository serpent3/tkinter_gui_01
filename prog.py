from tkinter import *
import json
import os

from tk_gui_02 import Block


script_path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_path, "LISTS.json")


def READ_FUNC():
    with open(path, "r", encoding="utf-8") as f:
        dict_lists = {}
        dict_lists = json.loads(f.read())
    return dict_lists


def DELETE_FUNC(dict_lists):
    with open(path, "w") as f:
        f.write(json.dumps(dict_lists, ensure_ascii=False))


def SAVE_FUNC(dict_lists):
    with open(path, "w") as f:
        f.write(json.dumps(dict_lists, ensure_ascii=False))


def MAKE_FUNC(main_directory, dirs):
    import os
    import shutil
    import glob

    os.chdir(main_directory)

    files_of_main_dir = []
    files_of_main_dir.clear()
    files_of_main_dir.extend(glob.glob('*.*'))

    for dir in dirs.keys():
        # print('dir', dir)
        if not os.path.exists(dir):
            os.mkdir(dir)

    for i in files_of_main_dir:

        filename, file_extension = os.path.splitext(i)

        for dir in dirs.keys():
            types = dirs[dir]
            if file_extension in types:
                shutil.move(i, dir)

    os.chdir(script_path)


root = Tk()

first_block = Block(root, READ_FUNC=READ_FUNC, DELETE_FUNC=DELETE_FUNC, SAVE_FUNC=SAVE_FUNC, MAKE_FUNC=MAKE_FUNC)

root.mainloop()



