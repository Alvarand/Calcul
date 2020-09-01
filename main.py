import tkinter

root = tkinter.Tk()

root.configure(background='black')
root.title('Calculator')
root.minsize(width=329, height=500)
root.attributes('-alpha', 0.99)

canvas = tkinter.Canvas(root, width=329, height=500, highlightthickness=0, bg='#1f1f1f')
canvas.place(x=0, y=0)


def zero():
    '''This function calls when button_0 pressed'''
    if label['text'] != '0':
        label['text'] += '0'


def create_buttons():
    '''Painting buttons'''
    for i in range(3):
        for j in range(1, 4):
            button = tkinter.Button(text=str(i * 3 + j), width=8, height=2, bd=0, font='arial', fg='white',
                                    bg='#060606')
            button.place(x=5 + (j - 1) * 80, y=402 - 48 * i)

    button = tkinter.Button(text='+/_', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606')
    button.place(x=5, y=450)
    button = tkinter.Button(text='0', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606', command=zero)
    button.place(x=5 + 80, y=450)
    button = tkinter.Button(text='.', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606')
    button.place(x=5 + 160, y=450)
    button = tkinter.Button(text='=', width=8, height=2, bd=0, font='arial', fg='white', bg='#795d13')
    button.place(x=5 + 240, y=450)
    button = tkinter.Button(text='+', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606')
    button.place(x=5 + 240, y=450 - 48)
    button = tkinter.Button(text='-', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606')
    button.place(x=5 + 240, y=450 - 96)
    button = tkinter.Button(text='x', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606')
    button.place(x=5 + 240, y=450 - 144)
    button = tkinter.Button(text='/', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606')
    button.place(x=5 + 240, y=450 - 192)
    button = tkinter.Button(text='C', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606')
    button.place(x=5, y=450 - 192)
    button = tkinter.Button(text='x^2', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606')
    button.place(x=5 + 80, y=450 - 192)
    button = tkinter.Button(text='<-', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606')
    button.place(x=5 + 160, y=450 - 192)


v = '0'
label = tkinter.Label(text=v, bg='#1f1f1f', fg='white', font='Arial 30')
label.place(x=10, y=10)

create_buttons()

if __name__ == '__main__':
    root.mainloop()
