import tkinter as tk
from tkinter import ttk

def iof(a): 
    a = float(a)
    if a%round(a,0)==0:
        a = int(a)
        return a
    else:
        a = float(a)
        return a

class Main(tk.Frame):

    def __init__(self,root):
           
        super().__init__(root)
        self.init_main()
        self.deist = {'plus': self.plusravn,'min':self.minravn,'umn':self.umnravn,'divis':self.divisravn,'degree':self.degreeravn}

    def init_main(self):
 
        
        self.entry_text = tk.Entry(self,relief = 'ridge',borderwidth = 10,width=34,bg = '#006400',fg='white',justify='right',insertbackground='white',font="Arial 11")
        self.entry_text.grid(row = 0, column = 0, columnspan=3, sticky='ew',ipady=7)


        # Создание панели инструментов
        toolb = tk.Frame(bg = 'White', bd =2)
        toolb.pack(side = tk.BOTTOM, fill = tk.X)

        toolb1 = tk.Frame(bg = 'White', bd = 2)
        toolb1.pack(side = tk.BOTTOM, fill = tk.X)

        toolb2 = tk.Frame(bg = 'White', bd = 2)
        toolb2.pack(side = tk.BOTTOM, fill = tk.X)

        toolb3 = tk.Frame(bg = 'White', bd = 2)
        toolb3.pack(side = tk.BOTTOM, fill = tk.X)

        toolb4 = tk.Frame(bg = 'White', bd = 2)
        toolb4.pack(side = tk.BOTTOM, fill = tk.X)

        toolb5 = tk.Frame(bg = 'White', bd = 2)
        toolb5.pack(side = tk.RIGHT)


        
#####################################################################

        self.btn_pl_min = tk.Button(toolb, text = '+/-', bg ='White',font=['arial','26'],width=5,
                            bd = 0,command=self.plmin)
        self.btn_pl_min.pack(side = tk.LEFT)

        self.btn_0 = tk.Button(toolb, text = '0', bg ='White',font=['arial','26'],width=5,
                            bd = 0, command=self.enter_0)
        self.btn_0.pack(side = tk.LEFT)

        self.btn_toch = tk.Button(toolb, text = '.', bg ='White',font=['arial','26'],width=5,
                            bd = 0,command=self.enter_toch)
        self.btn_toch.pack(side = tk.LEFT)

        self.btn_ravn = tk.Button(toolb, text = '=', bg ='Blue',font=['arial','26'],width=5,
                            bd = 0,command = self.ravn)
        self.btn_ravn.pack(side = tk.LEFT)

#######################################################################
    
        # Создание кнопки редактирования записи в таблице
        self.btn_1 = tk.Button(toolb1, text = '1', bg ='White',font=['arial','26'],width=5,
                            bd = 0, command=self.enter_1)
        self.btn_1.pack(side = tk.LEFT)
        # Создание кнопки редактирования записи в таблице
        self.btn_2 = tk.Button(toolb1, text = '2', bg ='White',font=['arial','26'],width=5,
                            bd = 0, command=self.enter_2)
        self.btn_2.pack(side = tk.LEFT)
        # Создание кнопки редактирования записи в таблице
        self.btn_3 = tk.Button(toolb1, text = '3', bg ='White',font=['arial','26'],width=5,
                            bd = 0, command=self.enter_3)
        self.btn_3.pack(side = tk.LEFT)
        # Создание кнопки редактирования записи в таблице
        self.btn_pl = tk.Button(toolb1, text = '+', bg ='#d7d7d7',font=['arial','26'],width=5,
                            bd = 0,command = self.plus)
        self.btn_pl.pack(side = tk.LEFT)

#########################################################################

        # Создание кнопки редактирования записи в таблице
        self.btn_4 = tk.Button(toolb2, text = '4', bg ='White',font=['arial','26'],width=5,
                            bd = 0, command=self.enter_4)
        self.btn_4.pack(side = tk.LEFT)
        # Создание кнопки редактирования записи в таблице
        self.btn_5 = tk.Button(toolb2, text = '5', bg ='White',font=['arial','26'],width=5,
                            bd = 0, command=self.enter_5)
        self.btn_5.pack(side = tk.LEFT)
        # Создание кнопки редактирования записи в таблице
        self.btn_6 = tk.Button(toolb2, text = '6', bg ='White',font=['arial','26'],width=5,
                            bd = 0, command=self.enter_6)
        self.btn_6.pack(side = tk.LEFT)
        # Создание кнопки редактирования записи в таблице
        self.btn_min = tk.Button(toolb2, text = '-', bg ='#d7d7d7',font=['arial','26'],width=5,
                            bd = 0,command=self.min)
        self.btn_min.pack(side = tk.LEFT)

##########################################################################

        # Создание кнопки редактирования записи в таблице
        self.btn_7 = tk.Button(toolb3, text = '7', bg ='White',font=['arial','26'],width=5,
                            bd = 0, command=self.enter_7)
        self.btn_7.pack(side = tk.LEFT)
        # Создание кнопки редактирования записи в таблице
        self.btn_8 = tk.Button(toolb3, text = '8', bg ='White',font=['arial','26'],width=5,
                            bd = 0, command=self.enter_8)
        self.btn_8.pack(side = tk.LEFT)
        # Создание кнопки редактирования записи в таблице
        self.btn_9 = tk.Button(toolb3, text = '9', bg ='White',font=['arial','26'],width=5,
                            bd = 0, command=self.enter_9)
        self.btn_9.pack(side = tk.LEFT)
        # Создание кнопки редактирования записи в таблице
        self.btn_umn = tk.Button(toolb3, text = '×', bg ='#d7d7d7',font=['arial','26'],width=5,
                            bd = 0,command=self.umn)
        self.btn_umn.pack(side = tk.LEFT)

