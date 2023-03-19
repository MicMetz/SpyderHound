import os
import sys
import tkinter as tk
import traceback

import customtkinter
from distutils.file_util import write_file

from customtkinter import CTk

from ui.entrybar import MainEntry
from target import Target
from spyder.spawner import SpyderSpawner
from ui.output_data_panel import OutputDataTerminal
from ui.sidebar import SideBar
from ui.message_controller import MessageController



customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


def new_excepthook(type, value, tb):
    traceback.print_exception(type, value, tb)


sys.excepthook = new_excepthook


class AppLogger:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name, "w")
        self.file_chunck = "_log"
        self.default_dir = 'SpyderHound/DUMP/'


    def __create_log_file(self):
        if not os.path.exists(self.default_dir):
            os.makedirs(self.default_dir)
        self.file = open(self.default_dir + self.file_name + self.file_chunck, "w")

    def __close_log_file(self):
        self.file.close()

    def write(self, message):
        self.__create_log_file()
        self.file.write(message)
        self.__close_log_file()

    def read(self):
        self.__create_log_file()
        return self.file.read()

    def clear(self):
        self.__create_log_file()
        self.file.truncate(0)
        self.__close_log_file()

    def __del__(self):
        self.__close_log_file()

    def __str__(self):
        return self.read()




class Application(CTk):
    def __init__(self):
        super().__init__()
        # self.__init_ui()
        # self.parser = Parser()
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.geometry(f"{1480}x{720}")
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

        # Menubar
        # menu_panel = tk.Menu(self)
        # self.config(menu=menu_panel)
        # filemenu = tk.Menu(menu_panel)
        # menu_panel.add_cascade(label="File", menu=filemenu)
        # filemenu.add_command(label="Load", command=self.__load)
        # filemenu.add_command(label="Save", command=self.__save)
        # menu_panel.add_cascade(label="Run", command=self.__run)
        # menu_panel.add_cascade(label="Stop", command=self.__stop)
        # menu_panel.add_cascade(label="Help", command=self.__help)
        # menu_panel.add_cascade(label="Exit", command=self.__quit)

        # main_frame = customtkinter.CTkFrame(master=self)
        # main_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S), padx=3, pady=12)

        self.side_panel = SideBar(self)
        self.entry_panel = MainEntry(self)
        # self.output_data = OutputDataTerminal(self)



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



    def __save(self):
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
    root = Application()
    root.mainloop()
