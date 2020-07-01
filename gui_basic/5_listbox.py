from tkinter import *

root = Tk()
root.title('Nado GUI')
root.geometry('640x480') # 가로,세로
#root.geometry('640x480+300+100') # 가로 * 세로 + x 좌표 + y 좌표

listbox = Listbox(root,selectmod='extended',height=0)
listbox.insert(0,'사과')
listbox.insert(1,'딸기')
listbox.insert(2,'바나나')
listbox.insert(END,'수박')
listbox.insert(END,'포도')
listbox.pack()

def btncmd():
    # 삭제
    #listbox.delete(END)
    #listbox.delete(0)
   
    # 갯수 확인
    #print('리스트에는',listbox.size())

    # 항목 확인
    #print('항목 확인', listbox.get(0,END))

    # 선택된 항목 확인 (위치(index번호)로 반환 ex (1,2,3))
    print('선택된 항목:',listbox.curselection())

btn = Button(root,text='클릭',command=btncmd)
btn.pack()


root.mainloop()