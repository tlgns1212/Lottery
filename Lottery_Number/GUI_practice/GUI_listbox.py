#-----------------------------------------------------------

from tkinter import *

root = Tk()
root.title("GUI test")

# 가로 * 세로
# root.geometry("540x380")

# 가로 * 세로 + x축 이동 + y축 이동
root.geometry("640x480+200+100")

# x축, y축 크기 조정
root.resizable(True,True) # 기본 설정이 True, True임

#-----------------------------------------------------------
# 목록
listbox1 = Listbox(root, selectmode="extended", height=0)

# 목록에 값을 넣어줄때
listbox1.insert(0,"대한민국")
listbox1.insert(1,"Germany")
listbox1.insert(2,"America")
# 숫자는 순서, END는 순서 상관없이
listbox1.insert(END,"Australia")
listbox1.insert(END,"New Zealand")
listbox1.pack()

def btncmd():
    # 목록 END(끝)에서부터 지우기, 0(시작)에서부터 지우기
    # listbox1.delete(END)

    # 목록 개수 세기
    # print(listbox1.size())

    # 항목 가져오기
    # print(listbox1.get(0,END))

    # 선택된 항목
    print(listbox1.curselection())

btn = Button(root, text="Click", command=btncmd)
btn.pack()

#-----------------------------------------------------------




root.mainloop()