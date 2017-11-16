
# A Simple Calculator
# Made By: John M.

# These libraries allow the UI and window to be made
from tkinter import *
from tkinter import ttk # Library adds widgets which can be added to the window

# Important Variables
TITLE = 'A Simple Calculator'
SIZE = '400x500'
BUTTONYPAD = 5
BUTTONXPAD = 5

# Creates a window 
window = Tk()
window.title(TITLE) # Sets the title of window
window.resizable(width=False, height=False) # Disables resizeing
window.geometry(SIZE) # Sets the size of the window
window.configure(background='grey')

answer = 12345678901
answerLabelVar = StringVar()
answerLabelVar.set(str(answer))

answerFrame = Frame(window)
answerFrame.pack(side=TOP, pady=15)

# The answer box
answerBox = Label(answerFrame, textvariable = answerLabelVar, borderwidth=2, relief='groove', anchor='e', bg='#006633', fg='#000000') # Can display 11 digits
answerBox.pack(side=TOP)
answerBox.config(width=11, font=('Courier', 42)) # Styling


# First row of buttons
row1 = Frame(window, background='grey')
row1.pack(side=TOP, pady=2, fill=Y)

squareroot = Button(row1, text='√', bg='#006633', fg='#000000')
squareroot.pack(side=LEFT, padx=BUTTONXPAD)
squareroot.config(width=4, font=('Courier', 24))

square = Button(row1, text='x^2', bg='#006633', fg='#000000')
square.pack(side=LEFT, padx=BUTTONXPAD)
square.config(width=4, font=('Courier', 24))

clear = Button(row1, text='C', bg='#006633', fg='#000000')
clear.pack(side=LEFT, padx=BUTTONXPAD)
clear.config(width=4, font=('Courier', 24))

add = Button(row1, text='+', bg='#006633', fg='#000000')
add.pack(side=LEFT, padx=BUTTONXPAD)
add.config(width=4, font=('Courier', 24))


# Second row of buttons

def test(event):
    global answer
    global answerLabelVar
    answer += 1
    answerLabelVar.set(str(answer))
window.bind('<b>', test)


# Escape key closes the program
def exit(event):
    print ('Exiting...')
    sys.exit()
window.bind('<Escape>', exit)

window.mainloop() # Keeps looping the window (prevents it from closing)
