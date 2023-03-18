import os
import customtkinter
from distutils.file_util import write_file
from spyder.spawner import SpyderSpawner
from .ui.input_data_panel import InputDataPanel
from .ui.message_controller import MessageController
import tkinter as tk
from spyder.parser import Parser
from .ui.output_data_panel import OutputDataTerminal
from .ui.side_panel import SidePanel



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




class Application(object):
    def __init__(self, root):
        self.parser = Parser()
        self.message_controller = MessageController(root)
        self.spawner = SpyderSpawner()
        self.crawlers = ["Chan", "Redd", "Twit", "Tar"]
        self.data = None
        self.output_properties = {}

        root.title("SpyderHound")
        root.geometry("1200x800")
        menu_panel = tk.Menu(root)
        root.config(menu=menu_panel)

        filemenu = tk.Menu(menu_panel, tearoff=0)
        filemenu.add_command(label="Load", command=self.load)
        filemenu.add_command(label="Save", command=self.save)
        filemenu.add_command(label="Help", command=self.help)
        filemenu.add_command(label="Run", command=self.run)
        filemenu.add_command(label="Exit", command=self.quit)

        main_frame = customtkinter.CTkFrame(master=root)
        main_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W), padx=5, pady=15)

        self.side_panel = SidePanel(main_frame, self)
        self.input_data = InputDataPanel(main_frame, self)
        self.output_data = OutputDataTerminal(main_frame)



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


    def help(self):
        self.message_controller.show_message("Help", "Help")

    def load(self):
        self.message_controller.show_message("Load", "Load")

    def save(self):
        self.message_controller.show_message("Save", "Save")

    def clear(self):
        self.message_controller.show_message("Clear", "Clear")

    def quit(self):
        self.message_controller.show_message("Quit", "Quit")

    def run(self):
        self.message_controller.show_message("Run", "Run")
