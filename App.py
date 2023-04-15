import os
import sys
import tkinter as tk
import customtkinter as ck

from core.pages.MainPage import MainPage
from core.pages.SplashPage import SplashPage
from core.HateSpeech import HateSpeechSpider
from core.ui.InputTerminal import InputTerminal
from core.Controller import Controller
from core.ui.SidePanel import SidePanel
from core.Target import Target



if os.path.exists(".env"):
    for line in open(".env"):
        var = line.strip().split("=")
        if len(var) == 2:
            os.environ[var[0]] = var[1]

if not os.path.exists('resources/hate_speech.csv'):
    HateSpeechSpider().start_requests()

# hate_frame = pd.read_csv('resources/hate_speech.csv')


class Application(ck.CTk):
    bg_color = "black"
    fg_color = "black"
    data_dir = 'output'
    title_str = "SpyderHound"

    sizeX = 1480
    sizeY = 720
    master = None
    database = None
    frame = None
    main_frame = None
    analysis_frame = None
    data_frame = None
    splash_frame = None
    frames = {}
    # frames = {"mainpage": CTkFrame, "splash": CTkFrame}

    entry_panel: tk.Entry = None
    controller: Controller = None
    input_panel: InputTerminal = None
    side_panel: SidePanel = None
    targets: [Target()] = None


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.entry_panel = None
        self.input_panel = None
        self.controller = None
        self.targets = None

        self.title(self.title_str)
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.geometry(self._root_size())
        self.configure(bg=self.bg_color, fg=self.fg_color)

        self.frame = ck.CTkFrame(self)
        self.frame.pack(side="top", fill="both", expand=True)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

        # self.pack()
        # self.splashPage()
        self.__loadFrames()


    def on_extract(self, event):
        self.controller.console.write("Scraping data...\n")
        self.controller.url = event
        self.controller.set_domain_url()

        self.targets.append(Target(self.controller.get_domain_data(), self.controller.url))

        if not os.path.exists(self.data_dir):
            self.controller.console.write(f"Creating directory {self.data_dir}\n")
            os.mkdir(self.data_dir)

        # Remove http(s):// www. and any trailing slashes or .html from the url and replace with nothing
        tag = (self.controller.url.replace(".html", "").replace(".htm", "").replace(".php", "").replace("https://", "").replace("http://", "")).replace("/", "-")
        domain_dir = f"{self.data_dir}/{tag}"
        if not os.path.exists(domain_dir):
            self.controller.console.write(f"Creating directory {domain_dir}\n")
            os.mkdir(domain_dir)

        self.controller.console.write("\n Scrap success! \n")

        self.controller.console.write("\n\n Saving raw text in domain \n")
        self.controller.save_raw_text(domain_dir)

        self.controller.console.write("\n\n Saving email addresses found in domain \n")
        self.controller.save_emails(domain_dir)

        self.controller.console.write("\n\n Saving heading list in {self.controller.url}.txt\n")
        self.controller.save_headings(domain_dir)

        self.controller.console.write("\n\n Saving links found in domain \n")
        self.controller.save_links(domain_dir)

        self.controller.console.write("\n\n Saving images found in domain \n")
        self.controller.save_images(domain_dir)

        self.controller.console.write("\n\n Saving text found in domain \n")
        self.controller.save_paragraphs(domain_dir)

        self.controller.console.write("\n\n Saving text found in domain by heading \n")
        self.controller.save_paragraphs_by_heading(domain_dir)



    def __loadFrames(self):
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

        # for F in (SplashPage, MainPage, AnalysisPage, DataPage,
        for F in (SplashPage, MainPage):
            page_name = F.__name__
            frame = F(frame=self.frame, parent=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.switch_panel("SplashPage")



    def _root_size(self) -> str:
        return f"{self.sizeX}x{self.sizeY}"




    def execute(self, searchphrase, target, crawler):
        self.controller.console.write("Scraping data...\n")
        self.controller.url = self.entry_panel.get()
        self.controller.set_domain_url()
        self.controller.console.write("Scrap success!\n")
        self.controller.console.write(f"Saving email list in {self.controller.url}.txt\n")
        emails = self.controller.get_email_list()
        links = self.controller.get_links()
        images = self.controller.get_images()

        if len(emails) > 0:
            self.controller.console.write(f"Emails found!\n")
            for email in emails:
                self.controller.console.write(f"Email found: {email}\n")
            self.controller.save_emails()
        else:
            self.controller.console.write(f"No Email found.\n")

        self.controller.console.write(f"Saving heading list in {self.controller.url}.txt\n")
        self.controller.save_headings()



    def switch_panel(self, panel):
        # self.frame.pack_forget()
        self.frame = self.frames[panel]
        self.frame.tkraise()



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
    view = Application()
    view.mainloop()
