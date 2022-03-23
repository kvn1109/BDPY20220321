import tkinter
from tkinter import font

def func57(event):
    label2.config(text="move to[%d,%d]" % (event.x, event.y))

#視窗起始
top = tkinter.Tk()

#列印字形的家族
print(font.families())
f1 = font.Font(family='Arial Black', size=24)

label = tkinter.Label(top, text="detect area", font=f1, padx=30, pady=30, bg='#C0FFEE', fg='#F00')
label2 = tkinter.Label(top, text="中文", font=f1, pady=20, bg='#C0EEFF', fg='#0F0')
label2.pack()
label.bind('<Motion>', func57)
label.pack()

#視窗結束
top.mainloop()