import customtkinter as ck
import AbstractPage as Page




class InstructionsPage(Page):

        def __init__(self, parent, controller):

            Page.__init__(self, parent, controller)

            self.title = "Instructions"

            self.label = tk.Label(self, text="Instructions Page", font=LARGE_FONT)

            self.label.pack(pady=10, padx=10)

            self.button1 = ck.Button(self, text="Back to Home",

                                command=lambda: controller.show_frame(StartPage))

            self.button1.pack()

            self.button2 = ck.Button(self, text="Page Two",

                                command=lambda: controller.show_frame(PageTwo))

            self.button2.pack()
