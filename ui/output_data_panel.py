import tkinter as tk


class OutputDataTerminal:
    def __init__(self, root):
        self.parent = root
        self.is_connected = False
        self.connection = None

        self.frame = tk.Frame(self.parent, bg="black")
        self.frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=(0, 20))

        self.text = tk.Text(self.frame, bg="black", fg="white", font=("Courier", 12), wrap=tk.WORD)
        self.text.grid(row=0, column=0, sticky="nsew", padx=20, pady=(0, 20))

        self.text.bind("<Button-1>", self.__on_click)

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def __on_click(self, event):
        if self.is_connected:
            self.connection.disconnect()
        else:
            self.parent.connect(self)

    def connect(self, connection):
        self.connection = connection
        self.is_connected = True
        self.frame.config(bg="black")

    def disconnect(self):
        self.connection = None
        self.is_connected = False
        self.frame.config(bg="black")

    def write(self, text):
        self.text.insert(tk.END, text)
        self.text.see(tk.END)

    def clear(self):
        self.text.delete(1.0, tk.END)

    def get_text(self):
        return self.text.get(1.0, tk.END)

    def get_name(self):
        return self.name

    def get_index(self):
        return self.index

    def get_is_input(self):
        return self.is_input

    def get_is_connected(self):
        return self.is_connected

    def get_connection(self):
        return self.connection
