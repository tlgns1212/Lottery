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

# 메뉴 바
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File")
menu.add_cascade(label="File",menu=menu_file)
root.config(menu=menu)

#-----------------------------------------------------------




root.mainloop()