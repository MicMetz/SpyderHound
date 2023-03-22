import customtkinter
from tkinter import W

from customtkinter import CTkFrame

from .input_data_panel import InputDataPanel
from .interface import Interface




class SideBar(CTkFrame):
    # (this, main_frame, Application module)
    def __init__(self, root):
        super().__init__(master=root)
        self.app = root
        self.active_targets = root.targets
        self.width = 140

        self.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self, text="SpyderHound", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # sidebar button group
        # sidebar_button_group = customtkinter.CTkFrame(master=sidebar_frame, width=140, corner_radius=0)
        # sidebar_button_group.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 10))
        # sidebar_button_group.grid_rowconfigure(0, weight=1)
        self.sidebar_button_one = customtkinter.CTkButton(master=self, text="Input", width=140, height=40, corner_radius=5, command=lambda: self.app.switch_panel("output_data_panel"))
        self.sidebar_button_one.grid(row=1, column=0, padx=10, pady=10)
        self.sidebar_button_two = customtkinter.CTkButton(master=self, text="Output", width=140, height=40, corner_radius=5, command=lambda: self.app.switch_panel("input_data_panel"))
        self.sidebar_button_two.grid(row=2, column=0, padx=10, pady=10)
        self.sidebar_button_three = customtkinter.CTkButton(master=self, text="Scrape", width=140, height=40, corner_radius=5, command=lambda: self.app.switch_panel("interface"))
        self.sidebar_button_three.grid(row=3, column=0, padx=10, pady=10)

        self.target_mode_label = customtkinter.CTkLabel(self, text="Target Mode:", anchor="w")
        self.target_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.target_mode_optionemenu = customtkinter.CTkOptionMenu(self, values=[target.name for target in self.active_targets],
                                                                   command=self.change_target_event)
        self.target_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self, text="Data Parsing:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self, values=[""],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        #
        self.nameLabel = customtkinter.CTkLabel(master=self, text="")
        self.nameLabel.grid(row=0, column=0, sticky=W, pady=(15, 0))
        # InputDataPanel(sidebar_frame, app)
        # Interface(sidebar_frame, app)

    def change_target_event(self, event):
        pass


    def change_scaling_event(self, event):
        pass
