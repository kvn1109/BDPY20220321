import tkinter
from tkinter import font

#視窗起始
top = tkinter.Tk()

#列印字形的家族
print(font.families())
f1 = font.Font(family='Arial Black', size=24)

#在視窗中顯示標題
label = tkinter.Label(top, text="Hi TK", font=f1, padx=20, bg='#C0FFEE', fg='#F00')
label2 = tkinter.Label(top, text="中文", font=f1, pady=20, bg='#C0EEFF', fg='#0F0')
label2.pack()
label.pack()

#視窗結束
top.mainloop()