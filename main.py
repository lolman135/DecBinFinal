from tkinter import *
import convertation as cnv
from tkinter.ttk import Combobox
from operation import calculating


def convert_win(title, type, func):
    win2 = Toplevel(root)
    win2.title(title)
    win2.minsize(width=200, height=350)
    win2.geometry("400x350")

    Label(win2, text=f"Enter {type} number", font="Arial 20").pack(pady=40)
    content_frame = Frame(win2)
    content_frame.pack(fill = BOTH, expand=True)
    number_to_get = Entry(content_frame, font="Arial 17")
    number_to_get.place(relx=0.5, rely=0.2, anchor="center", relwidth=0.8)
    result_lab = Label(win2, text = "", font="Arial 18")
    result_lab.pack(pady=10)
    Button(win2, text="Convert number", height=2, command=lambda: result_lab
           .config(text = f"Entered number: {number_to_get.get()}\nResult: {func(number_to_get)}")).pack(fill='x', side=BOTTOM)
    
    content_frame.anchor("center")

    win2.mainloop()


def calcul_win():
    win3 = Toplevel(root)
    win3.title("binary calculator")
    win3.minsize(width=400, height=300)
    
    Label(win3, text="Calculator", font="Arial 20").pack(pady=10)
    element_frame = Frame(win3)
    element_frame.pack(pady=20, fill= BOTH, expand=True)

    entry_1 = Entry(element_frame, font = "Arial 17", width=10)
    entry_2 = Entry(element_frame, font = "Arial 17", width=10)
    op_combo = Combobox(element_frame, values=("+", "-", "*", "/"), width=3)
    
    entry_1.grid(row=0, column=0, sticky=E+W, padx=(20, 10))
    op_combo.grid(row=0, column=1)
    entry_2.grid(row=0, column=2, sticky=E+W, padx=(10, 20))

    element_frame.grid_columnconfigure(0, weight=1)
    element_frame.grid_columnconfigure(1, weight=0)
    element_frame.grid_columnconfigure(2, weight=1)

    element_frame.anchor("center")
    result_lab = Label(win3, text = "", font="Arial 20")
    result_lab.pack(pady=40)
    Button(win3, text="Calculate", height=2, command= lambda: result_lab
           .config(text= f"Result: {calculating(entry1=entry_1, entry2=entry_2, mos=op_combo)}")).pack(fill="x", side=BOTTOM)

    win3.mainloop()


root = Tk()
root.title("DecBin")
root.minsize(width=300, height=200)

choice_label = Label(root, text = "Choose operation", font="Arial 20")
choice_label.pack(pady=10)
menu_frame = Frame(root)
menu_frame.pack(fill=BOTH, expand=True)
dec_to_bin_button = Button(menu_frame, text = "Decimal to Binary", width=15, command=lambda: convert_win("decimal to binary", "decimal", cnv.decimal_to_binary_lab))
bin_to_dec_button = Button(menu_frame, text = "Binary to Decimal", width=15, command=lambda: convert_win("binary to decimal", "binary", cnv.binary_to_decimal_lab))
calculator_button = Button(menu_frame, text = "Arithmetic operations", width=15, command=calcul_win)
dec_to_bin_button.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.2)
bin_to_dec_button.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.2)
calculator_button.place(relx=0.1, rely=0.65, relwidth=0.8, relheight=0.2)

menu_frame.anchor("center")
root.mainloop()