
# A Simple Calculator
# Made By: John M.

# These libraries allow the UI and window to be made
from tkinter import *
from tkinter import ttk # Library adds widgets which can be added to the window

from math import sqrt

print ("""
A Simple Calculator
By: John M.
""")

# Important Variables
TITLE = 'A Simple Calculator'
SIZE = '320x500'
BUTTONYPAD = 5
BUTTONXPAD = 5
BGCOLOR = '#6b624b'

# Creates a window 
window = Tk()
window.title(TITLE) # Sets the title of window
window.resizable(width=False, height=False) # Disables resizeing
window.geometry(SIZE) # Sets the size of the window
window.configure(background=BGCOLOR)

answer = 123456789
answerLabelVar = StringVar()
answerLabelVar.set(str(answer))

answerFrame = Frame(window)
answerFrame.pack(side=TOP, pady=15)

# The answer box
answerBox = Label(answerFrame, textvariable = answerLabelVar, borderwidth=2, relief='groove', anchor='e', bg='#006633', fg='#000000') # Can display 9 digits
answerBox.pack(side=TOP)
answerBox.config(width=9, font=('Courier', 42)) # Styling

def test():
    global answer
    global answerLabelVar
    answer += 1
    answerLabelVar.set(str(answer))

# Escape key closes the program
def exit(event=None):
    print ('Exiting...')
    sys.exit()
window.bind('<Escape>', exit)

# First row of buttons
row1 = Frame(window, background=BGCOLOR)
row1.pack(side=TOP, pady=2, padx=5, fill=X)

squareroot = Button(row1, text='√', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
squareroot.pack(side=LEFT, padx=BUTTONXPAD)
squareroot.config(width=3, font=('Courier', 24))

square = Button(row1, text='x^2', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
square.pack(side=LEFT, padx=BUTTONXPAD)
square.config(width=3, font=('Courier', 24))

clear = Button(row1, text='C', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
clear.pack(side=LEFT, padx=BUTTONXPAD)
clear.config(width=3, font=('Courier', 24))

add = Button(row1, text='+', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
add.pack(side=LEFT, padx=BUTTONXPAD)
add.config(width=3, font=('Courier', 24))


# Second row of buttons
row2 = Frame(window, background=BGCOLOR)
row2.pack(side=TOP, pady=10, padx=5, fill=X)

number7 = Button(row2, text='7', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
number7.pack(side=LEFT, padx=BUTTONXPAD)
number7.config(width=3, font=('Courier', 24))

number8 = Button(row2, text='8', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
number8.pack(side=LEFT, padx=BUTTONXPAD)
number8.config(width=3, font=('Courier', 24))

number9 = Button(row2, text='9', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
number9.pack(side=LEFT, padx=BUTTONXPAD)
number9.config(width=3, font=('Courier', 24))

subtract = Button(row2, text='-', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
subtract.pack(side=LEFT, padx=BUTTONXPAD)
subtract.config(width=3, font=('Courier', 24))


# Third row of buttons
row3 = Frame(window, background=BGCOLOR)
row3.pack(side=TOP, pady=10, padx=5, fill=X)

number4 = Button(row3, text='4', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
number4.pack(side=LEFT, padx=BUTTONXPAD)
number4.config(width=3, font=('Courier', 24))

number5 = Button(row3, text='5', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
number5.pack(side=LEFT, padx=BUTTONXPAD)
number5.config(width=3, font=('Courier', 24))

number6 = Button(row3, text='6', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
number6.pack(side=LEFT, padx=BUTTONXPAD)
number6.config(width=3, font=('Courier', 24))

multiply = Button(row3, text='*', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
multiply.pack(side=LEFT, padx=BUTTONXPAD)
multiply.config(width=3, font=('Courier', 24))


# Fourth row of buttons
row4 = Frame(window, background=BGCOLOR)
row4.pack(side=TOP, pady=10, padx=5, fill=X)

number1 = Button(row4, text='1', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
number1.pack(side=LEFT, padx=BUTTONXPAD)
number1.config(width=3, font=('Courier', 24))

number2 = Button(row4, text='2', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
number2.pack(side=LEFT, padx=BUTTONXPAD)
number2.config(width=3, font=('Courier', 24))

number3 = Button(row4, text='3', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
number3.pack(side=LEFT, padx=BUTTONXPAD)
number3.config(width=3, font=('Courier', 24))

divide = Button(row4, text='÷', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
divide.pack(side=LEFT, padx=BUTTONXPAD)
divide.config(width=3, font=('Courier', 24))


# Fifth (and last) row of buttons
row5 = Frame(window, background=BGCOLOR)
row5.pack(side=TOP, pady=10, padx=5, fill=X)

off = Button(row5, text='OFF', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000', command=exit)
off.pack(side=LEFT, padx=BUTTONXPAD)
off.config(width=3, font=('Courier', 24))

number0 = Button(row5, text='0', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
number0.pack(side=LEFT, padx=BUTTONXPAD)
number0.config(width=3, font=('Courier', 24))

decimal = Button(row5, text='.', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
decimal.pack(side=LEFT, padx=BUTTONXPAD)
decimal.config(width=3, font=('Courier', 24))

equals = Button(row5, text='=', bg='#006633', fg='#000000', activebackground=BGCOLOR, activeforeground='#000000')
equals.pack(side=LEFT, padx=BUTTONXPAD)
equals.config(width=3, font=('Courier', 24))

window.mainloop() # Keeps looping the window (prevents it from closing)
