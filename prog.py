from tkinter import *
import json
import os

from tk_gui_02 import Block


path = os.path.dirname(__file__)
path = os.path.join(path, "LISTS.json")


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
    import sys

    graphics_dir = "graphics"
    archives_dir = "archives"
    documents_dir = "documents"

    graphics = ['.png', '.jpg', '.jpeg', '.bmp']
    archives = ['.tar', '.zip', '.7zip', '.rar', '.iso', '.bin']
    documents = ['.fb2', '.pdf', '.doc', '.docx', '.xml', '.txt', '.md']

    os.chdir(main_directory)

    files_of_main_dir = []
    files_of_main_dir.clear()
    files_of_main_dir.extend(glob.glob('*.*'))

    for dir in dirs.keys():
        print('dir', dir)
        if not os.path.exists(dir):
            os.mkdir(dir)


    for i in files_of_main_dir:

        filename, file_extension = os.path.splitext(i)

        for dir in dirs.keys():
            types = dirs[dir] # Типы
            print('types', types)
            if file_extension in types:
                shutil.move(i, dir)




# def MAKE_FUNC(main_directory):
#     import os
#     import shutil
#     import glob
#     import sys
#
#     graphics_dir = "graphics"
#     archives_dir = "archives"
#     documents_dir = "documents"
#
#     graphics = ['.png', '.jpg', '.jpeg', '.bmp']
#     archives = ['.tar', '.zip', '.7zip', '.rar', '.iso', '.bin']
#     documents = ['.fb2', '.pdf', '.doc', '.docx', '.xml', '.txt', '.md']
#
#     os.chdir(main_directory)
#
#     files_of_main_dir = []
#
#     if not os.path.exists(graphics_dir):
#         os.mkdir(graphics_dir)
#     if not os.path.exists(archives_dir):
#         os.mkdir(archives_dir)
#     if not os.path.exists(documents_dir):
#         os.mkdir(documents_dir)
#
#     files_of_main_dir.clear()
#     files_of_main_dir.extend(glob.glob('*.*'))
#
#     for i in files_of_main_dir:
#         filename, file_extension = os.path.splitext(i)
#         if file_extension in graphics:
#             shutil.move(i, graphics_dir)
#         elif file_extension in archives:
#             shutil.move(i, archives_dir)
#         elif file_extension in documents:
#             shutil.move(i, documents_dir)
#
#     pass



root = Tk()

first_block = Block(root, READ_FUNC=READ_FUNC, DELETE_FUNC=DELETE_FUNC, SAVE_FUNC=SAVE_FUNC, MAKE_FUNC=MAKE_FUNC)

root.mainloop()



