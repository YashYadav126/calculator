
from tkinter import *
def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text =="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())   

        scvalue.set(value)
        screen.update()    



    elif text =="c":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
    

root = Tk()

root.geometry("400x800")
root.title('YASH CALCULATOR')
scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue,font="verdana 40 bold")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)
f = Frame(root,bg="gold")
b = Button(f,text="9",font="lucida 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)


b = Button(f,text="8",font="lucida 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)

b = Button(f,text="7",font="lucida 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)
f.pack()




f = Frame(root,bg="gold")
b = Button(f,text="6",font="lucida 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)


b = Button(f,text="5",font="lucida 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)

b = Button(f,text="4",font="lucida 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)
f.pack()



f = Frame(root,bg="gold")
b = Button(f,text="3",font="lucida 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)


b = Button(f,text="2",font="lucida 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)

b = Button(f,text="1",font="lucida 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)
f.pack()


f = Frame(root,bg="gold")
b = Button(f,text="-",font="lucida 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)


b = Button(f,text="0",font="lucida 35 bold")
b.pack(side=LEFT,padx=11,pady=3)
b.bind("<Button-1>",click)

b = Button(f,text="*",font="lucida 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="gold")
b = Button(f,text="/",font="lucida 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)


b = Button(f,text="c",font="lucida 35 bold")
b.pack(side=LEFT,padx=3,pady=3)
b.bind("<Button-1>",click)

b = Button(f,text="+",font="lucida 35 bold")
b.pack(side=LEFT,padx=3,pady=1)
b.bind("<Button-1>",click)
f.pack()


f = Frame(root,bg="gold")
b = Button(f,text="=",font="lucida 35 bold")
b.pack(side=LEFT,padx=50,pady=3)
b.bind("<Button-1>",click)

f.pack()


root.mainloop()