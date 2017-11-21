# A Simple Calculator
# A program that does basic math for you
# Made By: John M.

from tkinter import * # The foundation of this program (allows the user interface AKA UI to be made)
from tkinter import ttk # Library adds widgets which can be added to the window
from math import sqrt # Square root function

print ("""
A Simple Calculator
A program that does basic math for you
By: John M.
""")

# List of Colours used for the program

colours = {
    'bgcolor' : '#b3b3b3', # Grey
    'main' : '#c82027', # Red
    'click' : '#1f1a4f', # Blue
    'text' : '#000000' # Black
}

#
# ---------------- WINDOW CREATION -------------------
#

# Window and UI Variables
TITLE = 'A Simple Calculator'
SIZE = '320x500'
BUTTONYPAD = 5
BUTTONXPAD = 5

# Creates a window 
window = Tk() # Window object
window.title(TITLE) # Sets the title of window
window.resizable(width=False, height=False) # Disables resizeing
window.geometry(SIZE) # Sets the size of the window
window.configure(background=colours['bgcolor']) # Sets the background color
window.lift() # Makes sure the window is at the top of the screen

#
# ----------------- VARIABLES ------------------------
#

answer = 0 # The current value in the box
answerLabelVar = StringVar() # The variable responsible for changing the value in the label
answerLabelVar.set(' ') # Sets the answer box blank when first opened

var1 = None # The first number in the equation
operation = '' # Identifies the current operation being done (used for the calcualate function)
calculated = False # Sets to True if the equals sign has been pressed previously (fixes some bugs)

#
# --------------- THE ANSWER BOX -----------------
#

answerFrame = Frame(window) # The frame which contains the answer label
answerFrame.pack(side=TOP, pady=15) # Positions the frame

answerBox = Label(answerFrame, textvariable = answerLabelVar, borderwidth=2, relief='groove', anchor='e', bg=colours['main'], fg=colours['text']) # Can display 9 digits
answerBox.pack(side=TOP) 
answerBox.config(width=9, font=('Courier', 42)) # Styling

#
# ------------------- FUNCTIONS -----------------
#

''' A test function used during development
def test():
    global answer
    global answerLabelVar
    answer += 1
    answerLabelVar.set(str(answer))
'''
# Exits the program (OFF button or Escape key)
def exit(event=None):
    print ('Exiting...')
    sys.exit()

# Used to add digits to the end of the number
def appendDigit(num, event=None):
    global answer
    global answerLabelVar
    global calculated
    global var1
    if calculated == True:
        answer = 0
        answerLabelVar.set('')
        calculated = False
    if len(str(answer)) <= 8: # Prevents entering number from going past the digit limit
        ansString = str(answer)
        answer = ansString + str(num)
        answer = int(answer)
        answerLabelVar.set(str(answer))
        print (answer)

# Clears the answer box (and basically resets the entire calculator)
def clear():
    global answer
    global var1
    global answerLabelVar
    global calculated
    calculated = False
    answer = 0
    answerLabelVar.set(' ')
    var1 = None

# Calculates the equation
def calculate(event = None):
    global answer
    global var1
    global operation
    global answerLabelVar
    global calculated
    if operation == 'add':
        answer += var1
        var1 = answer
        calculated = True
        print ('VAR1: ', var1)
    elif operation == 'minus':
        answer = var1 - answer
        var1 = answer
        answer = var1
        print ('VAR1: ', var1)
        calculated = True
    elif operation == 'mult':
        answer *= var1
        var1 = answer
        calculated = True
        print ('VAR1: ', var1)
    elif operation == 'divide':
        try:
            answer = var1 / answer
            if float(var1).is_integer():
                var1 = int(var1)
            if answer.is_integer():
                answer = int(answer)
        except ZeroDivisionError:
            print('You Cannot Divide By Zero')
        var1 = answer
        answer = var1
        print ('VAR1: ', var1)
        calculated = True
    if len(str(answer)) <= 8:
        answerLabelVar.set(str(answer))
    else:
        answerLabelVar.set('# TOO BIG')
        answer = 0
        var1 = None
        calculated = False
    print('FINAL ANSWER: ', answer)

