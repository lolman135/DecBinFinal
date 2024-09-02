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

root.mainloop()