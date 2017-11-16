
# A Simple Calculator
# Made By: John M.

# These libraries allow the UI and window to be made
from tkinter import *
from tkinter import ttk # Library adds widgets which can be added to the window

# Important Variables
TITLE = 'A Simple Calculator'
SIZE = '320x500'
BUTTONYPAD = 5
BUTTONXPAD = 5
BGCOLOR = 'grey'

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

# First row of buttons
row1 = Frame(window, background=BGCOLOR)
row1.pack(side=TOP, pady=2, padx=5, fill=X)

squareroot = Button(row1, text='√', bg='#006633', fg='#000000')
squareroot.pack(side=LEFT, padx=BUTTONXPAD)
squareroot.config(width=3, font=('Courier', 24))

square = Button(row1, text='x^2', bg='#006633', fg='#000000')
square.pack(side=LEFT, padx=BUTTONXPAD)
square.config(width=3, font=('Courier', 24))

clear = Button(row1, text='C', bg='#006633', fg='#000000')
clear.pack(side=LEFT, padx=BUTTONXPAD)
clear.config(width=3, font=('Courier', 24))

add = Button(row1, text='+', bg='#006633', fg='#000000')
add.pack(side=LEFT, padx=BUTTONXPAD)
add.config(width=3, font=('Courier', 24))


# Second row of buttons
row2 = Frame(window, background=BGCOLOR)
row2.pack(side=TOP, pady=2, fill=X)


# Escape key closes the program
def exit(event):
    print ('Exiting...')
    sys.exit()
window.bind('<Escape>', exit)

window.mainloop() # Keeps looping the window (prevents it from closing)
