from tkinter import messagebox



class MessageController:
    def __init__(self, root):
        self.parent = root
        self.message = None


    def show_message(self, message, type):
        if type == "Error":
            messagebox.showerror("Error", message)
        elif type == "Info":
            messagebox.showinfo("Info", message)
        elif type == "Warning":
            messagebox.showwarning("Warning", message)
        elif type == "Ask":
            self.message = messagebox.askquestion("Question", message)
        else:
            messagebox.showinfo("Info", message)


    def add_message(self, messageString):
        self.message.append(messageString)
        self.message.append("\n")
