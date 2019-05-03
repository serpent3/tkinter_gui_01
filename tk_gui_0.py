from tkinter import *
import json


with open("LISTS.json", "r") as f:
    dict_lists = json.loads(f.read())


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

list_in = Listbox(l1, width=25, height=20, selectmode=EXTENDED)
list_in.pack(side=RIGHT, padx=10)


def items_tracer(*args):
    # Очистка списка
    list_in.delete(0, END)
    for name in Items.keys():
        # Если галочка установлена
        if Items[name].get():
            # Показываетм все элементы в списке dict_lists по ключу name
            for i in dict_lists[name]:
                list_in.insert(END, i)


Items = {}
for name in dict_lists:
    # Создаём словарь из tkinter.BooleanVar обектов
    Items.update({name: BooleanVar()})
    Items[name].set(0)
    c1 = Checkbutton(l1, text=name, variable=Items[name], onvalue=1, offvalue=0)
    c1.pack(anchor=W)

    # Назначаем этим объектам функцию, реагирующую на событие установки галочки
    Items[name].trace('w', items_tracer)


############################################################
# 2

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
    with open("LISTS.json", "w") as f:
        dict_lists.update({"Мой список":[*list_out.get(0, END)]})
        f.write(json.dumps(dict_lists, ensure_ascii=False))

        
badd = Button(l2, text="Добавить в список", command=add_item)
badd.pack(side=TOP, fill=X)

badd = Button(l2, text="Удалить из списока", command=del_item)
badd.pack(side=TOP, fill=X)

badd = Button(l2, text="Сохранить список", command=save_list)
badd.pack(side=TOP, fill=X)

list_out =  Listbox(l2,  width=25, height=14, selectmode=EXTENDED)
list_out.pack(anchor=N)



############################################################

root.mainloop()
