import time
import tkinter.ttk as ttk
from tkinter import *

#######################################
root = Tk()
root.title('Nado GUI')
root.geometry('640x480') # 가로,세로
########################################

# pb = ttk.Progressbar(root,maximum=100,mode='indeterminate')
# pb.start(10) # 10ms 마다 움직임
# pb.pack()

# pb2 = ttk.Progressbar(root,maximum=100,mode='determinate')
# pb2.start(10) # 10ms 마다 움직임
# pb2.pack()


p_var = DoubleVar()
pb = ttk.Progressbar(root,maximum=100,length=150,variable=p_var)
pb.pack()


def btncmd():
    # pb.stop()
    # pb2.stop()
    for i in range(1,101):
        time.sleep(0.01) # 0.01 초 대기
        p_var.set(i)
        pb.update()

btn = Button(root,text='시작',command=btncmd)
btn.pack()


root.mainloop()