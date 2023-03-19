class Searcher:
    """
    Search input handler
    """

    @staticmethod
    def search(raw):
        """
        :param raw:
        :type raw:
        :return:
        :rtype:
        """
        search = raw.strip().lower()
        tar = Searcher.format_search(search)
        return tar



    @staticmethod
    def format_search(search):
        """
        Format input string to be used in URL
        :param search:
        :type search:
        :return:
        :rtype:
        """
        import re
        return re.sub(" ", "-", search)
