import os
import sys
import tkinter as tk

import customtkinter as ck

from core.Controller import Controller
from core.Target import Target
from core.ui.InputTerminal import InputTerminal
from core.ui.SidePanel import SidePanel



class MainPage(ck.CTkFrame):
    def __init__(self, frame, parent):
        ck.CTkFrame.__init__(self, frame)
        self.parent = parent
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.parent.targets = [Target()]
        self.parent.side_panel = SidePanel(self.parent, self)
        self.parent.controller = Controller(self.parent, self)
        self.parent.input_panel = InputTerminal(self.parent, self)