###############################################################################

        # Создание кнопки редактирования записи в таблице
        self.btn_kor = tk.Button(toolb4, text = '√', bg ='White',font=['arial','26'],width=5,
                            bd = 0, command=self.sqrt)
        self.btn_kor.pack(side = tk.LEFT)
        # Создание кнопки редактирования записи в таблице
        btn_step = tk.Button(toolb4, text = 'x^y', bg ='White',font=['arial','26'],width=5,
                            bd = 0,command=self.degree)
        btn_step.pack(side = tk.LEFT)
        # Создание кнопки редактирования записи в таблице
        self.btn_C = tk.Button(toolb4, text = 'C', bg ='White',font=['arial','26'],width=5,
                            bd = 0,command=self.C)
        self.btn_C.pack(side = tk.LEFT)
        # Создание кнопки редактирования записи в таблице
        self.btn_divis = tk.Button(toolb4, text = '÷', bg ='#d7d7d7',font=['arial','26'],width=5,
                            bd = 0, command=self.division)
        self.btn_divis.pack(side = tk.LEFT)

##################################################################################

        self.btn_C1 = tk.Button(toolb5, text = '⌫', bg ='#d7d7d7',font=['arial','25'],width=5,
                            bd = 0,command=self.C1)
        self.btn_C1.pack(side = tk.LEFT)

    def enter_1(self):        
        
        self.entry_text.insert(tk.END,self.btn_1.cget('text'))

    def enter_2(self):        
        
        self.entry_text.insert(tk.END,self.btn_2.cget('text'))

    def enter_3(self):        
        
        self.entry_text.insert(tk.END,self.btn_3.cget('text'))

    def enter_4(self):        
        
        self.entry_text.insert(tk.END,self.btn_4.cget('text'))

    def enter_5(self):        
        
        self.entry_text.insert(tk.END,self.btn_5.cget('text'))

    def enter_6(self):        
        
        self.entry_text.insert(tk.END,self.btn_6.cget('text'))

    def enter_7(self):        
        
        self.entry_text.insert(tk.END,self.btn_7.cget('text'))

    def enter_8(self):        
        
        self.entry_text.insert(tk.END,self.btn_8.cget('text'))

    def enter_9(self):        
        
        self.entry_text.insert(tk.END,self.btn_9.cget('text'))

    def enter_0(self):        
        
        self.entry_text.insert(tk.END,self.btn_0.cget('text'))

    def enter_toch(self):        
        
        self.entry_text.insert(tk.END,self.btn_toch.cget('text'))

    def plus(self):

        self.ch1 = iof(self.entry_text.get())
        self.entry_text.delete(0, tk.END)
        self.key = 'plus'

    def min(self):

        self.ch1 = iof(self.entry_text.get())
        self.entry_text.delete(0, tk.END)
        self.key = 'min'

    def umn(self):

        self.ch1 = iof(self.entry_text.get())
        self.entry_text.delete(0, tk.END)
        self.key = 'umn'

    def division(self):

        self.ch1 = iof(self.entry_text.get())
        self.entry_text.delete(0, tk.END)
        self.key = 'divis'
    
    def sqrt(self):

        self.ch1 = iof(self.entry_text.get())
        self.entry_text.delete(0, tk.END)
        self.entry_text.insert(0, self.ch1**0.5)
    
    def degree(self):

        self.ch1 = iof(self.entry_text.get())
        self.entry_text.delete(0, tk.END)
        self.key = 'degree'


    def plusravn(self,ch1,ch2):

        otvet = ch1+ch2
        return otvet

    def minravn(self,ch1,ch2):

        otvet = ch1-ch2
        return otvet

    def umnravn(self,ch1,ch2):

        otvet = ch1*ch2
        return otvet

    def divisravn(self,ch1,ch2):

        otvet = ch1/ch2
        return otvet
    
    def degreeravn(self,ch1,ch2):
        
        return ch1**ch2

    
    def ravn(self):

        self.ch2 = iof(self.entry_text.get())
        self.entry_text.delete(0, tk.END)
        self.otwet = self.deist[self.key](ch1=self.ch1,ch2=self.ch2)
        self.entry_text.insert(0, self.otwet)

    def C(self):

        self.entry_text.delete(0, tk.END)
        self.ch1 = 0
    
    def C1(self):

        self.entry_text.delete(len(self.entry_text.get()) - 1)

    def plmin(self):
        
        self.ch = iof(self.entry_text.get())
        self.ch *= -1
        self.entry_text.delete(0,tk.END)
        self.entry_text.insert(0, str(self.ch))

if __name__ == '__main__':
    root_g = tk.Tk()
    app = Main(root_g)
    app.pack()
    root_g.title('Калькулятор')
    root_g.geometry('400x400')
    root_g.configure(bg = '#d7d7d7')
    root_g.resizable(False,False)

    root_g.mainloop()