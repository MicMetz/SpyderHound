from pandas import DataFrame



class AnnaFrame:
# class AnnaFrame(DataFrame):
    name: str = "None"
    description: str = "No description"
    index: list = []
    columns: list = []
    data: list = []
    dtype: None = None
    copy: bool = False


    def __init__(self, name="None", description=None, data=None, index=None, columns=None, dtype=None, copy=False):
        # super().__init__(data, index, columns, dtype, copy)
        self.name = name
        self.description = description
        self.index = index
        self.columns = columns
        self.data = data
        self.dtype = dtype
        self.copy = copy
        self.asynchronous = False


    def __str__(self):
        stringify = f"Name: {self.name}\nDescription: {self.description}\nIndex: {self.index}\nColumns: {self.columns}\nData: {self.data}\nDtype: {self.dtype}\nCopy: {self.copy}"
        return stringify


    def switch_async(self):
        self.asynchronous = not self.asynchronous


    def is_async(self):
        return self.asynchronous


    def on_update(self):
        pass


    def display(self, console):
        console.write(self.__str__())
        console.write("\n")


    async def display_async(self, console):
        console.write(self.__str__())
        console.write("\n")
