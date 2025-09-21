import math as m
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

V = np.arange(0.1,50.1)
T1 = 200
T2 = 300
p1 = []
p2 = []

T13 = T1*T1*T1
T23 = T2*T2*T2

for i in range(len(V)):
    y1 = m.sqrt(T13/(V[i]*V[i]))
    y2 = m.sqrt(T23/(V[i]*V[i]))
    p1.append(y1)
    p2.append(y2)

fig, ax = plt.subplots()
ax.plot(V,p2, color='red', label='T = 300 K')
ax.plot(V,p1, color='blue', label='T = 200 K')

ax.set(xlabel='Volume (m^3)', ylabel='Pressão (N/m2)', title='Gráficos de PxV a Temperaturas Constantes')
ax.grid()

plt.legend(loc='upper right')

fig.savefig("PxV3.jpg")
plt.show()
