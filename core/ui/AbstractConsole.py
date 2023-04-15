from customtkinter import CTkTextbox



class AbstractConsole(CTkTextbox):
    def __init__(self, frame):
        super().__init__(master=frame)



    # @Override
    # def insert(self, index, text):
    #     super().insert(index, text)
    #     self.see("end")

    def write(self, text):
        self.configure(state="normal")
        self.insert("end", text)
        self.configure(state="disabled")
        self.see("end")
        super().yview_moveto(1.0)


    def clear(self):
        self.configure(state="normal")
        self.delete("1.0", "end")
        self.configure(state="disabled")


    def get_text(self):
        return self.get("1.0", "end")


    def __scrollHandler(self, *L):
        self.yview_moveto(1.0)


    def yview_moveto(self, param):
        self.yview("moveto", param)
        self.yview("scroll", -1, "units")
        self.yview("scroll", 1, "units")


    def yview(self, *args):
        if args[0] == "moveto":
            self.see("end")
        super().yview(*args)
