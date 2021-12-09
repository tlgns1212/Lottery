#-----------------------------------------------------------

from tkinter import *
import tkinter.ttk as ttk
import time


root = Tk()
root.title("GUI test")

# 가로 * 세로
# root.geometry("540x380")

# 가로 * 세로 + x축 이동 + y축 이동
root.geometry("640x480+200+100")

# x축, y축 크기 조정
root.resizable(True,True) # 기본 설정이 True, True임

#-----------------------------------------------------------

# # 프로그레스 바 (다운로드 바)
# # indeterminate / determinate
# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")

# # start(10) == 10ms
# progressbar.start(10)

# # 멈추길 바라면
# # progressbar.stop()

# progressbar.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd1():
    for i in range(1,101):
        time.sleep(0.01)    # 0.01초 대기

        p_var2.set(i)
        progressbar2.update()

        print(p_var2.get())

btn = Button(root, text="전송", command=btncmd1)
btn.pack()

#-----------------------------------------------------------




root.mainloop()