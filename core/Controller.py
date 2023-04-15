import datetime
import tkinter as tk

from core.Domain import Domain
from urllib.parse import urlparse

from core.ui.AbstractConsole import AbstractConsole
from core.ui.DefaultConsole import DefaultConsole



class LogController:
    pass


class Controller():
    master: tk.Tk = None
    url: str = None
    domain: Domain = None
    console: AbstractConsole = None


    # logController: LogController = None
    def __init__(self, root, frame):
        self.parent = root
        self.console = DefaultConsole(self.parent, frame)


    def switch_console(self, console: AbstractConsole):
        self.console = console


    def set_domain_url(self):
        self.domain = Domain(self.url)


    def save_headings(self, directory: str):
        headings = self.domain.headings
        filepath = f"{directory}/{urlparse(self.url).netloc}_Headings_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"

        file = open(filepath, "a+", encoding="utf-8")
        file.write("Headings List:\n")
        for index, heading in enumerate(headings):
            file.write(f"\t{index + 1}: {heading}\n")
            self.console.write(f"{index + 1}: {heading}\n")
        else:
            self.console.write(f"No Headings found.\n")

        file.close()



    def save_emails(self, directory: str):
        self.console.write(f"\n\n Saving Emails found to {directory}/{urlparse(self.url).netloc}_Emails \n")
        filepath = f"{directory}/{urlparse(self.url).netloc}_Emails_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"
        emails = self.domain.emails

        file = open(filepath, "a+", encoding="utf-8")
        file.write("Email List:\n")
        for index, email in enumerate(emails):
            file.write(f"\t{index + 1}: {email}\n")
            self.console.write(f"{index + 1}: {email}\n")
        else:
            self.console.write("No Emails found.\n")

        file.close()



    def save_links(self, directory: str):
        self.console.write(f"\n\n Saving links found to f{directory}/{urlparse(self.url).netloc}_Links \n")
        filepath = f"{directory}/{urlparse(self.url).netloc}_Links_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"
        links = self.domain.links

        file = open(filepath, "a+", encoding="utf-8")
        file.write("Hyperlink List:\n")
        for index, link in enumerate(links):
            file.write(f"\t{index + 1}: {link}\n")
            self.console.write(f"{index + 1}: {link}\n")
        else:
            self.console.write("No Links found.\n")

        file.close()



    def save_images(self, directory: str):
        self.console.write(f"\n\n Saving Images found to f{directory}/{urlparse(self.url).netloc}_Images \n")
        filepath = f"{directory}/{urlparse(self.url).netloc}_Images_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"
        images = self.domain.images

        file = open(filepath, "a+", encoding="utf-8")
        file.write("Image List:\n")
        for index, image in enumerate(images):
            file.write(f"\t{index + 1}: {image}\n")
            self.console.write(f"{index + 1}: {image}\n")
        else:
            self.console.write("No Images found.\n")

        file.close()


    def save_paragraphs(self, directory: str):
        self.console.write(f"\n\n Saving Paragraphs found to f{directory}/{urlparse(self.url).netloc}_Paragraphs \n")
        filepath = f"{directory}/{urlparse(self.url).netloc}_Paragraphs_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"
        paragraphs = self.domain.paragraphs

        file = open(filepath, "a+", encoding="utf-8")
        file.write("Paragraph List:\n")
        for index, paragraph in enumerate(paragraphs):
            file.write(f"\t{index + 1}: {paragraph}\n")
            self.console.write(f"{index + 1}: {paragraph}\n")
        else:
            self.console.write("No Paragraphs found.\n")

        file.close()


    def save_paragraphs_by_heading(self, directory: str):
        self.console.write(f"\n\n Saving Paragraphs found, organized by headings, to f{directory}/{urlparse(self.url).netloc}_Paragraphs_By_Headings \n")
        filepath = f"{directory}/{urlparse(self.url).netloc}_Paragraphs_By_Headings_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"
        paragraphs_by_headings = self.domain.paragraphs_by_headings

        file = open(filepath, "a+", encoding="utf-8")
        file.write("Paragraph List:\n")
        for index, paragraph in enumerate(paragraphs_by_headings):
            file.write(f"\t{index + 1}: {paragraph}\n")
            self.console.write(f"{index + 1}: {paragraph}\n")
        else:
            self.console.write("No Paragraphs found.\n")

        file.close()


    def save_raw_text(self, directory: str):
        self.console.write(f"\n\n Saving Raw Text found to f{directory}/{urlparse(self.url).netloc}_Raw_Text \n")
        filepath = f"{directory}/{urlparse(self.url).netloc}_Raw_Text_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}.csv"
        raw_text_words = self.domain.raw_text_words

        file = open(filepath, "a+", encoding="utf-8")
        file.write("Raw Text:\n")
        for index, word in enumerate(raw_text_words):
            if word != "" and (word != "\n" or word != "\r" or word != "\t") and word != UnicodeEncodeError and word != UnicodeDecodeError:
                file.write(f"\t{index + 1}: {word}\n")
                self.console.write(f"{index + 1}: {word}\n")
        else:
            self.console.write("No Raw Text found.\n")

        file.close()


    def save_domain_data(self, directory: str):
        self.console.write("\n\n Saving Domain Data to file \n")
        pass


    def get_raw_text(self):
        return self.domain.raw_text_words


    def get_email_list(self) -> set:
        return self.domain.emails


    def get_links(self):
        return self.domain.links


    def get_images(self):
        return self.domain.images


    def get_domain_data(self):
        return self.domain.get_data()
