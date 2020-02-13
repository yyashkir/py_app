# 'Copyright © 2020 YASHKIR CONSULTING'
from typing import List

from pandas_datareader import data
import time
import datetime
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import matplotlib.pyplot as pyplot
from matplotlib.dates import date2num
import numpy
import math
import os
import glob
import os.path
import shutil
import webbrowser
import warnings
from PIL import Image


def run_code(k, pars):
    exe = str(pars[k - 1].get())
    if exe != '':                   # if non-py executable name is available
        messagebox.showinfo("START", 'Process starts, wait until the end')
        argument=save_arg_file(pars)
        os.system(exe + ' ' + argument)
        return (0)
    messagebox.showinfo("START", 'Process starts, wait until next message')
    ##body of py application, py code insert here
    messagebox.showinfo("END", 'Process terminated')
    print('Done running')
    return (0)

def save_arg_file(pars):
    arg_file = 'argfile'
    menu_length = len(menu_names)
    f = open(arg_file, 'w')
    for j in range(menu_length):
        f.write(str(menu_names[j]) + delimiter)
        s = menu_values[j][0]
        s = pars[j].get()
        f.write(str(s))
        if (j <= menu_length - 2):
            f.write('\n')
    f.close()
    return (arg_file)

def save_command_file(menu_names, menu_values, menu_file, k, pars):
    new_file = str(pars[k - 2].get())
    if len(new_file) > 0:
        menu_file = new_file
    menu_length = len(menu_names)
    f = open(menu_file, 'w')
    for j in range(menu_length):
        f.write(str(menu_names[j])+delimiter)
        s = menu_values[j][0]
        q = len(menu_values[j])
        if (q == 1):
            s = pars[j].get()
        if (q > 1):
            for i in range(q):
                s = ','.join(menu_values[j])
        f.write(str(s))
        if (j <= menu_length - 2):
            f.write('\n')
    f.close()


def read_menu_conf(mfile, delimiter):
    try:
        f = open(mfile, "r")  # opening
    except IOError:
        tkinter.messagebox.showinfo("ERROR", 'The file ' + mfile + ' is missing')
        quit()
    names = []
    values = []
    while 'TRUE':
        line = f.readline()
        if not line:
            break
        tokens = line.strip().split(delimiter)
        names.append(tokens[0])
        values.append(tokens[1])
    values_list: List[List[str]] = []
    print(values)
    print(len(values))
    print("yy")
    for k in range(len(values)):
        values_list.append(values[k].split(','))
    f.close()
    return (names, values_list)


def exit(man):
    for f in glob.glob("*.png"):
        if os.path.isfile(f):
            os.remove(f)
            print(f + ' removed')
    man.destroy()


def callback():
    webbrowser.open_new(r"http://www.yashkir.com")


def choose_command_file():
    mann = Tk()
    menufile = askopenfilename()
    mann.destroy()
    return menufile


def menu_func(menu_names, menu_values):
    man = Tk()
    pars = []
    k = 0
    for j in range(len(menu_names)):
        if (len(menu_values[j]) == 1):
            Label(man, text=menu_names[j], borderwidth=1, font=("Arial", 10, "bold")).grid(row=k, column=0, sticky=E)
            pars.append(StringVar())
            pars[k].set(menu_values[j][0])
            Entry(man, textvariable=pars[k], bd=2, justify=LEFT).grid(row=k, column=1, sticky=E + W)
            k = k + 1
        if (len(menu_values[j]) > 1):  # menu items with a set of values in the drop-down list
            Label(man, text=menu_names[j], borderwidth=1, font=("Arial", 10, "bold")).grid(row=k, column=0, sticky=E)
            pars.append(StringVar())
            types = menu_values[j]
            pars[k].set(types[0])
            w = OptionMenu(man, pars[k], *types)
            w.config(width=15, bg='light blue', activebackground='red')
            w.grid(row=k, column=1)
            k = k + 1

    man.title('run')

    Button(man, height=1, bg='light blue', activebackground='red', fg='dark blue', bd=2, text='RUN',
        font=("Arial", 12, "bold"), command=lambda:
        run_code(k, pars))\
        .grid(row=k + 2, column=0, columnspan=2, sticky=W + E)

    Button(man, bg='blue', activebackground='red', fg='red', text='Save command file',
        font=("Arial", 10, "bold"), command=lambda:
        save_command_file(menu_names, menu_values, menu_file, k, pars))\
        .grid(row=k + 3, column=0, columnspan=2,sticky=W + E)

    Button(man, bg='blue', activebackground='red', fg='red', text='Quit', font=("Arial", 10, "bold"),
        command=lambda:
        exit(man))\
        .grid(row=k + 4, column=0, columnspan=2, sticky=W + E)

    Button(man, height=1, bg='gray30', activebackground='red', fg='navy', text='Copyright © 2018 YASHKIR CONSULTING',
        font=("Arial", 10, "bold"), command=lambda:
        callback())\
        .grid(row=k + 5, column=0, columnspan=2, sticky=W + E)
    img = PhotoImage(file="yy.gif")
    imgo = PhotoImage(file="mk.gif")
    Label(man, image=img, borderwidth=1).grid(row=k + 6, column=0, columnspan=1, sticky=E + W)
    Label(man, image=imgo, borderwidth=1).grid(row=k + 6, column=1, columnspan=1, sticky=E + W)
    man.mainloop()


# starting!

menu_file = choose_command_file()

delimiter = '::'
menu_names, menu_values = read_menu_conf(menu_file, delimiter)

menu_func(menu_names, menu_values)

# 'Copyright © 2020 YASHKIR CONSULTING'
#   Last updated 11/02/2020
