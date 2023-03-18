from spyder.spyder import ChanSpyder, Spyder, ReddSpyder, TwitSpyder



class SpyderSpawner:
    def __init__(self):
        self.crawler_breed = None
        self.crawler = None

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

        return crawler
