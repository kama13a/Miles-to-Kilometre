from tkinter import *

def button_clicked():
    message = input.get()
    my_label.config(text= message)

window = Tk() # Creating Tk object and window
window.title("My first GUI program") # Giving title
window.minsize(width=500, height=300) # Size of the window
window.config(padx=20, pady=20) # Padding around window

# Label
my_label = Label(text="i am a label", font=("Arial", 24, "bold"))
# pack -- Placing the widgets in the window it is like preparing food then placing it on the table how i want
# pack will pack all widgets in order

# the =... means that the argument is optional in function

my_label["text"] = "New text" #Updating a widget's attribute in Tkinter
my_label.config(text="New text") # config() -- Updates multiple attributes at once
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)
# Button

button = Button(text="Click Me", command=button_clicked) # Creating a bottom and
# command --- action after button pressed , gets function
button.grid(column=1, row=1) # Layout for the bottom

def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.grid(column=3, row=0)
# Entry

input = Entry(width=10) # Input
input.grid(column=4, row=3) # Layout for input

 # returns the input as string

 # place --- is all about precise positioning








window.mainloop()