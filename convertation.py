from tkinter import END
import tkinter.messagebox as ms

def decimal_to_binary_lab(entry):
    try: 
        dec = int(entry.get())
        result_to_print = ""
        minus = True if dec < 0 else False
        dec = abs(dec)
        if dec == 0:
            return str(0)
        
        while dec!=0:
            result_to_print += str(dec%2)
            dec = dec//2
        entry.delete(0, END)
        return '-' + result_to_print[::-1] if minus else result_to_print[::-1]
    except TypeError:
        ms.showerror("Error!", "Enter integer number")
        entry.delete(0, END)
    except ValueError:
        ms.showerror("Error!", "Enter integer number")
        entry.delete(0, END)
    
def binary_to_decimal_lab(entry):
    try:
        binary = int(entry.get(), 2)
        entry.delete(0, END)
        return str(binary)
    except TypeError:
        ms.showerror("Error!", "Enter binary number")
        entry.delete(0, END)
    except ValueError:
        ms.showerror("Error!", "Enter binary number")
        entry.delete(0, END)