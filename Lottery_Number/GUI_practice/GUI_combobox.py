#-----------------------------------------------------------

from tkinter import *
import tkinter.ttk as ttk


root = Tk()
root.title("GUI test")

# 가로 * 세로
# root.geometry("540x380")

# 가로 * 세로 + x축 이동 + y축 이동
root.geometry("640x480+200+100")

# x축, y축 크기 조정
root.resizable(True,True) # 기본 설정이 True, True임

#-----------------------------------------------------------
# 1 ~ 31까지의 숫자
# values = [i for i in range(1,32)]
value1 = [str(i) + "일" for i in range(1,32)]

# 콤보 박스에 값이 입력될 수 있음
combobox = ttk.Combobox(root, height=5, values=value1)
combobox.pack()
combobox.set("카드 결제일")

# 읽기 전용 콤보박스
readonly_combobox = ttk.Combobox(root, height=10, values=value1, state="readonly")
readonly_combobox.current(0)
readonly_combobox.pack()
readonly_combobox.set("읽기 전용")

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

button1 = Button(root, text="Order", command=btncmd)
button1.pack()


#-----------------------------------------------------------




root.mainloop()