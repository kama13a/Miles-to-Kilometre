from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=100)
window.config(pady=15, padx=15)

#TODO 1: Create entry
entry = Entry(width=10, font=("Arial", 20, "normal"))
entry.insert(END, string="0")
entry.focus()
entry.grid(row=1, column=2)
    # Create label "miles" next to the entry
miles_label = Label(text="Miles", font=("Arial", 20, "normal"))
miles_label.grid(row=1, column=3)

# TODO 2: Create multiple Labels
    # "is equal to"
equal_label = Label(text="is equal to", font=("Arial", 20, "normal"))
equal_label.grid(row=2, column=1)
    # "0"
initial_km = Label(text="0", font=("Arial", 20, "normal"))
initial_km.grid(row=2, column=2)
    # "km"
kilometre = Label(text="Km", font=("Arial", 20, "normal"))
kilometre.grid(row=2, column=3)

def calculate():
    mile = int(entry.get())
    km = round(mile * 1.60934, 2)
    initial_km.config(text=km)

# TODO 3: Calculate Button
    # When you press the button the "0" label changes
button = Button(text="Calculate", command=calculate)
button.grid(row=3, column=2)


window.mainloop()