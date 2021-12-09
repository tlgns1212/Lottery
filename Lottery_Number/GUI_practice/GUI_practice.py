#-----------------------------------------------------------

from tkinter import *

root = Tk()
root.title("GUI test")

# 가로 * 세로
# root.geometry("540x380")

# 가로 * 세로 + x축 이동 + y축 이동
root.geometry("540x380+200+100")

# x축, y축 크기 조정
root.resizable(True,True) # 기본 설정이 True, True임

#-----------------------------------------------------------
# 버튼 추가(위치, 텍스트)
btn1 = Button(root, text="버튼1")
btn1.pack()

# 버튼 추가(위치, x축 크기(가변), y축 크기(가변), 텍스트)
btn2 = Button(root, padx = 10, pady = 10, text = "버튼2")
btn2.pack()

# 버튼 추가(위치, x축 크기(고정), y축 크기(고정), 텍스트)
btn3 = Button(root, width = 10, height = 10, text = "버튼3")
btn3.pack()

# 버튼 추가(위치, foreground 글자색, background 배경색, 텍스트)
btn4 = Button(root, fg = "green", bg = "yellow", text = "버튼4")
btn4.pack()

# 버튼의 텍스트 대신 사진
#photo1 = PhotoImage(file = "파일경로")
#btn5 = Button(root, image=photo)
#btn5.pack()

def btncmd():
    print("버튼이 클릭되었습니다!")

btn5 = Button(root, text = "동작하는 버튼", command = btncmd)
btn5.pack()

#-----------------------------------------------------------




root.mainloop()