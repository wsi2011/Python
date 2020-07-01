from tkinter import *

root = Tk()
root.title('Nado GUI')
root.geometry('640x480') # 가로,세로

checkvar = IntVar() 
checkbox = Checkbutton(root,text='오늘 하루 보지 않기',variable=checkvar)
checkbox.pack()

checkvar2 = IntVar()
checkbox2 = Checkbutton(root,text='일주일 동안 보지 않기',variable=checkvar2)
checkbox2.pack()


def btncmd():
   print(checkvar.get())
   print(checkvar2.get())
   
btn = Button(root,text='클릭',command=btncmd)
btn.pack()


root.mainloop()