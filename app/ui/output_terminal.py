from customtkinter import CTkTextbox


class OutputTerminal(CTkTextbox):
    def __init__(self, root, app):
        super().__init__(master=root, width=100, height=10, corner_radius=0)
        self.parent = app
        self.grid(row=3, column=0, sticky="nsew", padx=20, pady=(0, 20))
        self.config(state="disabled")

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
