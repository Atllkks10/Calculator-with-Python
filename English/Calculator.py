from tkinter import *
from tkinter import messagebox
root = Tk()

#Window size
root.geometry()
#Positioning variables
r = 0
c = 0
#Input 1
Input_1_info = Label(root, text = "First number:", font = "20")
Input_1_info.grid(row = r , column = c, padx = 3)
Input_1 = Entry(root, bg  = "grey", width = 10)
Input_1.grid(row = r + 1, column = c, padx = 10, pady = 10)
#Input 2
Input_2_info = Label(root, text = "Second number:", font = "20")
Input_2_info.grid(row = r  , column = c + 1, padx = 3)
Input_2 = Entry(root, bg  = "grey", width = 10)
Input_2.grid(row = r + 1, column = c + 1,  padx = 10, pady = 10)
#Operations
def Addition () : 
    try:
        global Result
        Result =str(int(Input_1.get()) + int(Input_2.get()))
        #Result Çubuğu
        ResultLine = Label(root, text = "Result: " + Result , font = 25)
        ResultLine.grid(row = r + 5, columnspan = 2)
    except ValueError:
        messagebox.showinfo("ERROR", "ENTER NUMBER")

def Subtraction () :
    try:
        global Result
        Result =str(int(Input_1.get()) - int(Input_2.get()))
        #Result Çubuğu
        ResultLine = Label(root, text = "Result: " + Result , font = 25)
        ResultLine.grid(row = r + 5, columnspan = 2)
    except ValueError:
        messagebox.showinfo("ERROR", "ENTER NUMBER")
def Multiplication () :
    try:
        global Result
        Result =str(int(Input_1.get())*int(Input_2.get()))
        #Result Çubuğu
        ResultLine = Label(root, text = "Result: " + Result , font = 25)
        ResultLine.grid(row = r + 5, columnspan = 2)
    except ValueError:
        messagebox.showinfo("ERROR", "ENTER NUMBER")
def Division () :
    try :
        global Result
        Result =str(int(Input_1.get())/int(Input_2.get()))
        #Result Çubuğu
        ResultLine = Label(root, text = "Result: " + Result , font = 25)
        ResultLine.grid(row = r + 5, columnspan = 2)
    except ValueError:
        messagebox.showinfo("ERROR", "ENTER NUMBER")
    except ZeroDivisionError:
        messagebox.showinfo("TANIMSIZ", "DIVISOR CAN NOT BE 0")
#Decide Operation
ButtonWidth = 5
ButtonHeight = 1
ButtonSpace_horizontal = 1
ButtonSpace_vertical = 1
Decide_Operation_info = Label(root, text = "Which operation ?", font = "20")
Decide_Operation_info.grid(row = r + 2, columnspan = 2)
Decide_Operation_1 = Button(root, text = "+", font = "50", width = ButtonWidth, height = ButtonHeight, command = Addition)
Decide_Operation_1.grid(row = r + 3 , column = c, padx = ButtonSpace_horizontal , pady = ButtonSpace_vertical)
Decide_Operation_2 = Button(root, text = "-", font = "30", width = ButtonWidth, height = ButtonHeight, command = Subtraction)
Decide_Operation_2.grid(row = r + 3 , column = c + 1, padx = ButtonSpace_horizontal , pady = ButtonSpace_vertical)
Decide_Operation_3 = Button(root, text = "*", font = "30", width = ButtonWidth, height = ButtonHeight, command = Multiplication)
Decide_Operation_3.grid(row = r + 4 , column = c, padx = ButtonSpace_horizontal , pady = ButtonSpace_vertical)
Decide_Operation_4 = Button(root, text = "/", font = "30", width = ButtonWidth, height = ButtonHeight, command = Division)
Decide_Operation_4.grid(row = r + 4 , column = c + 1, padx = ButtonSpace_horizontal , pady = ButtonSpace_vertical)

root.mainloop()
