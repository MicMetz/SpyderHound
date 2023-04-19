from datetime import date as dt
from torch.utils.data import Dataset
from torch.utils.data import DataLoader



class DataSet(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
        self.name = "None"


    def __getitem__(self, index) -> object:
        return self.data[index], self.labels[index]


    def __len__(self):
        return len(self.data)


    def getLength(self):
        return len(self.data)
