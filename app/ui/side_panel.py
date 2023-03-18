import customtkinter
import tkinter as tk

from app.ui.input_data_panel import InputDataPanel
from app.ui.interface import Interface


class SidePanel:
    def __init__(self, root, app):
        side_panel = customtkinter.CTkFrame(master=root)
        side_panel.grid(row=0, column=1, sticky=(tk.N, tk.S, tk.W, tk.E), ipadx=25)
        side_panel.rowconfigure(1)
        side_panel.rowconfigure(2)
        side_panel.columnconfigure(0, weight=1)
        side_panel_label = customtkinter.CTkLabel(master=side_panel, text="Side Panel", text_font=("", 16))
        side_panel_label.grid(row=0, column=0, sticky=tk.W, pady=(15, 0))
        InputDataPanel(side_panel, app)
        Interface(side_panel, app)


    def __clear(self):
        pass

