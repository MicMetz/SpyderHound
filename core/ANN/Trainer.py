import torch as torch




class Trainer:

    def __init__(self, model, optimizer, criterion, scheduler=None):
        self.model = model
        self.optimizer = optimizer
        self.criterion = criterion
        self.scheduler = scheduler


    def train(self, train_loader, val_loader, epochs, device):
        train_loss = []
        val_loss = []

        for epoch in range(epochs):
            self.model.train()
            running_loss = 0.0

            for i, (inputs, labels) in enumerate(train_loader):
                inputs = inputs.to(device)
                labels = labels.to(device)
                self.optimizer.zero_grad()
                outputs = self.model(inputs)
                loss = self.criterion(outputs, labels)
                loss.backward()
                self.optimizer.step()
                running_loss += loss.item()

            if self.scheduler is not None:
                self.scheduler.step()

            train_loss.append(running_loss / len(train_loader))
            val_loss.append(self.validate(val_loader, device))
            print('Epoch: {} tTraining Loss: {:.6f} tValidation Loss: {:.6f}'.format(epoch, train_loss[-1], val_loss[-1]))

            return train_loss, val_loss


        def validate(self, val_loader, device):
            self.model.eval()
            running_loss = 0.0

            for i, (inputs, labels) in enumerate(val_loader):
                inputs = inputs.to(device)
                labels = labels.to(device)
                outputs = self.model(inputs)
                loss = self.criterion(outputs, labels)
                running_loss += loss.item()

            return running_loss / len(val_loader)


        def test(self, test_loader, device):
            self.model.eval()
            running_loss = 0.0

            for i, (inputs, labels) in enumerate(test_loader):
                inputs = inputs.to(device)
                labels = labels.to(device)
                outputs = self.model(inputs)
                loss = self.criterion(outputs, labels)
                running_loss += loss.item()

            return running_loss / len(test_loader)


        def predict(self, test_loader, device):
            self.model.eval()
            predictions = []

            for i, inputs in enumerate(test_loader):
                inputs = inputs.to(device)
                outputs = self.model(inputs)
                _, predicted = torch.max(outputs.data, 1)
                predictions.append(predicted)

            return predictions


        def evaluate(self, test_loader, device):
            self.model.eval()
            correct = 0
            total = 0

            with torch.no_grad():
                for i, (inputs, labels) in enumerate(test_loader):
                    inputs = inputs.to(device)
                    labels = labels.to(device)
                    outputs = self.model(inputs)
                    _, predicted = torch.max(outputs.data, 1)
                    total += labels.size(0)
                    correct += (predicted == labels).sum().item()

            return correct / total
