from tkinter import *

# def button_clicked():
#     print("I got Clicked")
#     new_text = input.get()
#     my_label["text"] = new_text
#
# window = Tk()
# window.title("My first GUI Program")
# window.minsize(width=500, height=300)
#
# my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label["text"] = "New Text"
# my_label.grid(row=0, column=0)
#
# button = Button(text="Click Me", command=button_clicked)
# button.grid(row=1, column=1)
#
# new_button = Button(text="I am New Button", command=button_clicked)
# new_button.grid(row=0, column=2)
#
# input = Entry(width=10)
# print(input.get())
# input.grid(row=2, column=3)

def calculate():
    miles = float(miles_input.get())
    miltes_to_km = round(miles * 1.609)
    label_kilometer_result["text"] = f"{miltes_to_km}"

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=5)
miles_input.grid(column=1, row=0 )

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_is_equal_to = Label(text="is equal to")
label_is_equal_to.grid(column=0, row= 1)

label_kilometer_result = Label(text="0")
label_kilometer_result.grid(column=1, row = 1)

label_km = Label(text="km")
label_km.grid(column=2, row= 1)

button_calculate = Button(text="Calculate", command= calculate)
button_calculate.grid(column=1, row=2)


window.mainloop()