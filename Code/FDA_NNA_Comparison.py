import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

x=np.load("x.npy")
t=np.load("t.npy")
u_true=np.load("u.npy")

model=nn.Sequential(
    nn.Linear(2,32),
    nn.Tanh(),
    nn.Linear(32,32),
    nn.Tanh(),
    nn.Linear(32,1)
    )

model.load_state_dict(torch.load("NNA.pth"))
model.eval()

X,T=np.meshgrid(x,t)

inputs=np.column_stack((X.flatten(),T.flatten()))
inputs=torch.tensor(inputs,dtype=torch.float32)

with torch.no_grad():
    predictions=model(inputs)

u_nn=predictions.numpy().reshape(len(t),len(x))

mse=np.mean((u_true-u_nn)**2)
print("Mean Squared Error =",mse)

times=[1,250,500,750,999]
for k in times:
    plt.figure(figsize=(8,5))
    plt.plot(x,u_true[k],label="Finite Difference",linewidth=3)
    plt.plot(x,u_nn[k],"--",label="Neural Network",linewidth=2)
    plt.xlabel("x")
    plt.ylabel("u(x,t)")
    plt.title(f"Comparison at t={t[k]:.2f}")
    plt.legend()
    plt.show()

plt.figure(figsize=(8,5))
plt.imshow(
    np.abs(u_true-u_nn),
    aspect="auto",
    origin="lower",
    extent=[0,1,0,1]
    )
plt.colorbar(label="Absolute Error")
plt.xlabel("x")
plt.ylabel("t")
plt.title("Neural Network Error")
plt.show()