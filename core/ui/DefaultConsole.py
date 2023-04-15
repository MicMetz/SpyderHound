from core.ui.AbstractConsole import AbstractConsole



class DefaultConsole(AbstractConsole):
    def __init__(self, root, frame):
        super().__init__(frame=frame)
        self.parent = root
        self.bg_color = "black"
        self.fg_color = "white"
        self.font = ("Consolas", 12)
        self.text_color = "white"
        self.border_width = 0
        self.pack(padx=5, pady=5, fill="both", expand=True, anchor="s")


