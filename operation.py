from tkinter import *
import tkinter.messagebox as ms

def convert_to_decimal(num1, num2):
    num1 = int(num1, base=2)
    num2 = int(num2, base=2)
    return num1, num2


def convert_to_binary(result):
    result_to_print = ""
    minus = True if result < 0 else False
    result = abs(result)
    if result == 0:
        return str(0) 
    
    while result!=0:
        result_to_print += str(result%2)
        result =result//2

    return '-' + result_to_print[::-1] if minus else result_to_print[::-1]

#mos - mathematical operation sign
def calculating(entry1, entry2, mos):
    try:
        num1, num2 = convert_to_decimal(entry1.get(), entry2.get())
        flag = True
        match(mos.get()):
            case "+":
                result = num1 + num2
            case "-":
                result = num1 - num2
            case "*":
                result = num1 * num2
            case "/":
                result = num1 // num2
            case _:
                result = "wrong operation!"
                flag = False
        if flag:
            entry1.delete(0, END)
            entry2.delete(0, END)
            mos.delete(0, END)
            return convert_to_binary(result)
            
        else:
            entry1.delete(0, END)
            entry2.delete(0, END)
            mos.delete(0, END)
            return result
    
    except TypeError:
        ms.showerror("Error!", "Enter binary number")
        entry1.delete(0, END)
        entry2.delete(0, END)
        mos.delete(0, END)
    except ValueError:
        ms.showerror("Error!", "Enter binary number")
        entry1.delete(0, END)
        entry2.delete(0, END)
        mos.delete(0, END)