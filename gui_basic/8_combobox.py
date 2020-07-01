import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title('Nado GUI')
root.geometry('640x480') # 가로,세로

values = [str(i) + '월' for i in range(1,32)]
combobox = ttk.Combobox(root,height=5,values=values)
combobox.pack()
combobox.set('카드 결제일')

combobox2 = ttk.Combobox(root,height=10,values=values,state='readonly')
combobox2.current(0)
combobox2.pack()


def btncmd():
    print(combobox.get())
     print(combobox2.get())
   
btn = Button(root,text='선택',command=btncmd)
btn.pack()


root.mainloop()