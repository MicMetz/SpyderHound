import customtkinter as ck
import tkinter as tk



class AbstractPage(ck.CTkFrame):
    def __init__(self, frame, parent):
        ck.CTkFrame.__init__(self, frame)
        self.parent = parent
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


    def show(self):
        self.parent.tkraise()
