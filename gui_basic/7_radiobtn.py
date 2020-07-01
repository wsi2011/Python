from tkinter import *

root = Tk()
root.title('Nado GUI')
root.geometry('640x480') # 가로,세로


Label(root,text='메뉴를 선택하세요').pack()

var = IntVar()
btn_burger1 = Radiobutton(root,text='햄버거',value=1,variable=var)
btn_burger1.select()
btn_burger2 = Radiobutton(root,text='치즈버거',value=2,variable=var)
btn_burger3 = Radiobutton(root,text='치킨버거',value=3,variable=var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

var2 = StringVar()
btn_drink1 = Radiobutton(root,text='콜라',value='콜라',variable=var2)
btn_drink1.select()
btn_drink2 = Radiobutton(root,text='사이다',value='사이다',variable=var2)
btn_drink3 = Radiobutton(root,text='포카리',value='포카리',variable=var2)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
   print(var.get())
   print(var2.get())
   
btn = Button(root,text='클릭',command=btncmd)
btn.pack()


root.mainloop()