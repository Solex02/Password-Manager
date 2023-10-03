import time
import pyautogui as au
import secrets
import tkinter as tk
from tkinter import ttk
import os
import pyperclip




def create_file():
    try:
        f = open(entry_name.get()+".txt")
    except FileNotFoundError:
        input_name = entry_name.get() + ".txt"
        with open(input_name, 'w') as f:
            pswrd = secrets.token_urlsafe(10)
            f.write(pswrd)
            pyperclip.copy(pswrd)
        entry_name.delete(0, 'end')
        icon_label.pack(side='left')
        input_frame.pack()
    else:
        print("este archivo ya existe")
        

# window
window = tk.Tk()
window.title('Password Manager')
window.geometry('400x250')


# title 
title_lable = ttk.Label(master = window, text= 'Password Manager', font='Calibri 24 bold')
title_lable.pack()

#input field

input_frame = ttk.Frame(master = window)


entry_name = tk.StringVar()
entry_name = ttk.Entry(master= input_frame)
icon_label = ttk.Label(master = input_frame, text= '✓', font='Calibri 15 bold')


button = ttk.Button(master= window, text= 'Create Safe password', command= create_file)

entry_name.pack(side='left')

input_frame.pack()
button.pack()




#output


# run

window.mainloop()

