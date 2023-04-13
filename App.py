import sys

from customtkinter import CTkFrame

from core.Controller import Controller
import tkinter as tk
import os.path
import customtkinter as ck

from ui.InputEntry import InputEntry
from ui.SidePanel import SidePanel
from core.Target import Target



class Application(ck.CTk):
    bg_color = "black"
    fg_color = "black"
    data_dir = 'data'
    title_str = "SpyderHound"

    sizeX = 1480
    sizeY = 720
    master = None
    database = None
    main_container: ck.CTkFrame = None
    frames = {}
    # frames = {"mainpage": CTkFrame, "splash": CTkFrame}

    entry_panel: tk.Entry = None
    controller: Controller = None
    input_panel: InputEntry = None
    side_panel: SidePanel = None
    targets: [Target()] = None


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.side_panel = None
        self.entry_panel = None
        self.input_panel = None
        self.controller = None
        self.targets = None

        self.title(self.title_str)
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.geometry(self._root_size())
        self.configure(bg=self.bg_color, fg=self.fg_color)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.main_container = ck.CTkFrame(self, width=self.sizeX, height=self.sizeY, corner_radius=0)
        self.main_container.grid_columnconfigure(1, weight=1)
        self.main_container.grid_columnconfigure((2, 3), weight=0)
        self.main_container.grid_rowconfigure((0, 1, 2), weight=1)
        self.main_container.grid(row=0, column=0, rowspan=4, columnspan=4, sticky="nsew")
        self.main_container.grid_rowconfigure(4, weight=1)

        # self.pack()
        self.splashPage()
        # self.__loadFrames()


    def splashPage(self):
        self.frames["splash"] = ck.CTkFrame(self.main_container)
        self.frames["splash"].pack()

        splashTitle = tk.Label(self.frames["splash"], text="SpyderHound", bg="black", fg="red")
        splashTitle.config(font=("MS Sans Serif", 50))
        splashTitle.grid(row=0, column=0, sticky="nsew")

        splashIcon = tk.PhotoImage(file="resources/hater.png")
        splashIconLabel = tk.Label(self.frames["splash"], image=splashIcon, bg="black")
        splashIconLabel.image = splashIcon
        splashIconLabel.grid(row=0, column=1, sticky="nsew")

        splashSubTitle = tk.Label(self.frames["splash"], text="Hate-Crawler", bg="black", fg="red")
        splashSubTitle.config(font=("MS Sans Serif", 25))
        splashSubTitle.grid(row=1, column=0, sticky="nsew")

        self.after((delay := 4000), lambda: self.after(self.frames["splash"].pack_forget(), self.__loadFrames()))


    def __loadFrames(self):

        # self.frames["mainpage"] = ck.CTkFrame(self.main_container)
        # self.frames["mainpage"].pack()

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

        self.controller = Controller(self)
        self.targets = [Target()]
        self.side_panel = SidePanel(self)
        self.controller.start()
        self.input_panel = InputEntry(self)



    def _root_size(self) -> str:
        return f"{self.sizeX}x{self.sizeY}"


    def on_extract(self, event):
        self.controller.log_area.insert(tk.END, "Scraping data...\n")
        self.controller.url = event
        self.controller.set_domain_url()

        self.targets.append(Target(self.controller.get_domain_data(), self.controller.url))

        if not os.path.exists(self.data_dir):
            self.controller.log_area.insert(tk.END, f"Creating directory {self.data_dir}\n")
            os.mkdir(self.data_dir)

        # Remove http(s):// www. and any trailing slashes or .html from the url and replace with nothing
        tag = (self.controller.url.replace(".html", "").replace(".htm", "").replace(".php", "").replace("https://", "").replace("http://", "")).replace("/", "-")
        domain_dir = f"{self.data_dir}/{tag}"
        if not os.path.exists(domain_dir):
            self.controller.log_area.insert(tk.END, f"Creating directory {domain_dir}\n")
            os.mkdir(domain_dir)

        self.controller.log_area.insert(tk.END, "Scrap success! \n")

        emails = self.controller.get_email_list()
        links = self.controller.get_links()
        images = self.controller.get_images()

        self.controller.log_area.insert(tk.END, "\n Saving email addresses found in domain \n")
        self.controller.save_emails(domain_dir)

        self.controller.log_area.insert(tk.END, "\n Saving heading list in {self.controller.url}.txt\n")
        self.controller.save_headings(domain_dir)

        self.controller.log_area.insert(tk.END, "\n Saving links found in domain \n")
        self.controller.save_links(domain_dir)

        self.controller.log_area.insert(tk.END, "\n Saving images found in domain \n")
        self.controller.save_images(domain_dir)

        self.controller.log_area.insert(tk.END, "\n Saving text found in domain \n")
        self.controller.save_paragraphs(domain_dir)

        self.controller.log_area.insert(tk.END, "\n Saving text found in domain by heading \n")
        self.controller.save_paragraphs_by_heading(domain_dir)


    def execute(self, searchphrase, target, crawler):
        self.controller.log_area.insert(tk.END, "Scraping data...\n")
        self.controller.url = self.entry_panel.get()
        self.controller.set_domain_url()
        self.controller.log_area.insert(tk.END, "Scrap success!\n")
        self.controller.log_area.insert(tk.END, f"Saving email list in {self.controller.url}.txt\n")
        emails = self.controller.get_email_list()
        links = self.controller.get_links()
        images = self.controller.get_images()

        if len(emails) > 0:
            self.controller.log_area.insert(tk.END, f"Emails found!\n")
            for email in emails:
                self.controller.log_area.insert(tk.END, f"Email found: {email}\n")
            self.controller.save_emails()
        else:
            self.controller.log_area.insert(tk.END, f"No Email found.\n")

        self.controller.log_area.insert(tk.END, f"Saving heading list in {self.controller.url}.txt\n")
        self.controller.save_headings()


    def switch_panel(self, panel):
        self.ma
        self.side_panel = panel
        self.side_panel.pack(padx=5, pady=5, ipadx=self.sizeX / 4, side=tk.LEFT, fill=tk.X, expand=True, anchor=tk.S)


    def __new(self):
        # TODO document why this method is empty
        pass


    def __save(self):
        """

        """
        pass


    def __save_as(self):
        """

        """
        pass


    def __load(self):
        """

        """
        pass


    def __help(self):
        """

        """
        pass


    def __run(self):
        """

        """
        pass


    def __stop(self):
        """

        """
        pass


    def __quit(self):
        sys.exit(0)


if __name__ == "__main__":
    # root = tk.Tk()
    # root.resizable(False, False)
    # view = Application(root)
    view = Application()

    icon = tk.PhotoImage(file="resources/hater.png")
    view.mainloop()
