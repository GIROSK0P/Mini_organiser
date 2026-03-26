import tkinter as tk
from tkinter import ttk
import time
import os
import winsound

def iof(a): 
    a = float(a)
    if a-(round(a,0))==0:
        a = int(a)
        return a
    else:
        a = float(a)
        return a

class Main(tk.Frame):

    def __init__(self,root):

        super().__init__(root)
        self.init_main()
        self.h = 0

    def init_main(self):

        self.label_h = tk.Label(text = 'Часы',bg ='White',font=['arial','13'])
        self.label_h.place(x=40,y=40)

        self.label_m = tk.Label(text = 'Минуты',bg ='White',font=['arial','13'])
        self.label_m.place(x=40,y=80)

        self.label_s = tk.Label(text = 'Секунды',bg ='White',font=['arial','13'])
        self.label_s.place(x=40,y=120)

        self.entry_h = ttk.Entry()
        self.entry_h.place(x = 200,y = 40)
        self.entry_h.insert(tk.END,0)

        self.entry_m = ttk.Entry()
        self.entry_m.place(x = 200,y = 80)
        self.entry_m.insert(tk.END,0)

        self.entry_s = ttk.Entry()
        self.entry_s.place(x = 200,y = 120)
        self.entry_s.insert(tk.END,0)
        
        # H

        self.btn_plh_img = tk.PhotoImage(file = 'D:\Programms_my\School_proj\img\Triangle.png' )
        self.btn_plh = tk.Button(image=self.btn_plh_img, bg ='White',font=['arial','26'],width=16,
                            bd = 0,command=self.plh)
        self.btn_plh.place(x=180,y=40)

        self.btn_minh_img = tk.PhotoImage(file = 'D:\Programms_my\School_proj\img\Triangle_down.png' )
        self.btn_minh = tk.Button(image=self.btn_minh_img, bg ='White',font=['arial','26'],width=16,
                            bd = 0,command=self.minh)
        self.btn_minh.place(x=328,y=40)

        # M

        self.btn_plm = tk.Button(image=self.btn_plh_img, bg ='White',font=['arial','26'],width=16,
                            bd = 0,command=self.plm)
        self.btn_plm.place(x=180,y=80)

        self.btn_minm = tk.Button(image=self.btn_minh_img, bg ='White',font=['arial','26'],width=16,
                            bd = 0,command=self.minm)
        self.btn_minm.place(x=328,y=80)

        # S

        self.btn_pls = tk.Button(image=self.btn_plh_img, bg ='White',font=['arial','26'],width=16,
                            bd = 0,command=self.pls)
        self.btn_pls.place(x=180,y=120) 

        self.btn_mins = tk.Button(image=self.btn_minh_img, bg ='White',font=['arial','26'],width=16,
                            bd = 0,command=self.mins)
        self.btn_mins.place(x=328,y=120)

        #

        self.start_img = tk.PhotoImage(file = 'D:\Programms_my\School_proj\img\Triangle-right.png' )
        self.btn_start = tk.Button(image=self.start_img, bg ='White',width=24,
                            bd = 0,command=self.start)
        self.btn_start.place(x=230,y=160)

        self.stop_img = tk.PhotoImage(file = 'D:\Programms_my\School_proj\img\Stop.png' )
        self.btn_stop = tk.Button(image=self.stop_img, bg ='White',width=24,
                            bd = 0,command=self.stop)
        self.btn_stop.place(x=270,y=160)

    # H
           
    def plh(self):
        
        pred_zn_h = iof(self.entry_h.get())
        self.entry_h.delete(0, tk.END)
        if pred_zn_h+1<=24:
            self.entry_h.insert(tk.END,pred_zn_h+1)
        else:
            self.entry_h.insert(tk.END,24)

    def minh(self):

        pred_zn_h = iof(self.entry_h.get())
        self.entry_h.delete(0, tk.END)
        if pred_zn_h-1>=0:
            self.entry_h.insert(tk.END,pred_zn_h-1)
        else:
            self.entry_h.insert(tk.END,0)

    # M

    def plm(self):
        
        pred_zn_m = iof(self.entry_m.get())
        self.entry_m.delete(0, tk.END)
        if pred_zn_m+1 <= 60:
            self.entry_m.insert(tk.END,pred_zn_m+1)
        else:
            self.entry_m.insert(tk.END,60)

    def minm(self):

        pred_zn_m = iof(self.entry_m.get())
        self.entry_m.delete(0, tk.END)
        if pred_zn_m-1>=0:
            self.entry_m.insert(tk.END,pred_zn_m-1)
        else:
            self.entry_m.insert(tk.END,0)

    # S

    def pls(self):
        
        pred_zn_s = iof(self.entry_s.get())
        self.entry_s.delete(0, tk.END)
        if pred_zn_s+1<=60:
            self.entry_s.insert(tk.END,pred_zn_s+1)
        else:
            self.entry_s.insert(tk.END,60)

    def mins(self):

        pred_zn_s = iof(self.entry_s.get())
        self.entry_s.delete(0, tk.END)
        if pred_zn_s-1>=0:
            self.entry_s.insert(tk.END,pred_zn_s-1)
        else:
            self.entry_s.insert(tk.END,0)

    def start(self):
        
        self.hours = int(self.entry_h.get())
        self.min = int(self.entry_m.get())
        self.sec = int(self.entry_s.get())

        
        self.label_t = tk.Label(text = f'{self.hours}:{self.min}:{self.sec}',bg ='White',font=['arial','20'])
        self.label_t.place(x=150,y=300)

        self.total_sec = self.hours * 3600 + self.min * 60 + self.sec

        while self.total_sec >= 0  :
            
            self.hours = self.total_sec // 3600
            self.min = (self.total_sec % 3600) // 60
            self.sec = self.total_sec % 60

            self.label_t = tk.Label(text = f'{self.hours}:{self.min}:{self.sec}',bg ='White',font=['arial','20'])
            self.label_t.place(x=150,y=300)
            self.label_t.update()
        
            time.sleep(1)
        
            self.total_sec -= 1
        
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
        self.label_t = tk.Label(text = 'Время вышло!',bg ='White',font=['arial','20'])
        self.label_t.place(x=130,y=300) 
        self.label_t.update()
        time.sleep(1)        
        root.destroy()
        os.system('C:/Users/Ноут/AppData/Local/Programs/Python/Python311/python.exe D:/Programms_my/School_proj/timer.py')

    
    def stop(self):
        
        root.destroy()
        os.system('C:/Users/Ноут/AppData/Local/Programs/Python/Python311/python.exe D:/Programms_my/School_proj/timer.py')




if __name__ == '__main__':

    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('Таймер')
    root.geometry('400x400')
    root.configure(bg = 'White')
    root.resizable(False,False)

    root.mainloop()