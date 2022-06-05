import tkinter as tk
from tkinter import ttk
from PIL import  ImageTk, Image
import os

from functools import partial

from decodepage import DecodePage
from encodepage import EncodePage
from homepage import HomePage
from loginpage import LoginPage
import hashlib
# re module provides support
# for regular expressions
import re

from encodingmenu import EncodingMenu
from hashingmenu import HashingMenu
from crackingmenu import CrackingMenu
from registerpage import RegisterPage


LARGEFONT =("Verdana", 35)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.email= None
        ico = Image.open('logo.png')
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)

        self.title(" PentRacker ")

        # creating a container
        self.container = tk.Frame(self)
        self.container.pack(side = "top", fill = "both", expand = True)

        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        self.resizable(False, False)

        # initializing frames to an empty array
        self.frames = [LoginPage, RegisterPage, HomePage, EncodingMenu,
                       HashingMenu, CrackingMenu,
                       EncodePage,DecodePage,
                       ]

        # iterating through a tuple consisting
        # of the different page layouts
        # initializing frame of that object from
        # startpage, page1, page2 respectively with
        # for loop

        self.show_frame(0)

    # to display the current frame passed as
    # parameter
    def show_frame(self, ind):
        frame = self.frames[ind](self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def get_email(self):
        return self.email

    def set_email(self,email):
        self.email=email

# first window frame startpage










# Driver Code
app = tkinterApp()
app.mainloop()

















