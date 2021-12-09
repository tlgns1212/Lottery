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

# 체크박스 생성
chkclick = IntVar()
chkbox = Checkbutton(root, text="오늘 할 ㅜ그만 보기", variable=chkclick)
chkbox.pack()

chkclick1 = IntVar()
chkbox1 = Checkbutton(root, text="1주일 동안 보지 않기",variable=chkclick1)
chkbox1.pack()

# 체크박스 체크 초기값으로 설정
chkbox.select()

# 체크박스 체크 해제 초기값으로 설정
chkbox1.deselect()

def btncmd():
    print(chkclick.get())
    print(chkclick1.get())

btn = Button(root, text="Click",command = btncmd)
btn.pack()

#-----------------------------------------------------------




root.mainloop()