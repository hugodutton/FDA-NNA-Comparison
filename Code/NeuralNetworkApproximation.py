import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

x=np.load("x.npy")
t=np.load("t.npy")
u=np.load("u.npy")

X,T=np.meshgrid(x,t)

inputs=np.column_stack((X.flatten(),T.flatten()))
targets=u.flatten().reshape(-1,1)

inputs=torch.tensor(inputs,dtype=torch.float32)
targets=torch.tensor(targets,dtype=torch.float32)

model=nn.Sequential(
    nn.Linear(2,32),
    nn.Tanh(),
    nn.Linear(32,32),
    nn.Tanh(),
    nn.Linear(32,1)
    )

loss_function=nn.MSELoss()

optimiser=torch.optim.Adam(model.parameters(),lr=0.001)

losses=[]
epochs=1000
for epoch in range(epochs):
    predictions=model(inputs)
    loss=loss_function(predictions,targets)
    optimiser.zero_grad()
    loss.backward()
    optimiser.step()
    losses.append(loss.item())
    if epoch %250==0:
        print(
            f"Epoch {epoch}, "
            f"Loss={loss.item():.6f}"
        )

torch.save(model.state_dict(),"NNA.pth")

plt.plot(losses)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss")
plt.show()