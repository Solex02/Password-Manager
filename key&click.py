import time
import pyautogui as au
import secrets
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import style
import os
import pyperclip
from tkinter import messagebox
from PIL import Image, ImageTk
from configparser import ConfigParser


lista_nombres_contr = []

config = ConfigParser()
config.read("config.ini")

theme_list = ["darkly","cosmo","flatly", "minty", "morph","solar", "superhero", "vapor"]
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
        messagebox.showerror('File Manager', 'This File already exist')
        

def copy_to_clip():  
    combo_seleccionado = combo.get()
    with open(combo_seleccionado) as f:
        lines = f.readlines()
        solo_psswrd = str(lines)
        pyperclip.copy(solo_psswrd[2:16])


def open_path():
    path = os.getcwd()
    path = os.path.realpath(path)
    os.startfile(path)

    
def save_theme(theme):
    window.style.theme_use(theme)
    config.set('THEME','theme', theme)
    with open("config.ini", "w") as f:
        config.write(f)

def change_theme():
    theme_window = ttk.Toplevel(window)
    theme_window.geometry("250x120")
    theme_window.title("Cange Theme")
   
    theme_combo = ttk.Combobox(master=theme_window,values= theme_list)
    theme_combo.current(0)
    save_theme_button = ttk.Button(master=theme_window, command= lambda: save_theme(theme_combo.get()), text="Save")
    print(theme_combo.get())

    theme_combo.pack(pady=20)
    save_theme_button.pack()


lista_archivos = os.listdir(os.getcwd())

for i in lista_archivos:
    archivo = str(i)
    if ".txt" in archivo:
        lista_nombres_contr.append(archivo)
        lista_nombres_contr.sort()





# window
window = ttk.Window(themename=config["THEME"]["theme"])
window.title('Password Manager')
window.geometry('400x400')

ico = Image.open('icono.png')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)



# title 
title_lable = ttk.Label(master = window, text= 'Password Manager', font='Calibri 24 bold')
title_lable.pack()



#input field
combo = ttk.Combobox(values=lista_nombres_contr)
copy_button = ttk.Button(text="copy", command = copy_to_clip)

input_frame = ttk.Frame(master = window)

entry_name = tk.StringVar()
entry_name = ttk.Entry(master= input_frame)
icon_label = ttk.Label(master = input_frame, text= '✓', font='Calibri 15 bold')


button = ttk.Button(master= window, text= 'Create Safe password', command= create_file)

entry_name.pack(side='left')

input_frame.pack()
button.pack(pady=10)
combo.pack()
copy_button.pack()

#barra de menu 
menu_bar = tk.Menu()
menu_options = tk.Menu(menu_bar, tearoff=False)

menu_options.add_command(
    label="Open Path",
    command= open_path
)
menu_options.add_command(
    label="Chage Theme",
    command= change_theme
)



menu_bar.add_cascade(menu=menu_options, label="Options")
window.config(menu=menu_bar)
#output


# run

window.mainloop()