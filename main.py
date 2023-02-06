# import tkinter
""" changes how we use values like for "my_label" and "window" """
from tkinter import *

# window = tkinter.Tk()
window = Tk()
window.title("My First GUI Program")
window.minsize(width=800, height=600)

# Label
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0,row=0)
# my_label.place(x=0,y=0)
# my_label.pack()

"""to override the text value label initially established"""
my_label["text"] = "New Text 1"
my_label.config(text="New Text 2")

# my_label.pack(side="left")
# my_label.pack(expand=True)

# Pack is the mechanism that adds the items to the screen
# my_label.pack()

# Button
def button_clicked():
    # my_label["text"] = "I got clicked"
    # print("I got clicked")
    my_label["text"] = input.get()

# Entry
input = Entry(width=100)
input.grid(column=0,row=1)
# input.pack()

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=1)
# button.pack()



# Entry
entry = Entry(width=100)
entry.insert(END, "Placeholder")
entry.grid(column=0,row=3)
# entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.grid(column=0,row=4)
# text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(column=0,row=5)
# spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.grid(column=0,row=6)
# scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(column=0,row=7)
# checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=0,row=8)
radiobutton2.grid(column=1,row=8)
# radiobutton1.pack()
# radiobutton2.pack()

#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=0,row=9)
# listbox.pack()
window.mainloop()