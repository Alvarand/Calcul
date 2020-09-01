import tkinter

root = tkinter.Tk()

root.configure(background='black')
root.title('Calculator')
root.minsize(width=329, height=500)
root.attributes('-alpha', 0.99)
root.resizable(width=False, height=False)
canvas = tkinter.Canvas(root, width=329, height=500, highlightthickness=0, bg='#1f1f1f')
canvas.place(x=0, y=0)


def zero():
    '''This function calls when button_0 pressed'''
    if label['text'] != '0':
        label['text'] += '0'


def one():
    '''This function calls when button_1 pressed'''
    if label['text'] == '0':
        label['text'] = '1'
    else:
        label['text'] += '1'


def two():
    '''This function calls when button_2 pressed'''
    if label['text'] == '0':
        label['text'] = '2'
    else:
        label['text'] += '2'


def three():
    '''This function calls when button_3 pressed'''
    if label['text'] == '0':
        label['text'] = '3'
    else:
        label['text'] += '3'


def four():
    '''This function calls when button_4 pressed'''
    if label['text'] == '0':
        label['text'] = '4'
    else:
        label['text'] += '4'


def five():
    '''This function calls when button_5 pressed'''
    if label['text'] == '0':
        label['text'] = '5'
    else:
        label['text'] += '5'


def six():
    '''This function calls when button_6 pressed'''
    if label['text'] == '0':
        label['text'] = '6'
    else:
        label['text'] += '6'


def seven():
    '''This function calls when button_7 pressed'''
    if label['text'] == '0':
        label['text'] = '7'
    else:
        label['text'] += '7'


def eight():
    '''This function calls when button_8 pressed'''
    if label['text'] == '0':
        label['text'] = '8'
    else:
        label['text'] += '8'


def nine():
    '''This function calls when button_9 pressed'''
    if label['text'] == '0':
        label['text'] = '9'
    else:
        label['text'] += '9'


def CE():
    '''This function calls when button_C pressed'''
    label['text'] = '0'


def backspace():
    '''This function calls when button_(<-) pressed'''
    if len(label['text']) > 1:
        if label['text'][-1] == ' ':
            label['text'] = label['text'][:len(label['text']) - 3]
        else:
            label['text'] = label['text'][:len(label['text']) - 1]
    else:
        label['text'] = '0'


def plus_minus():
    '''This function calls when button_(+/_) pressed'''
    if (label['text'][0] != '-') and (label['text'] != '0'):
        label['text'] = '-' + label['text']
    elif label['text'][0] != '0':
        label['text'] = label['text'][1:]


def plus():
    '''This function calls when button_+ pressed'''
    if label['text'][-1] not in ('+', '-', '*', '/', '.', ' '):
        label['text'] += ' + '


def minus():
    '''This function calls when button_- pressed'''
    if label['text'][-1] not in ('+', '-', '*', '/', '.', ' '):
        label['text'] += ' - '


def divide():
    '''This function calls when button_/ pressed'''
    if label['text'][-1] not in ('+', '-', '*', '/', '.', ' '):
        label['text'] += ' / '


def multiply():
    '''This function calls when button_* pressed'''
    if label['text'][-1] not in ('+', '-', '*', '/', '.', ' '):
        label['text'] += ' * '


def dot():
    '''This function calls when button_. pressed'''
    if label['text'].count('.') == 0 and label['text'][-1] not in ('+', '-', '*', '/', ' '):
        label['text'] += '.'


def equals():
    '''This function calls when button_= pressed'''
    pass


def degree():
    '''This function calls when button_(x^2) pressed'''
    pass


def create_buttons():
    '''Painting buttons'''
    dict = {
        '1': one,
        '2': two,
        '3': three,
        '4': four,
        '5': five,
        '6': six,
        '7': seven,
        '8': eight,
        '9': nine
    }
    for i in range(3):
        for j in range(1, 4):
            button = tkinter.Button(text=str(i * 3 + j), width=8, height=2, bd=0, font='arial', fg='white',
                                    bg='#060606', command=dict[str(i * 3 + j)])
            button.place(x=5 + (j - 1) * 80, y=402 - 48 * i)

    button = tkinter.Button(text='+/_', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606',
                            command=plus_minus)
    button.place(x=5, y=450)
    button = tkinter.Button(text='0', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606', command=zero)
    button.place(x=5 + 80, y=450)
    button = tkinter.Button(text='.', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606', command=dot)
    button.place(x=5 + 160, y=450)
    button = tkinter.Button(text='=', width=8, height=2, bd=0, font='arial', fg='white', bg='#795d13', command=equals)
    button.place(x=5 + 240, y=450)
    button = tkinter.Button(text='+', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606', command=plus)
    button.place(x=5 + 240, y=450 - 48)
    button = tkinter.Button(text='-', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606', command=minus)
    button.place(x=5 + 240, y=450 - 96)
    button = tkinter.Button(text='x', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606', command=multiply)
    button.place(x=5 + 240, y=450 - 144)
    button = tkinter.Button(text='/', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606', command=divide)
    button.place(x=5 + 240, y=450 - 192)
    button = tkinter.Button(text='C', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606', command=CE)
    button.place(x=5, y=450 - 192)
    button = tkinter.Button(text='x^2', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606', command=degree)
    button.place(x=5 + 80, y=450 - 192)
    button = tkinter.Button(text='<-', width=8, height=2, bd=0, font='arial', fg='white', bg='#060606',
                            command=backspace)
    button.place(x=5 + 160, y=450 - 192)


v = '0'
label = tkinter.Label(text=v, bg='#1f1f1f', fg='white', font='Arial 30')
label.place(x=10, y=10)

create_buttons()

if __name__ == '__main__':
    root.mainloop()
