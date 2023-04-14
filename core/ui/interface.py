import tkinter as tk
import customtkinter





class Interface:
    def __init__(self, root, app):
        root_frame = customtkinter.CTkFrame(master=root)
        root_frame.grid(row=4, column=0, sticky=(tk.W, tk.E), ipadx=25, padx=25, pady=(25, 0))
        root_frame.columnconfigure(0, weight=1)
        root_frame.columnconfigure(1, weight=2)
        root_frame.columnconfigure(2, weight=2, pad=20)
        root_frame.rowconfigure(0, pad=20)
        root_frame.rowconfigure(1, pad=20)
        root_frame.rowconfigure(2, pad=20)
        root_frame.rowconfigure(3, pad=20)
        root_frame.rowconfigure(4, pad=20)
        root_frame.rowconfigure(5, pad=20)

        self.__root = root
        self.__app = app
        self.__title = tk.StringVar(root_frame, "")
        self.__spydermap = tk.StringVar(root_frame, "viridis")
        self.__spydermap_accents = tk.StringVar(root_frame, "plasma")

        self.__title_font_string = tk.StringVar(root_frame, "Sonos 20")
        self.__title_font_family = "Sonos"
        self.__title_font_size = 20
        self.__title_font_color = "white"

        self.__data_font_string = tk.StringVar(root_frame, "Terminal 10")
        self.__data_font_family = "Terminal"
        self.__data_font_size = 10
        self.__data_font_color = "white"

        self.__app.table_properties = {
            "title": self.__title.get(),
            "title_font_family": self.__title_font_family,
            "title_font_size": self.__title_font_size,
            "spydermap": self.__spydermap.get(),
        }

        __title_label = customtkinter.CTkLabel(master=root_frame, textvariable=self.__title )
        __title_label.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E), padx=25, pady=25)
        __title_entry = customtkinter.CTkEntry(master=root_frame, textvariable=self.__title)
        __title_entry.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), padx=25, pady=25)
        __title_label_font = tk.font.Font(family=self.__title_font_family, size=self.__title_font_size)
        __title_entry_font = tk.font.Font(family=self.__title_font_family, size=self.__title_font_size)


        __spydermap_label = customtkinter.CTkLabel(master=root_frame, text="Spyders")
        __spyders = ["4Chan Crawler", "Reddit Crawler", "Twitter Crawler", "Mastodon Crawler", "Tiktok Crawler", "Targeted Crawler", "Custom Crawler"]
        __spydermap_entry = customtkinter.CTkComboBox(master=root_frame,  values=__spyders)
        __spydermap_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))
        __spydermap_entry.configure(state="readonly", text_color="white")


    def __update_data(self):
        self.__app.table_properties = {
            "title": self.__title.get(),
            "title_font_family": self.__title_font_family,
            "title_font_size": self.__title_font_size,
            "spydermap": self.__spydermap.get(),
        }
        self.__app.update_data()



    def __reset(self):
        self.__title.set("")
        self.__spydermap.set("viridis")
        self.__spydermap_accents.set("plasma")
        self.__app.reset()
