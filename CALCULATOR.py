from tkinter import *
root = Tk()

root.title("CALCULATOR") # Title
root.geometry("340x310")

text = Entry(root, font = ("calibri", 16))
text.pack(fill = X, padx = 5, pady = 5, ipadx = 5, ipady = 5) # Text

def Add_Text(n): # Add Text
    text.insert(END, n)

def calculate(): # Calculations
    result = eval(text.get())
    text.delete(0, END)
    text.insert(0, result)

def Del(): # Clear Text
    text.delete(0, END)
    text.insert(0, "")

frame = Frame(root)
frame.pack(side = TOP, anchor = NW)

# NUMBERS

frame1 = Frame(frame)
frame1.pack()

button_1 = Button(frame1, text = "1", width = 9, height = 3, command = lambda:Add_Text("1"))
button_1.pack(side = LEFT)

button_2 = Button(frame1, text = "2", width = 9, height = 3, command = lambda:Add_Text("2"))
button_2.pack(side = LEFT)

button_3 = Button(frame1, text = "3", width = 9, height = 3, command = lambda:Add_Text("3"))
button_3.pack(side = LEFT)

frame2 = Frame(frame)
frame2.pack()

button_4 = Button(frame2, text = "4", width = 9, height = 3, command = lambda:Add_Text("4"))
button_4.pack(side = LEFT)

button_5 = Button(frame2, text = "5", width = 9, height = 3, command = lambda:Add_Text("5"))
button_5.pack(side = LEFT)

button_6 = Button(frame2, text = "6", width = 9, height = 3, command = lambda:Add_Text("6"))
button_6.pack(side = LEFT)

frame3 = Frame(frame)
frame3.pack()

button_7 = Button(frame3, text = "7", width = 9, height = 3, command = lambda:Add_Text("7"))
button_7.pack(side = LEFT)

button_8 = Button(frame3, text = "8", width = 9, height = 3, command = lambda:Add_Text("8"))
button_8.pack(side = LEFT)

button_9 = Button(frame3, text = "9", width = 9, height = 3, command = lambda:Add_Text("9"))
button_9.pack(side = LEFT)

frame4 = Frame(frame)
frame4.pack()

button_point = Button(frame4, text = ".", width = 9, height = 3, command = lambda:Add_Text("."))
button_point.pack(side = LEFT)

button_0 = Button(frame4, text = "0", width = 9, height = 3, command = lambda:Add_Text("0"))
button_0.pack(side = LEFT)

button_equal_sign = Button(frame4, text = "=", width = 9, height = 3, command = lambda:calculate())
button_equal_sign.pack(side = LEFT)

frame5 = Frame(frame)
frame5.pack()

button_bracket_open = Button(frame5, text = "(", width = 9, height = 3, command = lambda:Add_Text("("))
button_bracket_open.pack(side = LEFT)

button_bracket_close = Button(frame5, text = ")", width = 9, height = 3, command = lambda:Add_Text(")"))
button_bracket_close.pack(side = LEFT)

button_dummy = Button(frame5, text = "", width = 9, height = 3, command = lambda:Add_Text(""))
button_dummy.pack(side = LEFT)

button_delete = Button(frame5, text = "C", width = 9, height = 3, command = lambda:Del())
button_delete.pack(side = LEFT)

button_division = Button(frame1, text = "/", width = 9, height = 3, command = lambda:Add_Text("/"))
button_division.pack()

button_multiplictaion = Button(frame2, text = "*", width = 9, height = 3, command = lambda:Add_Text("*"))
button_multiplictaion.pack()

button_addition = Button(frame3, text = "+", width = 9, height = 3, command = lambda:Add_Text("+"))
button_addition.pack()

button_substraction = Button(frame4, text = "-", width = 9, height = 3, command = lambda:Add_Text("-"))
button_substraction.pack()

root.mainloop()