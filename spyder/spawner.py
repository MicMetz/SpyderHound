from spyder.spyder import ChanSpyder, Spyder, ReddSpyder, TwitSpyder



class SpyderSpawner:
    def __init__(self):
        self.crawler_breed = None
        self.crawler = None
        self.crawlers = []


    def spawn(self, crawler_breed, crawler_properties=None) -> Spyder:
        if crawler_properties is None:
            crawler_properties = {}
        crawler = None
        match crawler_breed:
            case "Chan":
                crawler = ChanSpyder(crawler_properties["project_name"], crawler_properties["base_url"], crawler_properties["domain_name"])
            case "Redd":
                crawler = ReddSpyder(crawler_properties["project_name"], crawler_properties["base_url"], crawler_properties["domain_name"])
            case "Twit":
                crawler = TwitSpyder(crawler_properties["project_name"], crawler_properties["base_url"], crawler_properties["domain_name"])
            case "Gen":
                crawler = Spyder(crawler_properties["project_name"], crawler_properties["base_url"], crawler_properties["domain_name"])

        return crawler


    def start(self):
        self.crawler = self.spawn("Gen", crawler_properties = {"project_name": "test", "base_url": "https://www.google.com", "domain_name": "google.com"})
        self.crawlers.append(self.crawler)
        return self.crawler
