from pandas import DataFrame
import customtkinter as ck
import tkinter as tk



class DataSheet(ck.CTkFrame):
    def __init__(self, parent, frame, name, description, index, columns, data, dtype, copy):
        ck.CTkFrame.__init__(self, frame)
        self.parent = parent
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.name = name
        self.description = description
        self.index = index
        self.columns = columns
        self.data = data
        self.dtype = dtype
        self.copy = copy

        self.options = ck.CTkOptionMenu(self, self.show_options()).pack()
        self.options.set("Options")

        self.text = tk.Text(self, height=10, width=50)
        self.text.pack()

        self.asynchronous = False



    def __str__(self):
        stringify = f"Name: {self.name}\nDescription: {self.description}\nIndex: {self.index}\nColumns: {self.columns}\nData: {self.data}\nDtype: {self.dtype}\nCopy: {self.copy}"
        return stringify


    def show_options(self):
        opts = self.options.get()



    def switch_async(self):
        self.asynchronous = not self.asynchronous


    def is_async(self):
        return self.asynchronous


    def on_update(self):
        pass


    def display(self, console):
        console.write(self.__str__())
        console.write("\n")


    async def display_async(self, console):
        console.write(self.__str__())
        console.write("\n")
