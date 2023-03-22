import os
import sys
import tkinter as tk
import traceback
from distutils.file_util import write_file

import customtkinter
from customtkinter import CTk, CTkFrame

from ui.entrybar import MainEntry
from target import Target
from spyder.spawner import SpyderSpawner
from ui.output_data_panel import OutputDataTerminal
from ui.sidebar import SideBar
from ui.message_controller import MessageController


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

def new_excepthook(type, value, tb):
    traceback.print_exception(type, value, tb)


sys.excepthook = new_excepthook


def clear(*widgets):
    for widget in widgets:
        if widget.winfo_exists():
            widget.destroy()

    return widgets


class Application(CTk):
    def __init__(self):
        super().__init__()
        self.main_color = "cornflower blue"
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.geometry(f"{1480}x{720}")
        # self.configure(bg="black")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.message_controller = MessageController(self)
        self.spawner = SpyderSpawner()
        self.crawlers = ["Chan", "Redd", "Twit", "Tar"]
        self.targets = [Target()]
        self.data = None
        self.output_properties = {}

        self.title("SpyderHound")

        self.splashPage()

        # self.output_data = OutputDataTerminal(self)


    def mainPage(self):
        # Menubar
        mainFrame = customtkinter.CTkFrame(master=self)
        mainFrame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

        # filemenu = customtkinter.CTkOptionMenu(master=mainFrame, values=["New", "Load", "Save", "Save As", "Help", "Exit"], command=self.optionmenu_callback)
        # Menubar
        menu_panel = tk.Menu(self)
        self.config(menu=menu_panel)
        filemenu = tk.Menu(menu_panel)
        menu_panel.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Load", command=self.__load)
        filemenu.add_command(label="Save", command=self.__save)
        menu_panel.add_cascade(label="Run", command=self.__run)
        menu_panel.add_cascade(label="Stop", command=self.__stop)
        menu_panel.add_cascade(label="Help", command=self.__help)
        menu_panel.add_cascade(label="Exit", command=self.__quit)

        side_panel = SideBar(self)
        entry_panel = MainEntry(self)
        # output_data = OutputDataTerminal(mainFrame)



    def splashPage(self):
        splashFrame = customtkinter.CTkFrame(master=self)
        splashFrame.place(relx=0, rely=0, relheight=0.9, relwidth=1)

        splashTitle = tk.Label(splashFrame, text="SpyderHound", bg="green", fg="black")
        splashTitle.config(font=("MS Sans Serif", 50))
        splashTitle.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.8)

        splashSubTitle = tk.Label(splashFrame, text="Love to Hate-Crawl?", bg="green", fg="red")
        splashSubTitle.config(font=("MS Sans Serif", 25))
        splashSubTitle.place(relx=0.1, rely=0.3, relheight=0.1, relwidth=0.8)

        splashSubsubTitle = tk.Label(splashFrame, text="Well, so do we!", bg="green", fg="red")
        splashSubsubTitle.config(font=("MS Sans Serif", 15))
        splashSubsubTitle.place(relx=0.1, rely=0.4, relheight=0.1, relwidth=0.8)

        self.after((delay := 4000), lambda: self.after(clear(splashFrame), self.mainPage()))



    def spawn(self, crawler, url, depth):
        self.spawner.spawn(crawler, url, depth)


    @staticmethod
    def create_project_dir(directory):
        if not os.path.exists(directory):
            print('Creating directory ' + directory)
            os.makedirs(directory)


    @staticmethod
    def create_data_files(project_name, base_url):
        queue = os.path.join(project_name, 'queue.txt')
        crawled = os.path.join(project_name, "crawled.txt")
        if not os.path.isfile(queue):
            write_file(queue, base_url)
        if not os.path.isfile(crawled):
            write_file(crawled, '')


    @staticmethod
    def write_file(path, data):
        with open(path, 'w') as f:
            f.write(data)


    @staticmethod
    def append_to_file(path, data):
        with open(path, 'a') as file:
            file.write(data + '\n')


    @staticmethod
    def delete_file_contents(path):
        open(path, 'w').close()


    @staticmethod
    def file_to_set(file_name):
        results = set()
        with open(file_name, 'rt') as f:
            for line in f:
                results.add(line.replace('\n', ''))
        return results


    @staticmethod
    def set_to_file(links, file_name):
        with open(file_name, "w") as f:
            for l in sorted(links):
                f.write(l + "\n")


    def switch_panel(self, panel):
        match panel:
            case "RawCombinedOutput":
                # self.output_data = OutputDataTerminal(self)
                pass

    def optionmenu_callback(self, value):
        match value:
            case "New":
                self.__new()
            case "Load":
                self.__load()
            case "Save":
                self.__save()
            case "Save As":
                self.__save_as()
            case "Help":
                self.__help()
            case "Exit":
                self.__quit()


    def __new(self):
        pass

    def __save(self):
        pass

    def __save_as(self):
        pass

    def __load(self):
        pass

    def __help(self):
        pass

    def __run(self):
        pass

    def __stop(self):
        pass

    def __quit(self):
        sys.exit(0)




if __name__ == '__main__':
    app = Application()
    app.mainloop()
