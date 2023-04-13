from customtkinter import CTkTextbox


class OutputTerminal(CTkTextbox):
    def __init__(self, root):
        super().__init__(master=root.main_container)
        self.parent= root
        self.bg_color = "black"
        self.fg_color = "white"
        self.font = ("Consolas", 12)
        self.text_color = "white"
        self.border_width = 0
        self.pack(padx=5, pady=5, fill="both", expand=True, anchor="s")

    def write(self, text):
        self.config(state="normal")
        self.insert("end", text)
        self.config(state="disabled")
        self.see("end")

    def clear(self):
        self.config(state="normal")
        self.delete("1.0", "end")
        self.config(state="disabled")

    def get_text(self):
        return self.get("1.0", "end")
