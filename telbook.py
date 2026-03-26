import tkinter as tk
from tkinter import ttk
import sqlite3

# Класс Главного окна
class Main(tk.Frame):

    # Создание инициализатора
    def __init__(self, root):
        
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    # Метод ля хранения и создания виджетов
    def init_main(self):

        # Создание панели инструментов
        toolbar = tk.Frame(bg = 'White', bd = 2)
        toolbar.pack(side = tk.TOP, fill = tk.X)

        # Создание кнопки добавления записи в таблицу
        self.add_img = tk.PhotoImage(file = 'D:\Programms_my\School_proj\img\Add.png' )
        btn_add = tk.Button(toolbar, text = 'Добавить', bg ='White',
                            bd = 0, image = self.add_img,
                            command = self.open_child)
        btn_add.pack(side = tk.LEFT)
    
        # Создание кнопки редактирования записи в таблице
        self.refr_img = tk.PhotoImage(file = 'D:/Programms_my/School_proj/img/Upd.png')
        btn_refr = tk.Button(toolbar, text = 'Редактировать', bg ='White',
                            bd = 0, image = self.refr_img,
                            command = self.open_update_child)
        btn_refr.pack(side = tk.LEFT)

        # Создание кнопки удаления записи в таблицы
        self.del_img = tk.PhotoImage(file = 'D:/Programms_my/School_proj/img/delete.png' )
        btn_del = tk.Button(toolbar, text = 'Удалить', bg ='White',
                            bd = 0, image = self.del_img,
                            command = self.delete_records)        
        btn_del.pack(side = tk.LEFT)

        # Создание кнопки обновления всех записей таблицы
        self.upd_img = tk.PhotoImage(file = 'D:/Programms_my/School_proj/img/refresh.png' )
        btn_upd = tk.Button(toolbar, text = 'Обновить', bg ='White',
                            bd = 0, image = self.upd_img,
                            command = self.refresh_records)        
        btn_upd.pack(side = tk.LEFT)

        # Создание кнопки поиска 
        self.search_img = tk.PhotoImage(file = 'D:/Programms_my/School_proj/img/search.png' )
        btn_search = tk.Button(toolbar, text = 'Поиск', bg ='White',
                            bd = 0, image = self.search_img,
                            command = self.open_search_child)        
        btn_search.pack(side = tk.LEFT)

        # Добавлление таблиц
        self.tree = ttk.Treeview(self, columns = ('ID', 'name', 'phone', 'email'),
                                 height = 45, show = 'headings')

        
        # Добавление параметров колонкам
        self.tree.column('ID', width = 30, anchor = tk.CENTER)
        self.tree.column('name', width = 300, anchor = tk.CENTER)
        self.tree.column('phone', width = 150, anchor = tk.CENTER)
        self.tree.column('email', width = 150, anchor = tk.CENTER)

        # Добавление записей колонкам
        self.tree.heading('ID', text = '№')
        self.tree.heading('name', text = 'Name')
        self.tree.heading('phone', text = 'Phone')
        self.tree.heading('email', text = 'Email')

        self.tree.pack(side = tk.LEFT)        

        # Создание ползунка для пролистывания таблицы
        scroll = tk.Scrollbar(self, command = self.tree.yview)
        scroll.pack(side = tk.LEFT, fill = tk.Y)
        self.tree.configure(yscrollcommand = scroll.set)
    
    # Запись данных в БД
    def records(self,name,phone,email,):

        self.db.insert_data(name,phone,email)
        self.view_records()

    # Сбор данных в TreeView
    def view_records(self):

        # Выбор информации из БД
        self.db.cur.execute('''SELECT * FROM Users''')

        # Удаление всего из виджета таблицы
        [self.tree.delete(i) for i in self.tree.get_children()]

        # Добавление в  таблицу всех данных из таблицы
        [self.tree.insert('','end',values = row)
         for row in self.db.cur.fetchall()]
        
    # Метод поиска данных по ФИО
    def search_records(self, name):

        name = ('%' + name + '%')

        # Выбор информации из БД
        self.db.cur.execute('''SELECT * FROM Users WHERE name LIKE ?''',(name,))

        # Удаление всего из виджета таблицы
        [self.tree.delete(i) for i in self.tree.get_children()]

        # Добавление в  таблицу всех данных из таблицы
        [self.tree.insert('','end',values = row)
         for row in self.db.cur.fetchall()]
    
    # Метод изменения данных
    def update_record(self,name,phone,email):

        select_record_id = self.tree.set(self.tree.selection()[0],'#1')
        self.db.cur.execute('''UPDATE Users SET name = ?, phone = ?, email = ? WHERE ID = ?''',
                            (name,phone,email,select_record_id))
        
        self.db.conn.commit()
        self.view_records()

    # Метод удаления данных
    def delete_records(self):

        for row in self.tree.selection():

            self.db.cur.execute('''DELETE FROM Users WHERE ID = ?''',
                                (self.tree.set(row,'#1'), ))
            
        self.db.conn.commit()
        self.view_records()

    # Метод обновления все телефонной книги
    def refresh_records(self):
        self.view_records()

    # Метод по вызову дочернего класса
    def open_child(self):

        Child()
    
    # Метод по вызову класса кнопки редактирования
    def open_update_child(self):

        Update()

    # Метод по вызову класса кнопки поиска 
    def open_search_child(self):

        Search()
        
