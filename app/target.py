class Target:
    """
        Target class
        - name: name of target
        - url: url of target
        - type: type of target
        - data: data on target

    """

    def __init__(self, name="None", url="", type="None"):
        self.name = name
        self.url = url
        self.type = type
        self.data = None
