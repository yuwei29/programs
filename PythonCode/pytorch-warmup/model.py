import torch
import torch.nn as nn
class Value(nn.Module):
    def __init__(self):
        super(Value, self).__init__()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(9,9),
            nn.ReLU(),
            nn.Linear(9,3),
            nn.ReLU(),
            nn.Linear(3, 1),
        )

    def forward(self, x):
        x = self.linear_relu_stack(x)
        return x
valueNN_Black = Value()
valueNN_White = Value()
def value(board,color):
    if color=='black':
        res = valueNN_Black(board)
    else:
        res = valueNN_White(board)
    if res>1:
        return 1
    elif res<-1:
        return -1
    else:
        return res
epochs = 100
loss_fn = nn.MSELoss()
learning_rate = 1e-3
optimizerB = torch.optim.SGD(valueNN_Black.parameters(), lr=learning_rate)
optimizerW = torch.optim.SGD(valueNN_White.parameters(), lr=learning_rate)
def updateModel(color,board,newValue):
    if color=='black':
        for i in range(epochs):
            pred = valueNN_Black(board)
            loss = loss_fn(pred,newValue)
            predW = valueNN_White(board)
            lossW = loss_fn(predW,-newValue)
            
            optimizerB.zero_grad()
            optimizerW.zero_grad()
            loss.backward()
            lossW.backward()
            optimizerB.step()
            optimizerW.step()
    else:
        for i in range(epochs):
            pred = valueNN_White(board)
            loss = loss_fn(pred,newValue)
            predB = valueNN_Black(board)
            lossB = loss_fn(predB,-newValue)
            
            optimizerB.zero_grad()
            optimizerW.zero_grad()
            loss.backward()
            lossB.backward()
            optimizerB.step()
            optimizerW.step()
