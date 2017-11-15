
# A Simple Calculator
# Made By: John M.

# These libraries allow the UI and window to be made
from tkinter import *
from tkinter import ttk # Library adds widgets whci can be added to the window

# Variables that determine the window
TITLE = 'A Simple Calculator'
SIZE = '400x550'

# Creates a window 
window = Tk()
window.title(TITLE) # Sets the title of window
window.resizable(width=False, height=False) # Disables resizeing
window.geometry(SIZE) # Sets the size of the window




# Escape key closes the program
def exit(event):
    print ('Exiting...')
    sys.exit()
window.bind('<Escape>', exit)

window.mainloop() # Keeps looping the window (prevents it from closing)