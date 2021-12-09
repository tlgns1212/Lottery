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

# 레이블
label1 = Label(root, text="Hi~ 안녕하세요~")
label1.pack()

# 레이블에 이미지 넣가
# photo = PhotoImage(file="파일경로")
# label2 = Label(root,image=photo)
# label2.pack()


def change():
    label1.config(text="한국에 오신걸 환영합니다.")

btn = Button(root, text = "클릭", command = change)
btn.pack()

#-----------------------------------------------------------




root.mainloop()