import tkinter as tk
import customtkinter as ck

import setuptools



class SplashPage(ck.CTkFrame):
    def __init__(self, parent, frame):
        ck.CTkFrame.__init__(self, frame)
        self.parent = parent
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        splashTitle = tk.Label(self, text="SpyderHound", bg="black", fg="red")
        splashTitle.config(font=("MS Sans Serif", 50))
        splashTitle.grid(row=0, column=0, sticky="nsew")

        splashIcon = tk.PhotoImage(setuptools.find_packages("../../assets/hater.png"))
        # splashIcon = tk.PhotoImage(file="../../assets/hater.png")
        splashIconLabel = tk.Label(self, image=splashIcon, bg="black")
        splashIconLabel.image = splashIcon
        splashIconLabel.grid(row=0, column=1, sticky="nsew")

        splashSubTitle = tk.Label(self, text="Hate-Crawler", bg="black", fg="red")
        splashSubTitle.config(font=("MS Sans Serif", 25))
        splashSubTitle.grid(row=1, column=0, sticky="nsew")

        self.after((delay := 1000), lambda: self.parent.switch_panel("MainPage"))
