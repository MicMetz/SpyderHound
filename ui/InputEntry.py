import customtkinter
from customtkinter import CTkEntry, CTkFrame
import tkinter as tk



class InputEntry(CTkEntry):
    def __init__(self, root):
        super().__init__(master=root.main_container)
        self.parent= root
        self.bg_color = "black"
        self.fg_color = "white"
        self.font = ("Consolas", 12)
        self.text_color = "white"
        self.border_width = 0
        self.pack(side="left", fill="x", expand=True, padx=5, pady=5, anchor="s")

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

        self.extract_button = customtkinter.CTkButton(root.main_container, fg_color="transparent", border_width=1, text_color=("gray10", "#DCE4EE"), text="Extract", command=self.on_enter)
        self.extract_button.pack(side="right", padx=5, pady=5)


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


    def on_enter(self):
        self.parent.on_extract(self.get())
        # self.history[self.history_index] = self.get()
        # self.history_index += 1
        # if self.history_index >= len(self.history):
        #     self.history.append("")
        # self.delete(0, tk.END)
        # self.history[self.history_index] = ""
        # self.parent.on_extract(self.history[self.history_index - 1])
