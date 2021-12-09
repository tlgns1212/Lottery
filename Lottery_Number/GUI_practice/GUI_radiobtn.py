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
label1 = Label(root, text="햄버거를 선택하세요")
label2 = Label(root, text="음료를 선택하세요")
label1.pack()


# 라디오버튼 생성
burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="클래식버거", value = 1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="치즈버거", value = 2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value = 3, variable=burger_var)
btn_burger4 = Radiobutton(root, text="더블버거", value = 4, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()
btn_burger4.pack()

label2.pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라",variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다",variable=drink_var)
btn_drink3 = Radiobutton(root, text="밀크쉐이크", value="밀크쉐이크",variable=drink_var)
btn_drink4 = Radiobutton(root, text="레모에이드", value="레모에이드",variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()
btn_drink4.pack()

def btncmd():
    print(burger_var.get())
    print(drink_var.get())

btn1 = Button(root, text="Order",command=btncmd)
btn1.pack()



#-----------------------------------------------------------




root.mainloop()