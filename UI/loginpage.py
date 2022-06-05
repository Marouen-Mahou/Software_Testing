import random
import tkinter as tk
from PIL import ImageTk, Image

import requests

from homepage import HomePage
from registerpage import RegisterPage


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="black")
        self.parent = parent

        canvas = tk.Canvas(self, width=900, height=500)
        canvas.configure(background='black')
        canvas.grid(columnspan=3, rowspan=9)

        image = Image.open("logo.png")
        image = image.resize((200, 200), Image.ANTIALIAS)
        image1 = ImageTk.PhotoImage(image)

        label = tk.Label(self, image=image1)
        label.image = image1

        label.configure(background='black')
        label.grid(columnspan=3, row=0)

        # Login
        loginText = tk.Label(self, text="Connexion")
        loginText.config(font=("Anonymous Pro", 30))
        loginText.config(fg="#FFFFFF")
        loginText.config(bg="black")
        loginText.grid(column=1, row=1)

        # username
        tk.Label(self, text="email :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=2, column=1)
        username = tk.StringVar()
        tk.Entry(self, textvariable=username, font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                 insertbackground="#57B947").grid(row=3, column=1)

        # password label and password entry box
        tk.Label(self, text="Password :", bg="black", fg="#57B947", font=("Anonymous Pro", 12)).grid(row=4, column=1)
        password = tk.StringVar()
        tk.Entry(self, textvariable=password, show='*', font=("Anonymous Pro", 12), bg="black", fg="#57B947",
                 insertbackground="#57B947").grid(row=5, column=1)


        # Error text
        error_label = tk.Label(self,bg="black", fg="#660000", font=("Anonymous Pro", 12))
        error_label.grid(row=6, column=1)

        # button
        connexion_text = tk.StringVar()
        connexion_btn = tk.Button(self, command=lambda: self.login(username, password, controller, error_label),
                                  textvariable=connexion_text, font=("Anonymous Pro", 14), bg="#57B947", fg="black")
        connexion_text.set("Login")
        connexion_btn.grid(column=1, row=7)

        # button
        connexion_text = tk.StringVar()
        connexion_btn = tk.Button(self, command=lambda: self.register(controller), textvariable=connexion_text,
                                  font=("Anonymous Pro", 14), bg="#57B947", fg="black")
        connexion_text.set("Register")
        connexion_btn.grid(column=1, row=8)

    def login(self, email, password, controller, error_label):
        print("email entered :", email.get())
        print("password entered :", password.get())

        # sending post request and saving response as response object
        r = requests.post(url="http://127.0.0.1:5000/login", data={
            "email": email.get(),
            "password": password.get()
        })

        resultat = r.json()

        if resultat.message == "Wrong password":
            error_label.config(text="Wrong password")

        if resultat.message == "Wrong email":
            error_label.config(text="Wrong password")


    def register(self, controller):
        controller.show_frame(1)
