import torch
import torch.nn as nn



class HateClassifier(nn.ModuleList):
    def __init__(self, input_size, hidden_size, output_size, num_layers, dropout):
        super(HateClassifier, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.num_layers = num_layers
        self.dropout = dropout
        self.embedding = nn.Embedding(input_size, hidden_size)

        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, dropout=dropout, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)



    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        torch.nn.init.xavier_uniform_(h0)
        torch.nn.init.xavier_uniform_(c0)

        output, (hn, cn) = self.lstm(x, (h0, c0))
        output = self.dropout(output)
        output = torch.relu(self.fc(output))
        output = self.dropout(output)
        output = torch.sigmoid(self.fc(output))
        return output
