import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

# hyperparameters
input_size = 28 * 28
hidden_szie = 100
num_classes = 10
n_epochs = 3
batch_size = 100
learning_rate = 0.001

# transformers
transform = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
)

# MNIST
train_dataset = torchvision.datasets.MNIST(
    root="./Mnist",  # path to save data
    train=True,
    transform=transform,
    download=True,  # if it not available download it
)

test_dataset = torchvision.datasets.MNIST(
    root="./Mnist", train=False, transform=transform
)

train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)

test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=True)


# define model
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_szie, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_szie)
        self.relu = nn.ReLU()
        self.l2 = nn.Linear(hidden_szie, num_classes)

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        return out


model = NeuralNet(input_size, hidden_szie, num_classes)
loss = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
n_total_steps = len(train_loader)

# training
for epoch in range(n_epochs):
    for i, (images, labels) in enumerate(train_loader):
        # reshpae 100*1*28*28 => 100 * 784
        images = images.reshape(-1, 28 * 28)

        # forward
        outputs = model(images)

        # loss
        l = loss(outputs, labels)
        l.backward()

        # update parameters
        optimizer.step()
        optimizer.zero_grad()

        _, pred = torch.max(outputs, 1)

        if (i + 1) % 100 == 0:
            print(
                f"epoch: {epoch}/{n_epochs}",
                f"step: {i+1}/{n_total_steps}",
                f"loss: {l.item():.3f}",
            )


# test
with torch.no_grad():
    n_samples = 0
    n_corrects = 0
    for images, labels in test_loader:
        images = images.reshape(-1, 28 * 28)

        outputs = model(images)

        # valeu, index
        _, predictions = torch.max(outputs, 1)
        n_samples += labels.shape[0]
        n_corrects += (predictions == labels).sum()

    acc = 100 * n_corrects / n_samples
    print(f"Accuracy on test images: {acc}")


torch.save(model.state_dict(), "mnist_ffn.pth")
