import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
from PIL import Image
import io


# hyperparameters
input_size = 28 * 28
hidden_szie = 100
num_classes = 10


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


# load model
PATH = "mnist_ffn.pth"
model = NeuralNet(input_size, hidden_szie, num_classes)
model.load_state_dict(torch.load(PATH))
model.eval()


# transfrom input image
def transform_image(image_bytes):

    transform = transforms.Compose(
        [
            transforms.Grayscale(num_output_channels=1),  # maybe input imag is RGB
            transforms.Resize((28, 28)),
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,)),
        ]
    )

    image = Image.open(io.BytesIO(image_bytes))
    return transform(image).unsqueeze(0)


# predict
def get_prediction(image_tensor):

    image = image_tensor.reshape(-1, 28 * 28)
    outputs = model(image)
    # valeu, index
    _, predicted = torch.max(outputs, 1)

    return predicted
