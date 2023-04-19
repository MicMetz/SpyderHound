import customtkinter
from customtkinter import CTkEntry
import tkinter as tk



class InputTerminal(CTkEntry):
    def __init__(self, parent, frame):
        super().__init__(master=frame)
        self.parent = parent
        self.bg_color = "black"
        self.fg_color = "white"
        self.font = ("Consolas", 12)
        self.text_color = "white"
        self.border_width = 0
        self.bind("<Return>", lambda command: self.on_enter())
        self.bind("<Escape>", lambda command: self.on_escape())
        self.bind("<Tab>", lambda command: self.on_tab())
        self.bind("<Up>", lambda command: self.on_up())
        self.bind("<Down>", lambda command: self.on_down())
        self.pack(side="left", fill="x", expand=True, padx=5, pady=5, anchor="s")


        self.history = []
        self.history_index = 0
        self.history_max = 100
        self.history.append("")

        self.placeholder_text = "Enter command"
        self.placeholder_color = "green"
        self.text_color = "green"
        self.text_font = ("", 12)

        self.extract_button = customtkinter.CTkButton(frame, fg_color="transparent", border_width=1, text_color=("gray10", "#DCE4EE"), text="Extract", command=self.on_enter)
        self.extract_button.pack(side="right", padx=5, pady=5, anchor="s")




    def on_escape(self):
        self.delete(0, tk.END)
        self.history_index = 0
        self.history[self.history_index] = ""


    def on_tab(self):
        pass


    def on_up(self):
        if self.history_index > 0:
            self.history_index -= 1
            self.delete(0, tk.END)
            self.insert(0, self.history[self.history_index])


    def on_down(self):
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.delete(0, tk.END)
            self.insert(0, self.history[self.history_index])


    def on_enter(self):
        if self.get() == "":
            return

        if self.get() == self.history[self.history_index - 1]:
            self.parent.extract(self.history[self.history_index - 1])
            self.history.append("")
            self.delete(0, tk.END)
            return

        self.history[self.history_index] = self.get()
        self.history_index += 1
        self.history.append("")
        self.parent.extract(self.history[self.history_index - 1])
        self.delete(0, tk.END)

        if self.history_index == 100:
            # removed oldest 50 entries and push down the rest
            self.history = self.history[50:]
            self.history_index = 50
