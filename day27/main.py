from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

button = Button(text="Click me")
button.pack()

window.mainloop()
