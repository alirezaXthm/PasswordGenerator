from tkinter import *
from pw_manager import pass_generator 

window = Tk()
window.geometry('600x600')
window.title('first GUI app')
window.config(background='#9bc2a2')

frame = Frame(window, bg = '#9bc2a2')
values = []


head_label = Label(frame, text='What do you want in your password? ', font = ('arial', 12,'bold'),bg='#9bc2a2', fg='black' )
length_label = Label(window, text='How many characters should your password have?', font = ('arial', 12,'bold'),bg='#9bc2a2', fg='black')


def get_length():
    print(length_box.get())
    global password_length
    password_length = length_box.get()
    

def submit():
    password_text.delete(1.0, END)
    global length 
    global values
    global password
    user_choice = values
    length = int(password_length)
    password = pass_generator(user_choice, length)
    password_text.insert(1.0, password)
    password_text.configure(state='normal')
    print(password)


password_length = 8
length_box = Spinbox(frame, from_=8, to=100, textvariable=password_length, command= get_length, bg='#9bc2a2')
password = "NONE"
password_text = Text(window, font = ('arial', 15),bg ='#9bc2a2' )


submit_button = Button(
                        window,
                        text='Generate',
                        command=submit,
                        font = ('Arial', 12, 'bold'),
                        compound='bottom',
                        fg = '#6f67b5',
                        bg = '#8aba92',
                        activeforeground='#6f67b5',
                        activebackground='#8aba92',
)


def lower_action():
    values.append(lower_check_value.get())

    
    
def upper_action():
    values.append(upper_check_value.get())



def number_action():
    values.append(number_check_value.get())



def symbol_action():
    values.append(symbol_check_value.get())



lower_check_value = IntVar()
upper_check_value = IntVar()
number_check_value = IntVar()
symbol_check_value = IntVar()

lower_check_button = Checkbutton(
                        frame,
                        text = '. Lower Case Letters',
                        font = ('airal', 16, 'italic'),
                        fg = 'black',
                        bg = '#9bc2a2',
                        activeforeground='black',
                        activebackground='#9bc2a2',
                        command=lower_action,
                        variable=lower_check_value,
                        onvalue=1,
                        offvalue=0,
                        anchor=W,
                        )

upper_check_button = Checkbutton(
                        frame,
                        text = '. Upper Case Letters',
                        font = ('airal', 16, 'italic'),
                        fg = 'black',
                        bg = '#9bc2a2',
                        activeforeground='black',
                        activebackground='#9bc2a2',
                        command=upper_action,
                        variable=upper_check_value,
                        onvalue=2,
                        offvalue=0,
                        anchor=W,
                        )

number_check_button = Checkbutton(
                        frame,
                        text = '. Numbers',
                        font = ('airal', 16, 'italic'),
                        fg = 'black',
                        bg = '#9bc2a2',
                        activeforeground='black',
                        activebackground='#9bc2a2',
                        command=number_action,
                        variable=number_check_value,
                        onvalue=3,
                        offvalue= 0,
                        anchor=W,
                        )

symbol_check_button = Checkbutton(
                        frame,
                        text = '. Symbols',
                        font = ('airal', 16, 'italic'),
                        fg = 'black',
                        bg = '#9bc2a2',
                        activeforeground='black',
                        activebackground='#9bc2a2',
                        command=symbol_action,
                        variable=symbol_check_value,
                        onvalue=4,
                        offvalue=0,
                        anchor=W,
                        )


def run():
    length_label.pack()
    length_box.pack()
    head_label.pack(fill=X)
    frame.pack(fill=X,)
    lower_check_button.pack(fill=X)
    upper_check_button.pack(fill=X)
    number_check_button.pack(fill=X)
    symbol_check_button.pack(fill=X)
    submit_button.pack(side=['bottom'])
    password_text.pack()
    window.mainloop()

if __name__ =='__main__':
    
    run()
