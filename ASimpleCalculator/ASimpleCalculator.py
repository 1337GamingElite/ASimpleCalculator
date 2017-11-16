
# A Simple Calculator
# Made By: John M.

# These libraries allow the UI and window to be made
from tkinter import *
from tkinter import ttk # Library adds widgets which can be added to the window

# Variables that determine the window
TITLE = 'A Simple Calculator'
SIZE = '400x550'

# Creates a window 
window = Tk()
window.title(TITLE) # Sets the title of window
window.resizable(width=False, height=False) # Disables resizeing
window.geometry(SIZE) # Sets the size of the window
window.configure(background='grey')

answer = 0
answerLabelVar = StringVar()
answerLabelVar.set(str(answer))


# The answer box
answerBox = Label(window, textvariable = answerLabelVar, borderwidth=2, relief='groove') # Can display 11 digits
answerBox.grid(row=0, column=0, columnspan=4, pady=15, padx=10) # Positions label on grid
answerBox.config(width=11, font=('Courier', 42)) # Styling

''' A Test Method which adds 1 to the answer
def test(event):
    global answer
    global answerLabelVar
    answer += 1
    answerLabelVar.set(str(answer))
window.bind('<b>', test)
'''

# Escape key closes the program
def exit(event):
    print ('Exiting...')
    sys.exit()
window.bind('<Escape>', exit)

window.mainloop() # Keeps looping the window (prevents it from closing)