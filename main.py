from tkinter import *

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



root = Tk()
root.title("DecBin")
root.minsize(width=300, height=200)

choice_label = Label(root, text = "Choose operation", font="Arial 20")
choice_label.pack(pady=10)
menu_frame = Frame(root)
menu_frame.pack(fill=BOTH, expand=True)
dec_to_bin_button = Button(menu_frame, text = "Decimal to Binary", width=15, command=None)
bin_to_dec_button = Button(menu_frame, text = "Binary to Decimal", width=15, command=None)
calculator_button = Button(menu_frame, text = "Arithmetic operations", width=15, command=None)
dec_to_bin_button.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.2)
bin_to_dec_button.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.2)
calculator_button.place(relx=0.1, rely=0.65, relwidth=0.8, relheight=0.2)

menu_frame.anchor("center")
root.mainloop()