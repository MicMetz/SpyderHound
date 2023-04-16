class Target:
    data: object = None
    url: str = "None"
    name: str = "None"


    def __init__(self, data=None, name="None"):
        self.data = data
        self.url = name
        self.name = name
        # self.images = data.images
        # self.links = data.links
        # self.emails = data.emails
        # self.headings = data.headings
        # self.paragraphs = data.paragraphs
        # self.paragraphs_by_headings = data.paragraphs_by_headings
