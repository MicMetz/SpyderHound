from tkinter import filedialog

import customtkinter
import tkinter as tk


class InputDataPanel:
    def __init__(self, root, app):
        input_panel = customtkinter.CTkFrame(master=root)
        input_panel.grid(row=4, column=0, sticky=(tk.W, tk.E), ipadx=25, padx=25, pady=(25, 0))
        input_panel.columnconfigure(0, weight=1)
        input_panel.columnconfigure(1, weight=2)
        input_panel.columnconfigure(2, weight=2, pad=20)
        input_panel.rowconfigure(0, pad=20)
        input_panel.rowconfigure(1, pad=20)
        input_panel.rowconfigure(2, pad=20)
        input_panel.rowconfigure(3, pad=20)
        input_panel.rowconfigure(4, pad=20)
        input_panel.rowconfigure(5, pad=20)

        self.__app = app
        self.__file_path = tk.StringVar(input_panel, "No file selected")
        self.file_object = None

        panel_title_label = customtkinter.CTkLabel(master=input_panel, text="Panel title", font="Terminal 10", anchor=tk.W)
        panel_title_label.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=25, pady=25)
        panel_file_label = customtkinter.CTkLabel(master=input_panel, text="File path", font="Terminal 10", anchor=tk.W)
        panel_file_label.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=25, pady=25)
        panel_button = customtkinter.CTkButton(master=input_panel, text="Select file", command=self.__select_file)
        panel_button.grid(row=1, column=2, sticky=(tk.W, tk.E), padx=25, pady=25)

        panel_file_path_label = customtkinter.CTkLabel(master=input_panel, textvariable=self.__file_path, font="Terminal 10", anchor=tk.W)
        panel_file_path_label.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=25, pady=25)

        start_button = customtkinter.CTkButton(master=input_panel, text="Start", command=self.__start)
        start_button.grid(row=2, column=0, sticky=(tk.W, tk.E), padx=25, pady=25)

        stop_button = customtkinter.CTkButton(master=input_panel, text="Stop", command=self.__stop)
        stop_button.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=25, pady=25)

        clear_button = customtkinter.CTkButton(master=input_panel, text="Clear", command=self.__clear)
        clear_button.grid(row=2, column=2, sticky=(tk.W, tk.E), padx=25, pady=25)

        def __select_file(self):
            self.file_object = filedialog.askopenfile(mode="r", title="Select file", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
            if self.file_object is not None:
                self.__file_path.set(self.file_object.name)

        def __start(self):
            if self.file_object is not None:
                self.__app.start(self.file_object)
            else:
                self.__app.message_controller.show_message("No file selected", "Error")

        def __stop(self):
            self.__app.stop()

        def __clear(self):
            self.__app.clear()
            self.__file_path.set("No file selected")
            self.file_object = None

        def __help(self):
            self.__app.help()
