import torch
import torchvision
from torchvision import transforms, datasets
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import matplotlib.pyplot as plt

train = datasets.MNIST('', train=True, download=True, transform=transforms.Compose([transforms.ToTensor()]))
test = datasets.MNIST('', train=False, download=True, transform=transforms.Compose([transforms.ToTensor()]))

train_set = torch.utils.data.DataLoader(train, batch_size=16, shuffle=True)
test_set = torch.utils.data.DataLoader(test, batch_size=16, shuffle=True)

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28 * 28, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 64)
        self.fc4 = nn.Linear(64, 10)
    
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return F.log_softmax(x, dim=1)

net = Net()
optimiser = optim.Adam(net.parameters(), lr=1e-3)

# EPOCHS = 3
# for epoch in range(EPOCHS):
#     for data in train_set:
#         X, y = data
#         net.zero_grad()
#         output = net(X.view(-1, 28*28))
#         loss = F.nll_loss(output, y)
#         loss.backward()
#         optimiser.step()
#     print(loss)

correct = 0
total = 0

with torch.no_grad():
    for data in train_set:
        X, y = data
        output = net(X.view(-1, 28*28))
        for idex, i in enumerate(output):
            if torch.argmax(i) == y[idex]:
                correct += 1
            total += 1
print("Accuracy:", round(correct/total, 3))

plt.imshow(X[0].view(28, 28))
plt.show()
print(torch.argmax(net(X[0].view(-1, 28*28))[0]))