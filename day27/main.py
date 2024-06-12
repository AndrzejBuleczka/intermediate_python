from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=50, pady=50)


miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

is_equal_label = Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=10, pady=10)

km_label = Label(text="Km", font=("Arial", 24, "bold"))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

result_label = Label(text="0", font=("Arial", 24, "bold"))
result_label.grid(column=1, row=1)
result_label.config(padx=10, pady=10)


def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    result_label["text"] = f"{km}"


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)
calculate_button.config(width=10, font=("Arial", 24, "bold"))


input = Entry(width=10, font=("Arial", 24, "bold"))
input.grid(column=1, row=0)

window.mainloop()
