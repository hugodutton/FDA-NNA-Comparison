# Comparing Finite Difference Approximation and Neural Network Approximation of the 1-Dimensional Heat Equation

## Finite Difference Approximation of the 1-Dimensional Heat Equation

Let $u(x,t)$ be the temperature of a rod depending on position $x$ and time $t$, then the 1-dimensional heat equation is given by
\begin{align}
    \frac{\partial u(x,t)}{\partial t}=\alpha\frac{\partial^2u(x,t)}{\partial x^2},
\end{align}
where $\alpha=0.01$ is the thermal diffusivity of the rod and $x,t\in[0,1]$ and
\begin{align}
    u(0,t)=u(1,t)=0,&&u(x,0)=\exp\left(-100\left(x-0.5\right)^2\right),
    \nonumber
\end{align}
then let
\begin{align}
    x_i&=i\Delta x,&&i\in\{0,1,\dots,100\},
    \nonumber\\
    t_n&=n\Delta t,&&n\in\{0,1,\dots,1000\},
    \nonumber
\end{align}
and
\begin{align}
    u_i^n\approx u(x_i,t_n),
    \nonumber
\end{align}
then
\begin{align}
    \frac{\partial u(x,t)}{\partial t}&\approx\frac{u_i^{n+1}-u_i^n}{\Delta t},
    \nonumber\\
    \frac{\partial^2u(x,t)}{\partial x^2}&\approx\frac{u_{i+1}^n-2u_i^n+u_{i-1}^n}{\left(\Delta x\right)^2},
    \nonumber
\end{align}
then
\begin{align}
    \frac{\partial u(x,t)}{\partial t}=\alpha\frac{\partial^2u(x,t)}{\partial x^2}&&\iff&&\frac{u_i^{n+1}-u_i^n}{\Delta t}=\alpha\frac{u_{i+1}^n-2u_i^n+u_{i-1}^n}{\left(\Delta x\right)^2}&&\iff&&u_i^{n+1}=u_i^n+r\left(u_{i+1}^n-2u_i^n+u_{i-1}^n\right),
    \nonumber
\end{align}
where $r=\frac{\alpha\Delta t}{\left(\Delta x\right)^2}$ is the diffusion number.
