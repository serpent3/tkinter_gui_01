from tkinter import *
import json


class Block:
    def __init__(self, root, READ_FUNC, DELETE_FUNC, SAVE_FUNC, MAKE_FUNC):
        self.root = root
        self.READ_FUNC = READ_FUNC
        self.DELETE_FUNC = DELETE_FUNC
        self.SAVE_FUNC = SAVE_FUNC
        self.MAKE_FUNC = MAKE_FUNC

        # Блоки окна
        self.left_frame = LabelFrame(text="Категории продуктов")
        self.left_frame.pack(side=LEFT, padx=10, pady=10)
        self.left_frame_label = Label(self.left_frame)
        self.left_frame_label.pack()

        self.right_frame = LabelFrame(text="Список продуктов")
        self.right_frame.pack(side=RIGHT, padx=10, pady=10)
        self.right_frame_label = Label(self.right_frame)
        self.right_frame_label.pack()

        # 1
        self.make_list_in()

        # 2
        self.make_list_out()

        # Кнопки
        self.button_add = Button(self.right_frame, text="Добавить в список", command=self.add_item)
        self.button_add.pack(side=TOP, fill=X)

        self.button_del_item = Button(self.right_frame, text="Удалить элемент\n из списока", command=self.del_item)
        self.button_del_item.pack(side=TOP, fill=X)

        self.button_save = Button(self.right_frame, text="Сохранить список", command=self.save_list)
        self.button_save.pack(side=TOP, fill=X)

        self.button_del_list = Button(self.right_frame, text="Удалить список", command=self.del_list)
        self.button_del_list.pack(side=TOP, fill=X)

        self.button_del_list = Button(self.right_frame, text="СОРТИРОВКА", command=self.make_func)
        self.button_del_list.pack(side=TOP, fill=X)
        # Кнопки

        self.dict_lists = {}
        self.Items = {}
        self.read_lists()
        self.make_Items()

    #######################################
    # Функции создания объектов на форме
    def make_list_in(self):
        # Список и его скроллер
        self.list_in = Listbox(self.left_frame, width=25, height=20, selectmode=EXTENDED)
        self.list_in.pack(side=RIGHT, fill=BOTH, expand=1)

        self.list_in_scrollbar = Scrollbar(self.left_frame, orient="vertical")
        self.list_in_scrollbar.config(command=self.list_in.yview)
        self.list_in_scrollbar.pack(side=RIGHT, fill=Y, expand=1)

        self.list_in.config(yscrollcommand=self.list_in_scrollbar.set)
        # Список и его скроллер

    def make_list_out(self):
        # Список и его скроллер
        self.list_out =  Listbox(self.right_frame,  width=25, height=20, selectmode=EXTENDED)
        self.list_out.pack(side=RIGHT)

        self.list_out_scrollbar = Scrollbar(self.right_frame, orient="vertical")
        self.list_out_scrollbar.config(command=self.list_out.yview)
        self.list_out_scrollbar.pack(side=RIGHT, fill=Y, expand=1)

        self.list_out.config(yscrollcommand=self.list_out_scrollbar.set)
        # Список и его скроллер
    #######################################

    #######################################
    # Чтение данных из внешнего источника
    def read_lists(self):
        self.dict_lists = self.READ_FUNC()
        # with open("LISTS.json", "r", encoding="utf-8") as f:
        #     global dict_lists
        #     self.dict_lists = {}
        #     self.dict_lists = json.loads(f.read())

    # Функция основляющая списки
    def items_tracer(self, *args):
        # Очистка списка
        self.list_in.delete(0, END)
        for name in self.Items.keys():
            # Если галочка установлена
            if self.Items[name].get():
                # Показываетм все элементы в списке dict_lists по ключу name
                for i in self.dict_lists[name]:
                    self.list_in.insert(END, i)

    # Создаём словарь для работы со списками
    def make_Items(self):
        global Items
        self.Items = {}
        for name in self.dict_lists:
            # Создаём словарь из tkinter.BooleanVar обектов
            self.Items.update({name: BooleanVar()})
            self.Items[name].set(0)
            _ = Checkbutton(self.left_frame, text=name, variable=self.Items[name], onvalue=1, offvalue=0)
            _.pack(anchor=W)

            # Назначаем этим объектам функцию, реагирующую на событие установки галочки
            self.Items[name].trace('w', self.items_tracer)
    # Управляющие внешними данными функции
    #######################################

    #######################################
    # Функции внутренеей работы со списками
    # Добавление элемента в свой список
    def add_item(self):
        for i in self.list_in.curselection():
            item_in = self.list_in.get(i)
            if not item_in in self.list_out.get(0, END):
                self.list_out.insert(END, item_in)

    # !!! Удаление работает странно, пока не знаю почему
    # По одному удаляет нормально
    def del_item(self):
        for i in self.list_out.curselection():
            self.list_out.delete(i)
    # Функции внутренеей работы со списками
    #######################################

    #######################################
    # Функции, пишущие результат
    # Удаление списка
    def del_list(self):
        self.button_del_list.configure(state=DISABLED)

        for name in self.Items.keys():
            if self.Items[name].get():
                self.l_del_question = Label(self.right_frame, width=20, text="Удалить {}?".format(name))
                self.l_del_question.pack()

        self.l_del_warning = Label(self.right_frame, width=20, text="Это действие\nневозможно отменить".format(name))
        self.l_del_warning.pack()

        self.del_button = Button(self.right_frame, text="Удалить", command=self.delele)
        self.del_button.pack(side=TOP, fill=X)

        self.cancel_button = Button(self.right_frame, text="Отмена", command=self.cancel)
        self.cancel_button.pack(side=TOP, fill=X)

    def delele(self):
        for name in self.Items.keys():
            if self.Items[name].get():
                self.dict_lists.pop(name)
                # Items.pop(name)

        self.DELETE_FUNC(self.dict_lists)
        # with open("LISTS.json", "w") as f:
        #     f.write(json.dumps(self.dict_lists, ensure_ascii=False))

        # Всё убираем из левого фрейма
        lst = self.left_frame.winfo_children()
        for l in lst:
            # if l.winfo_name() == 'с1':
            l.destroy()

        # и перерисовываем
        self.make_list_in()
        self.read_lists()
        self.make_Items()
        self.items_tracer()

        self.l_del_question.destroy()
        self.l_del_warning.destroy()
        self.del_button.destroy()
        self.cancel_button.destroy()

        # Лейбл показывает статус сохранения и удаляется через 2,5 секунды
        l_info = Label(self.right_frame, width=20, text="Удалено".format(name))
        l_info.pack()
        self.root.after(2500, l_info.destroy)

        self.button_del_list.configure(state=NORMAL)

    # Сохранение списка
    def save_list(self):
        self.name_new_list = Label(self.right_frame, width=20, text="Название списка:")
        self.name_new_list.pack()

        self.entry_list_name = Entry(self.right_frame)
        self.entry_list_name.pack(anchor=N)

        self.save_button = Button(self.right_frame, text="Сохранить", command=self.save)
        self.save_button.pack(side=TOP, fill=X)

        self.cancel_button = Button(self.right_frame, text="Отмена", command=self.cancel)
        self.cancel_button.pack(side=TOP, fill=X)

    # Функция дополнительного вопроса
    def save(self):
        name = self.entry_list_name.get()
        if name:
            self.dict_lists.update({name:[*self.list_out.get(0, END)]})
            self.SAVE_FUNC(self.dict_lists)
            # with open("LISTS.json", "w") as f:
            #     self.dict_lists.update({name:[*self.list_out.get(0, END)]})
            #     f.write(json.dumps(self.dict_lists, ensure_ascii=False))

            # Лейбл показывает статус сохранения и удаляется через 2,5 секунды
            l_info = Label(self.right_frame, width=20, text="Список {}\nсохранён".format(name))
            l_info.pack()
            self.root.after(2500, l_info.destroy)

            self.read_lists()
            # Добавляем список
            self.Items.update({name: BooleanVar()})
            self.Items[name].set(0)
            _ = Checkbutton(self.left_frame, text=name, variable=self.Items[name], onvalue=1, offvalue=0)
            _.pack(anchor=W)
            # Назначаем объекту функцию, реагирующую на событие установки галочки
            self.Items[name].trace('w', self.items_tracer)

            # Удаление элементов диалога сохранения
            self.entry_list_name.destroy()
            self.save_button.destroy()
            self.name_new_list.destroy()
            self.cancel_button.destroy()

    def cancel(self):
        self.button_del_list.configure(state=NORMAL)
        self.button_save.configure(state=NORMAL)

        try:
            self.l_del_question.destroy()
            self.l_del_warning.destroy()
            self.del_button.destroy()
        except:
            pass

        try:
            self.entry_list_name.destroy()
            self.save_button.destroy()
            self.name_new_list.destroy()
        except:
            pass

        self.cancel_button.destroy()

    #######################################

    def make_func(self):
        label = Label(self.right_frame, width=20, text="Папка для сортировки:")
        label.pack()

        self.entry = Entry(self.right_frame)
        self.entry.pack(anchor=N)

        button = Button(self.right_frame, text="Сортировать", command=self.sort)
        button.pack(side=TOP, fill=X)

    def sort(self):
        print(self.Items)

        self.dirs = {}
        self.l = []

        for name in self.Items.keys():

            # print('Название папки :: ', name)
            # print('Значение галочки :: ', self.Items[name].get())
            # print('Значения :: ', self.dict_lists[name])


            self.l = [i for i in self.dict_lists[name]]
            print(self.l)

            if self.Items[name].get():
                self.dirs.update({name : self.l}) # self.dict_lists[name]})

            print(self.dirs)


        if self.entry.get():
            self.MAKE_FUNC(self.entry.get(),  self.dirs) #, self.lists)





