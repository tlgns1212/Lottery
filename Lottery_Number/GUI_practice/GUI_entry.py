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
# 텍스트 (위치, 가로, 세로)
txt1 = Text(root, width=30, height=30)
# 텍스트 초기값 설정
txt1.insert(END, "글자를 입력하세요")
txt1.pack()


# 한줄 입력만 되는 엔트리 사용
ent1 = Entry(root, width=30)
ent1.pack()
ent1.insert(0, "한 줄만 입력됩니다!")

def btncmd1():
    # 텍스트와 엔트리의 내용 출력
    print(txt1.get("1.0",END))
    print(ent1.get())
btn1 = Button(root, text="Click", command=btncmd1)
btn1.pack()

#-----------------------------------------------------------




root.mainloop()