# Класс дочернего окна

class Child(tk.Toplevel):

    # Создание инициализатора
    def __init__(self):

        super().__init__(root)
        self.init_child()
        self.view = app

    # Метод создания и хранения виджетов дочернего окна
    def init_child(self):

        self.title('Добавить контакт')
        self.geometry('400x200')
        self.resizable(False,False)

        # Перехват всех событий происходящих в приложении
        self.grab_set()

        # Захват фокуса
        self.focus_set()

        # Создание строк

        label_name = tk.Label(self, text = 'ФИО: ')
        label_name.place(x = 50,y = 15) 

        label_phone = tk.Label(self, text = 'Телефон: ')
        label_phone.place(x = 50,y = 55)         

        label_email = tk.Label(self, text = 'E-mail: ')
        label_email.place(x = 50,y = 95)

        # Создание полей ввода

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x = 200,y = 15)

        self.entry_phone = ttk.Entry(self)
        self.entry_phone.place(x = 200,y = 55)

        self.entry_email = ttk.Entry(self)
        self.entry_email.place(x = 200,y = 95)   

        # Кнопка закрытия дочернего окна
        self.btn_cancel = ttk.Button(self, text = 'Закрыть', command = self.destroy)
        self.btn_cancel.place(x = 300,y = 170)

        # Кнопка добавления записи
        self.btn_add1 = ttk.Button(self, text = 'Добавить')
        self.btn_add1.place(x = 220,y = 170)
        self.btn_add1.bind('<Button-1>', lambda event: 
                             self.view.records(self.entry_name.get(),
                                               self.entry_phone.get(),
                                               self.entry_email.get()))

# Класс кнопки редактирования

class Update(Child):

    # Создание инициализатора
    def __init__(self):

        super().__init__()
        self.init_update()
        self.db = db
        self.default_data()

    # Метод редактирования данных
    def init_update(self):

        self.title('Редактировать позицию')
        self.btn_add1.destroy()
        
        self.btn_update = ttk.Button(self, text = 'Редактировать')
        self.btn_update.place(x = 200,y=170)
        self.btn_update.bind('<Button-1>', lambda event: 
                             self.view.update_record(self.entry_name.get(),
                                                    self.entry_phone.get(),
                                                    self.entry_email.get()))
        
        self.btn_update.bind('<Button-1>', lambda event: self.destroy(), add = '+')
        self.btn_update.place(x = 200,y = 170)

    # Метод по выборке всех данных из таблицы с определённым id для выведения этих данных в строке ввода
    def default_data(self):

        select_record_id = self.view.tree.set(self.view.tree.selection()[0],'#1')
        self.db.cur.execute('''SELECT * FROM Users WHERE id = ?''',(select_record_id))

        # Получение доступа к первой записи выборки
        row = self.db.cur.fetchone()
        self.entry_name.insert(0, row[1])
        self.entry_phone.insert(0, row[2])
        self.entry_email.insert(0, row[3])

# Класс поиска записей

class Search(tk.Toplevel):

    # Создание инициализатора
    def __init__(self):

        super().__init__(root)
        self.init_search()
        self.view = app

    # Метод поиска данных 
    def init_search(self):

        self.title('Поиск контакта')
        self.geometry('300x130')
        self.resizable(False,False)

        # Перехват всех событий происходящих в приложении
        self.grab_set()

        # Захват фокуса
        self.focus_set()     
        
        # Создание строки
        label_name = tk.Label(self, text = 'ФИО: ')
        label_name.place(x = 50,y = 50)

        # Создание поля ввода
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x = 135,y = 50)

        # Кнопка закрытия дочернего окна
        self.btn_cancel = ttk.Button(self, text = 'Закрыть', command = self.destroy)
        self.btn_cancel.place(x = 200,y = 80)

        # Кнопка поиска записи
        self.btn_search = ttk.Button(self, text = 'Найти')
        self.btn_search.place(x = 120,y = 80)
        self.btn_search.bind('<Button-1>', lambda event: 
                             self.view.search_records(self.entry_name.get()))   

# Класс базы данных

class DB:

    # Создание инициализатора
    def __init__(self):

        self.conn = sqlite3.connect('Contacts.db')

        self.cur = self.conn.cursor()

        # Создание таблицы
        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS Users(
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            phone TEXT,
                            email  TEXT)
                            ''')
    
    # Метод по заполнению таблицы        
    def insert_data(self,name,phone,email):

        self.cur.execute('''INSERT INTO Users(name,phone,email)
                         VALUES(?,?,?)''',(name,phone,email) )
        
        self.conn.commit()  

# Запуск программы только при запуске программы из этого файла 
if __name__ == '__main__':

    db = DB()

    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('Телефонная книга')
    root.geometry('645x450')
    root.configure(bg = '#d7d7d7')
    root.resizable(False,False)

    root.mainloop()