import customtkinter
from customtkinter import CTkFrame
import customtkinter as ck



class SidePanel(CTkFrame):
    def __init__(self, parent, frame):
        super().__init__(master=frame)
        self.parent = parent
        self.master = frame
        self.bg_color = "black"
        self.fg_color = "white"
        self.font = ("Consolas", 12)
        self.text_color = "white"
        self.border_width = 0
        self.pack(side=ck.LEFT, fill=ck.Y, padx=20, pady=20)

        # self.columnconfigure((1, 2), weight=0)
        # self.rowconfigure((0, 8), weight=0)
        # self.pack(padx=5, pady=5, fill="y", expand=True, anchor="nw", side="left")

        self.logo_label = customtkinter.CTkLabel(self, text="SpyderHound", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=5, pady=5)

        self.sidebar_button_one = customtkinter.CTkButton(self, text="Input", width=140, height=40, corner_radius=5, fg_color="red", command=lambda: self.parent.switch_panel("output_data_panel"))
        self.sidebar_button_one.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_two = customtkinter.CTkButton(self, text="Output", width=140, height=40, corner_radius=5, fg_color="red", command=lambda: self.parent.switch_panel("input_data_panel"))
        self.sidebar_button_two.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_three = customtkinter.CTkButton(self, text="Scrape", width=140, height=40, corner_radius=5, fg_color="red", command=lambda: self.parent.switch_panel("interface"))
        self.sidebar_button_three.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_button_four = customtkinter.CTkButton(self, text="Database", width=140, height=40, corner_radius=5, fg_color="red", command=lambda: self.parent.switch_panel("database"))
        self.sidebar_button_four.grid(row=4, column=0, padx=20, pady=10)

        self.target_mode_label = customtkinter.CTkLabel(self, text="Target Mode:", anchor="w")
        self.target_mode_label.grid(row=5, column=0, padx=20, pady=(20, 0))
        self.target_mode_optionemenu = customtkinter.CTkOptionMenu(self, fg_color="red", values=[target.name for target in self.parent.targets], command=self.change_target_event)
        self.target_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 20))

        self.annaFrame_label = customtkinter.CTkLabel(self, text="Dataframe:", anchor="w")
        self.annaFrame_label.grid(row=7, column=0, padx=20, pady=(20, 0))
        self.annaFrame_optionemenu = customtkinter.CTkOptionMenu(self, fg_color="red", values=[annaframe.name for annaframe in self.parent.dataframes], command=self.change_dataframe_event)
        self.annaFrame_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # self.annaFrame_label = customtkinter.CTkLabel(self, text="Trainer:", anchor="w")
        # self.annaFrame_label.grid(row=9, column=0, padx=20, pady=(20, 0))
        # self.annaFrame_optionemenu = customtkinter.CTkOptionMenu(self, fg_color="red", values=[""], command=self.change_trainer_event)
        # self.annaFrame_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))

        # self.nameLabel = customtkinter.CTkLabel(self, text="")
        # self.nameLabel.grid(row=0, column=0, sticky=W, pady=(15, 0))


    def change_target_event(self, event):
        pass


    def change_dataframe_event(self, event):
        pass


    def change_trainer_event(self, event):
        pass