# Adds
def add(event = None):
    global answer
    global var1
    global operation
    global calculated
    if var1 == None:
        var1 = 0
    if calculated == False:
        var1 += int(answer)
    else:
        calculate == False
    answer = 0
    operation = 'add'
    print('var1: ', var1)

# Subtracts
def subtract(event = None):
    global answer
    global var1
    global operation
    global calculated
    if var1 == None:
        var1 = int(answer)
    elif calculated == False:
        var1 -= int(answer)
    else:
        calculated = False
    answer = 0
    operation = 'minus'
    print('var1: ', var1)

# Multiplies
def multiply(event = None):
    global answer
    global var1
    global operation
    global calculated
    if var1 == None:
        var1 = int(answer)
    elif calculated == False:
        var1 *= int(answer)
    else:
        calculated == False
    answer = 0
    operation = 'mult'
    print('var1: ', var1)

# Divides
def divide(event = None):
    global answer
    global var1
    global operation
    global calculated
    if var1 == None:
        var1 = int(answer)
    elif calculated == False:
        try:
            var1 /= float(answer)
        except ZeroDivisionError:
            print('You Cannot Divide By Zero')
        if var1.is_Integer():
            print ('Meme')
    else:
        calculated == False
    answer = 0
    operation = 'divide'
    print('var1: ', var1)

# Square Number
def square():
    global answer
    global var1
    global answerLabelVar
    global calculated
    answer *= answer
    var1 = answer
    calculated = True
    answerLabelVar.set(str(answer))

# Square Root
def squarert():
    global answer
    global answerLabelVar
    global var1
    global calculated 
    # NOTE: THE CURRENT SYSTEM DOES NOT WORK WELL 
    #       WITH DECIMALS SO IT CONVERTS IT TO INTEGERS
    answer = sqrt(answer)
    var1 = answer
    calculated = True
    if len(str(answer)) <= 8:
        answerLabelVar.set(str(answer))
    else:
        answerLabelVar.set('# TOO BIG')
        answer = 0
        var1 = None
        calculated = False

#
# ------------- KEY BINDS ---------------------
#

window.bind('<Escape>', exit) # Exits program

# Number Keys
window.bind('1', lambda event: appendDigit(1))
window.bind('2', lambda event: appendDigit(2))
window.bind('3', lambda event: appendDigit(3))
window.bind('4', lambda event: appendDigit(4))
window.bind('5', lambda event: appendDigit(5))
window.bind('6', lambda event: appendDigit(6))
window.bind('7', lambda event: appendDigit(7))
window.bind('8', lambda event: appendDigit(8))
window.bind('9', lambda event: appendDigit(9))
window.bind('0', lambda event: appendDigit(0))

# Operations
window.bind('+', add) # Add
window.bind('-', subtract) # Subtract
window.bind('*', multiply) # Multiply
window.bind('/', divide) # Divide

window.bind('<Return>', calculate) # Calculate

#
# ------------- BUTTONS ---------------------
#

# First row of buttons
row1 = Frame(window, background=colours['bgcolor'])
row1.pack(side=TOP, pady=2, padx=5, fill=X)

# Square root
squareroot = Button(row1, text='√', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=squarert)
squareroot.pack(side=LEFT, padx=BUTTONXPAD)
squareroot.config(width=3, font=('Courier', 24))

# Square
square = Button(row1, text='x^2', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=square)
square.pack(side=LEFT, padx=BUTTONXPAD)
square.config(width=3, font=('Courier', 24))

# Clear
clear = Button(row1, text='C', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=clear)
clear.pack(side=LEFT, padx=BUTTONXPAD)
clear.config(width=3, font=('Courier', 24))

