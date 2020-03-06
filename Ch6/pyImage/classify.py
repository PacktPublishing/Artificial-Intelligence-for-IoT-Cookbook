import numpy as np
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from torchvision import datasets, transforms, models
from torch.utils.data.sampler import SubsetRandomSampler
    

datadir = './data/train'
valid_size = .3
epochs = 3
steps = 0
running_loss = 0
print_every = 10
train_losses, test_losses = [], []

def print_score(torch, testloader, inputs, device, model,criterion,labels):
    test_loss = 0
    accuracy = 0
    model.eval()
    
    with torch.no_grad():
        for inputs, labels in testloader:
            inputs, labels = inputs.to(device), labels.to(device)
            logps = model.forward(inputs)
            batch_loss = criterion(logps, labels)
            test_loss += batch_loss.item()

            ps = torch.exp(logps)
            top_p, top_class = ps.topk(1, dim=1)
            equals = top_class == labels.view(*top_class.shape)
            accuracy += torch.mean(equals.type(torch.FloatTensor)).item()
    train_losses.append(running_loss/len(trainloader))
    test_losses.append(test_loss/len(testloader))                    
    print(f"Epoch {epoch+1}/{epochs} Train loss: {running_loss/print_every:.3f} Test loss: {test_loss/len(testloader):.3f} Test accuracy: {accuracy/len(testloader):.3f}")
    
    return test_loss, accuracy


train_transforms = transforms.Compose([transforms.Resize(224),transforms.ToTensor()])
test_transforms = transforms.Compose([transforms.Resize(224), transforms.ToTensor()])
train_data = datasets.ImageFolder(datadir, transform=train_transforms)
test_data = datasets.ImageFolder(datadir, transform=test_transforms)
num_train = len(train_data)
indices = list(range(num_train))
split = int(np.floor(valid_size * num_train))
np.random.shuffle(indices)
train_idx, test_idx = indices[split:], indices[:split]
train_sampler = SubsetRandomSampler(train_idx)
test_sampler = SubsetRandomSampler(test_idx)
trainloader = torch.utils.data.DataLoader(train_data, sampler=train_sampler, batch_size=1)
testloader = torch.utils.data.DataLoader(test_data, sampler=test_sampler, batch_size=1)

print(trainloader.dataset.classes)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet50(pretrained=True)

for param in model.parameters():
    param.requires_grad = False
    
model.fc = nn.Sequential(nn.Linear(2048, 512), nn.ReLU(), nn.Dropout(0.2), nn.Linear(512, 10), nn.LogSoftmax(dim=1))
criterion = nn.NLLLoss()
optimizer = optim.Adam(model.fc.parameters(), lr=0.003)
model.to(device)



for epoch in range(epochs):
    for inputs, labels in trainloader:
        steps += 1
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()
        logps = model.forward(inputs)
        loss = criterion(logps, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
        
        if steps % print_every == 0:
            test_loss, accuracy = print_score(torch, testloader, inputs, device, model,criterion,labels)
            running_loss = 0
            model.train()
torch.save(model, 'saftey.pth')


