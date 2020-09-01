import tkinter

root = tkinter.Tk()
root.title("Calculator")
root.geometry('300x500')
canvas = tkinter.Canvas(root, width=300, height=500)
canvas.place(x=0, y=0)


if __name__ == '__main__':
    root.mainloop()
