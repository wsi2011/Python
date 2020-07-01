from tkinter import *
import tkinter.messagebox as mesbox

#######################################
root = Tk()
root.title('Nado GUI')
root.geometry('640x480') # 가로,세로
########################################

# 기차 예매 시스템
def info():
    mesbox.showinfo('알림','정상적으로 예매 완료되었습니다.')


def warn():
    mesbox.showwarning('경고','해당 좌석은 매진되었습니다.')

def error():
    mesbox.showerror('에러','결제 오류 발생!')

def okcancel():
    mesbox.askokcancel('확인/취소','해당 좌석은 유아 동반석입니다. 예매하시겠습니다까?')

def retrycancel():
    mesbox.askretrycancel('재시도.취소','일시적인 오류 입니다. 다시 시도 하시겠습니다까?')

Button(root,command=info,text='알림').pack()
Button(root,command=warn,text='경고').pack()
Button(root,command=error,text='에러').pack()
Button(root,command=okcancel,text='확인 취소').pack()
Button(root,command=retrycancel,text='재시도 취소').pack()




root.mainloop()