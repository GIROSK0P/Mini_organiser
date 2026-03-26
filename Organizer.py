import tkinter as tk
from tkinter import ttk
import subprocess




class General(tk.Frame):

    def __init__(self,root):

        super().__init__(root)
        self.init_general()

    def main_k(self):
        
        subprocess.call(["D:\Programms_my\School_proj\output\calc.exe"])

    def main_tel(self):
        
        subprocess.call(["D:/Programms_my/School_proj/output/telbook.exe"])
    
    def main_timer(self):

        subprocess.call(["D:/Programms_my/School_proj/output/timer.exe"])

    def init_general(self):        
    
        toolb3 = tk.Frame(bg = 'White', bd = 2)
        toolb3.pack(side = tk.TOP, fill = tk.X)

        toolb4 = tk.Frame(bg = 'White', bd = 2)
        toolb4.pack(side = tk.TOP, fill = tk.X)

        toolb5 = tk.Frame(bg = 'White', bd = 2)
        toolb5.pack(side = tk.TOP, fill = tk.X)

        self.k_img = tk.PhotoImage(file = 'D:\Programms_my\School_proj\img\k.png' )
        self.button_k = tk.Button(toolb3,image = self.k_img, bg ='White',width=75,
                            bd = 0, command=self.main_k)
        self.button_k.pack(side=tk.LEFT)

        self.tel_img = tk.PhotoImage(file = 'D:/Programms_my/School_proj/img/tel.png' )
        self.button_tel = tk.Button(toolb3,image=self.tel_img, bg ='White',
                            bd = 0, command=self.main_tel)
        self.button_tel.pack(side=tk.LEFT)

        self.label_k = tk.Label(toolb4, text = 'Калькулятор',bg ='White',font=['TkDefaultFont','8'])
        self.label_k.pack(side=tk.LEFT)
    
        self.label_tel = tk.Label(toolb4, text = 'Телефонная',bg ='White',font=['TkDefaultFont','9'])
        self.label_tel.pack(side=tk.LEFT)

        self.label_k1 =tk.Label(toolb5, text = ' ',bg ='White',width=12)
        self.label_k1.pack(side=tk.LEFT)

        self.label_tel1 = tk.Label(toolb5, text = 'Книга',bg ='White')
        self.label_tel1.pack(side=tk.LEFT)

        self.btn_tim_img = tk.PhotoImage(file='D:\Programms_my\School_proj\img\Timer.png')
        self.btn_tim = tk.Button(toolb3,image=self.btn_tim_img, bg ='White',
                            bd = 0, command=self.main_timer)
        self.btn_tim.pack(side=tk.LEFT)

        self.label_tel = tk.Label(toolb4, text = 'Таймер',bg ='White')
        self.label_tel.pack(side=tk.LEFT)

if __name__ == '__main__':

    root_k = tk.Tk()
    app = General(root_k)
    app.pack()
    root_k.title('Органайзер')
    root_k.geometry('400x400')
    root_k.configure(bg = 'White')
    root_k.resizable(False,False)

    root_k.mainloop()

    
