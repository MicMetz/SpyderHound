import tkinter as tk


class OutputDataTerminal:
    def __init__(self, parent, name, index, is_input):
        self.parent = parent
        self.name = name
        self.index = index
        self.is_input = is_input
        self.is_connected = False
        self.connection = None

        self.frame = tk.Frame(self.parent, bg="black", width=200, height=200)
        self.frame.grid(row=0, column=self.index, sticky=(tk.N, tk.S, tk.E, tk.W), padx=5, pady=15)
        self.frame.grid_propagate(False)

        self.label = tk.Label(self.frame, text=self.name, bg="black", fg="white")
        self.label.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W), padx=5, pady=15)

        self.text = tk.Text(self.frame, bg="black", fg="white", height=10, width=20)
        self.text.grid(row=1, column=0, sticky=(tk.N, tk.S, tk.E, tk.W), padx=5, pady=15)

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
        self.frame.config(bg="green")

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
