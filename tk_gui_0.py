from tkinter import *
import json

def read_lists():
    with open("LISTS.json", "r") as f:
        global dict_lists
        dict_lists = {}
        dict_lists = json.loads(f.read())

read_lists()

root = Tk()
root.title(u'Пример приложения')


############################################################
# Блоки окна

f_top = LabelFrame(text="Категории продуктов")
l1 = Label(f_top)
f_top.pack(side=LEFT, padx=10, pady=10)
l1.pack()

f_top = LabelFrame(text="Список продуктов")
l2 = Label(f_top)
f_top.pack(side=RIGHT, padx=10, pady=10)
l2.pack()


############################################################
# 1

# def make_list_in():
global list_in
list_in = Listbox(l1, width=25, height=20, selectmode=EXTENDED)
list_in.pack(side=RIGHT, fill=BOTH, expand=1)

scrollbar = Scrollbar(l1, orient="vertical")
scrollbar.config(command=list_in.yview)
scrollbar.pack(side=RIGHT, fill=Y, expand=1)

list_in.config(yscrollcommand=scrollbar.set)

# make_list_in()

def items_tracer(*args):
    # Очистка списка
    list_in.delete(0, END)
    for name in Items.keys():
        # Если галочка установлена
        if Items[name].get():
            # Показываетм все элементы в списке dict_lists по ключу name
            for i in dict_lists[name]:
                list_in.insert(END, i)

def make_Items():
    global Items
    Items = {}
    for name in dict_lists:
        # Создаём словарь из tkinter.BooleanVar обектов
        Items.update({name: BooleanVar()})
        Items[name].set(0)
        c1 = Checkbutton(l1, text=name, variable=Items[name], onvalue=1, offvalue=0)
        c1.pack(anchor=W)

        # Назначаем этим объектам функцию, реагирующую на событие установки галочки
        Items[name].trace('w', items_tracer)


make_Items()


############################################################
# 2

list_out =  Listbox(l2,  width=25, height=20, selectmode=EXTENDED)
list_out.pack(side=RIGHT)

scrollbar2 = Scrollbar(l2, orient="vertical")
scrollbar2.config(command=list_out.yview)
scrollbar2.pack(side=RIGHT, fill=Y, expand=1)

list_out.config(yscrollcommand=scrollbar2.set)


def add_item():
    for i in list_in.curselection():
        item_in = list_in.get(i)
        if not item_in in list_out.get(0, END):
            list_out.insert(END, item_in)


# !!! Удаление работает странно, пока не знаю почему
def del_item():
    for i in list_out.curselection():
        list_out.delete(i)


def save_list():
    l = Label(l2, width=20, text="Название списка:")
    l.pack()

    global entry
    entry = Entry(l2)
    entry.pack(anchor=N)

    badd = Button(l2, text="Сохранить", command=save)
    badd.pack(side=TOP, fill=X)


def save():
    name = entry.get()
    if name:
        with open("LISTS.json", "w") as f:
            dict_lists.update({name:[*list_out.get(0, END)]})
            f.write(json.dumps(dict_lists, ensure_ascii=False))
            l = Label(l2, width=20, text="Список {} сохранён".format(name))
            l.pack()

        read_lists()
        # Добавляем список
        Items.update({name: BooleanVar()})
        Items[name].set(0)
        c1 = Checkbutton(l1, text=name, variable=Items[name], onvalue=1, offvalue=0)
        c1.pack(anchor=W)
        # Назначаем объекту функцию, реагирующую на событие установки галочки
        Items[name].trace('w', items_tracer)


def del_list():
    for name in Items.keys():
        if Items[name].get():
            dict_lists.pop(name)
            # Items.pop(name)

    with open("LISTS.json", "w") as f:
        f.write(json.dumps(dict_lists, ensure_ascii=False))

    lst = l1.winfo_children()
    for l in lst:
        # if l.winfo_name() == 'с1':
        l.destroy()


    global list_in
    list_in = Listbox(l1, width=25, height=20, selectmode=EXTENDED)
    list_in.pack(side=RIGHT, fill=BOTH, expand=1)

    scrollbar = Scrollbar(l1, orient="vertical")
    scrollbar.config(command=list_in.yview)
    scrollbar.pack(side=RIGHT, fill=Y, expand=1)

    list_in.config(yscrollcommand=scrollbar.set)


    read_lists()
    make_Items()
    items_tracer()
    # make_list_in()
    # list_out.delete(0, END)






badd = Button(l2, text="Добавить в список", command=add_item)
badd.pack(side=TOP, fill=X)

badd = Button(l2, text="Удалить из списока", command=del_item)
badd.pack(side=TOP, fill=X)

badd = Button(l2, text="Сохранить список", command=save_list)
badd.pack(side=TOP, fill=X)

badd = Button(l2, text="Удалить список", command=del_list)
badd.pack(side=TOP, fill=X)

############################################################


root.mainloop()
