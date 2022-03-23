import tkinter
from tkinter import font

counter = 0
c_list2 = [0]

def func1():
    #需要在函式中將不可變的數字變數進行宣告，才能變化數字
    global counter
    print("hi, button clicked")
    label.config(text="hi, button clicked %d times" % counter)
    counter += 1

def func2():
    #使用的List變數時候，則不需要在函式中宣告即可引用變數
    label2.config(text="你已經按下了%d次" % c_list2[0])
    c_list2[0] += 1

top = tkinter.Tk()

print(font.families())
f1 = font.Font(family='Arial Black', size=24)

label = tkinter.Label(top, text="Hi TK", font=f1, padx=20, bg='#C0FFEE', fg='#F00')
label2 = tkinter.Label(top, text="中文", font=f1, pady=20, bg='#C0EEFF', fg='#0F0')
button = tkinter.Button(top, text="按我1", font=f1, bg='#FFC0EE', command=func1)
button2 = tkinter.Button(top, text="按我2", font=f1, bg="#FFEEC0", command=func2)
label.pack()
label2.pack()
button.pack()
button2.pack()

top.mainloop()