from tkinter import *
import json

from tk_gui_02 import Block


def READ_FUNC():
    with open("LISTS.json", "r", encoding="utf-8") as f:
        dict_lists = {}
        dict_lists = json.loads(f.read())
    return dict_lists


def DELETE_FUNC(dict_lists):
    with open("LISTS.json", "w") as f:
        f.write(json.dumps(dict_lists, ensure_ascii=False))


def SAVE_FUNC(dict_lists):
    with open("LISTS.json", "w") as f:
        f.write(json.dumps(dict_lists, ensure_ascii=False))

root = Tk()

first_block = Block(root, READ_FUNC=READ_FUNC, DELETE_FUNC=DELETE_FUNC, SAVE_FUNC=SAVE_FUNC)

root.mainloop()



