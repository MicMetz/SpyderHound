import customtkinter
import tkinter as tk
from tkinter import W

from .input_data_panel import InputDataPanel
from .interface import Interface




class SideBar:
    def __init__(self, root, app):
        sidebar_frame = customtkinter.CTkFrame(master=root)
        sidebar_frame.grid(row=0, column=1, sticky=(tk.N, tk.S, tk.W, tk.E), ipadx=25)
        sidebar_frame.rowconfigure(1)
        sidebar_frame.rowconfigure(2)
        sidebar_frame.columnconfigure(0, weight=1)

        nameLabel = customtkinter.CTkLabel(master=sidebar_frame, text="Sidebar")
        nameLabel.grid(row=0, column=0, sticky=W, pady=(15, 0))
        InputDataPanel(sidebar_frame, app)
        Interface(sidebar_frame, app)
