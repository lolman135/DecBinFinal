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