import numpy as np
import matplotlib.pyplot as plt

alpha=0.01

L=1
nx=100
dx=L/(nx-1)

T=1
nt=1000
dt=T/nt

r=alpha*dt/dx**2

print("r=",r)

if r>0.5:
    raise ValueError("Unstable: r>0.5")

x=np.linspace(0,L,nx)

t=np.linspace(0,T,nt)

u=np.zeros((nt,nx))

u[0,:]=np.exp(-100*(x-0.5)**2)

for n in range(0,nt-1):
    for i in range(1,nx-1):
        u[n+1,i]=u[n,i]+r*(u[n,i+1]-2*u[n,i]+u[n,i-1])

np.save("x.npy",x)
np.save("t.npy",t)
np.save("u.npy",u)

times=[1,250,500,750,999]
for k in times:
    plt.plot(x,u[k],label=f"t={t[k]:.2f}")
plt.xlabel("x")
plt.ylabel("u(x,t)")
plt.legend()
plt.title("Finite Difference Approximation of Heat Equation")
plt.show()