# Addition
add = Button(row1, text='+', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=add)
add.pack(side=LEFT, padx=BUTTONXPAD)
add.config(width=3, font=('Courier', 24))


# Second row of buttons
row2 = Frame(window, background=colours['bgcolor'])
row2.pack(side=TOP, pady=10, padx=5, fill=X)

# 7
number7 = Button(row2, text='7', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=lambda: appendDigit(7))
number7.pack(side=LEFT, padx=BUTTONXPAD)
number7.config(width=3, font=('Courier', 24))

# 8
number8 = Button(row2, text='8', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=lambda: appendDigit(8))
number8.pack(side=LEFT, padx=BUTTONXPAD)
number8.config(width=3, font=('Courier', 24))

# 9
number9 = Button(row2, text='9', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=lambda: appendDigit(9))
number9.pack(side=LEFT, padx=BUTTONXPAD)
number9.config(width=3, font=('Courier', 24))

# Subtraction
subtract = Button(row2, text='-', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=subtract)
subtract.pack(side=LEFT, padx=BUTTONXPAD)
subtract.config(width=3, font=('Courier', 24))


# Third row of buttons
row3 = Frame(window, background=colours['bgcolor'])
row3.pack(side=TOP, pady=10, padx=5, fill=X)

# 4
number4 = Button(row3, text='4', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=lambda: appendDigit(4))
number4.pack(side=LEFT, padx=BUTTONXPAD)
number4.config(width=3, font=('Courier', 24))

# 5
number5 = Button(row3, text='5', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=lambda: appendDigit(5))
number5.pack(side=LEFT, padx=BUTTONXPAD)
number5.config(width=3, font=('Courier', 24))

# 6
number6 = Button(row3, text='6', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=lambda: appendDigit(6))
number6.pack(side=LEFT, padx=BUTTONXPAD)
number6.config(width=3, font=('Courier', 24))

# Multiplication
multiply = Button(row3, text='*', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=multiply)
multiply.pack(side=LEFT, padx=BUTTONXPAD)
multiply.config(width=3, font=('Courier', 24))


# Fourth row of buttons
row4 = Frame(window, background=colours['bgcolor'])
row4.pack(side=TOP, pady=10, padx=5, fill=X)

# 1
number1 = Button(row4, text='1', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=lambda: appendDigit(1))
number1.pack(side=LEFT, padx=BUTTONXPAD)
number1.config(width=3, font=('Courier', 24))

# 2
number2 = Button(row4, text='2', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=lambda: appendDigit(2))
number2.pack(side=LEFT, padx=BUTTONXPAD)
number2.config(width=3, font=('Courier', 24))

# 3
number3 = Button(row4, text='3', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=lambda: appendDigit(3))
number3.pack(side=LEFT, padx=BUTTONXPAD)
number3.config(width=3, font=('Courier', 24))

# Division
divide = Button(row4, text='÷', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=divide)
divide.pack(side=LEFT, padx=BUTTONXPAD)
divide.config(width=3, font=('Courier', 24))


# Fifth (and last) row of buttons
row5 = Frame(window, background=colours['bgcolor'])
row5.pack(side=TOP, pady=10, padx=5, fill=X)

# Off button
off = Button(row5, text='OFF', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=exit)
off.pack(side=LEFT, padx=BUTTONXPAD)
off.config(width=3, font=('Courier', 24))

# 0
number0 = Button(row5, text='0', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=lambda: appendDigit(0))
number0.pack(side=LEFT, padx=BUTTONXPAD)
number0.config(width=3, font=('Courier', 24))

# Equals
equals = Button(row5, text='=', bg=colours['main'], fg=colours['text'], activebackground=colours['click'], activeforeground=colours['text'], command=calculate)
equals.pack(side=LEFT, padx=BUTTONXPAD)
equals.config(width=8, font=('Courier', 24))

window.mainloop() # Keeps looping the window (prevents it from closing)