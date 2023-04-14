import datetime
import tkinter as tk

from core.Domain import Domain
from urllib.parse import urlparse

from core.ui.OutputTerminal import OutputTerminal



class LogController:
    pass


class Controller():
    master: tk.Tk = None
    url: str = None
    domain: Domain = None
    console: OutputTerminal = None


    # logController: LogController = None
    def __init__(self, root, frame):
        self.parent = root
        self.console = OutputTerminal(self, frame)


    def switch_console(self, console: OutputTerminal):
        self.console = console


    def set_domain_url(self):
        self.domain = Domain(self.url)


    def save_headings(self, directory: str):
        headings = self.domain.headings
        filepath = f"{directory}/{urlparse(self.url).netloc}_Headings_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}.txt"
        f = open(filepath, "a+")
        f.write("Heading List:\n")
        for heading in headings:
            f.write("\t" + heading + "\n")
        f.close()


    def save_emails(self, directory: str):
        self.console.insert(tk.END, f"Saving Emails found to {directory}/{urlparse(self.url).netloc}_Emails \n")
        emails = self.domain.emails

        if len(emails) > 0:
            self.console.insert(tk.END, f"Emails found!\n")
            filepath = f"{directory}/{urlparse(self.url).netloc}_Emails_{datetime.datetime.now().strftime('%Y-%m-%d_%H')}.txt"
            file = open(filepath, "a+")
            file.write("Email List:\n")
            for email in emails:
                file.write("\t" + email + "\n")
                self.console.insert(tk.END, f"{email}\n")
            file.close()
        else:
            self.console.insert(tk.END, f"No Email found.\n")


    def save_links(self, directory: str):
        self.console.insert(tk.END, f"Saving links found to f{directory}/{urlparse(self.url).netloc}_Links \n")
        links = self.domain.links

        if len(links) > 0:
            self.console.insert(tk.END, f"Links found!\n")
            filepath = f"{directory}/{urlparse(self.url).netloc}_Links_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}.txt"
            file = open(filepath, "a+")
            file.write("Link List:\n")
            for link in links:
                file.write("\t" + link + "\n")
                self.console.insert(tk.END, f"{link}\n")
            file.close()
        else:
            self.console.insert(tk.END, f"No Links found.\n")


    def save_images(self, directory: str):
        self.console.insert(tk.END, f"Saving Images found to f{directory}/{urlparse(self.url).netloc}_Images \n")
        images = self.domain.images

        if len(images) > 0:
            self.console.insert(tk.END, f"Images found!\n")
            filepath = f"{directory}/{urlparse(self.url).netloc}_Images_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}.txt"
            file = open(filepath, "a+")
            file.write("Link List:\n")
            for image in images:
                file.write("\t" + image + "\n")
                self.console.insert(tk.END, f"{image}\n")
            file.close()
        else:
            self.console.insert(tk.END, f"No Images found.\n")


    def save_paragraphs(self, directory: str):
        self.console.insert(tk.END, f"Saving Paragraphs found to f{directory}/{urlparse(self.url).netloc}_Paragraphs \n")
        paragraphs = self.domain.paragraphs

        if len(paragraphs) > 0:
            self.console.insert(tk.END, f"Paragraphs found!\n")
            filepath = f"{directory}/{urlparse(self.url).netloc}_Paragraphs_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}.txt"
            file = open(filepath, "a+")
            file.write("Paragraph List:\n")
            for paragraph in paragraphs:
                file.write("\t" + paragraph + "\n")
                self.console.insert(tk.END, f"{paragraph}\n")
            file.close()
        else:
            self.console.insert(tk.END, f"No Paragraphs found.\n")


    def save_paragraphs_by_heading(self, directory: str):
        self.console.insert(tk.END, f"Saving Paragraphs found to f{directory}/{urlparse(self.url).netloc}_Paragraphs \n")
        paragraphs_by_headings = self.domain.paragraphs_by_headings

        if len(paragraphs_by_headings) > 0:
            self.console.insert(tk.END, f"Paragraphs found!\n")
            filepath = f"{directory}/{urlparse(self.url).netloc}_Paragraphs_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')}.txt"
            file = open(filepath, "a+")
            file.write("Paragraph List:\n")
            for heading, paragraphs in paragraphs_by_headings.items():
                file.write("\t" + heading + "\n")
                self.console.insert(tk.END, f"{heading}\n")
                for paragraph in paragraphs:
                    file.write("\t\t" + paragraph + "\n")
                    self.console.insert(tk.END, f"\t{paragraph}\n")
            file.close()
        else:
            self.console.insert(tk.END, f"No Paragraphs found.\n")


    def get_text(self):
        (whole_text, headings, paragraphs) = (self.domain.paragraphs, self.domain.headings, self.domain.paragraphs_by_headings)
        return (whole_text, headings, paragraphs)


    def get_email_list(self) -> set:
        return self.domain.emails


    def get_links(self):
        return self.domain.links


    def get_images(self):
        return self.domain.images


    def get_domain_data(self):
        return self.domain.get_data()
