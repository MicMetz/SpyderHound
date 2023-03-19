import customtkinter
from customtkinter import CTkEntry
import tkinter as tk


class MainEntry(CTkEntry):
    def __init__(self, root):
        super().__init__(master=root)
        self.app = root
        self.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.bind("<Return>", self.on_enter)
        self.bind("<KP_Enter>", self.on_enter)
        self.bind("<Up>", self.on_up)
        self.bind("<Down>", self.on_down)
        self.bind("<Tab>", self.on_tab)
        self.bind("<Escape>", self.on_escape)

        self.history = []
        self.history_index = 0
        self.history_max = 100
        self.history.append("")
        self.history_index = 1

        self.placeholder_text = "Enter command"
        self.placeholder_color = "green"
        self.text_color = "green"
        self.text_font = ("", 12)

        self.main_button = customtkinter.CTkButton(master=root, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Enter", command=self.on_enter)
        self.main_button.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")


    def on_escape(self, event):
        self.delete(0, tk.END)
        self.history_index = 0
        self.history[self.history_index] = ""

    def on_tab(self, event):
        pass

    def on_up(self, event):
        if self.history_index > 0:
            self.history_index -= 1
            self.delete(0, tk.END)
            self.insert(0, self.history[self.history_index])

    def on_down(self, event):
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.delete(0, tk.END)
            self.insert(0, self.history[self.history_index])

    def on_enter(self, event):
        self.history[self.history_index] = self.get()
        self.history_index += 1
        if self.history_index >= len(self.history):
            self.history.append("")
        self.delete(0, tk.END)
        self.history[self.history_index] = ""
        self.app.on_enter(self.history[self.history_index - 1])
