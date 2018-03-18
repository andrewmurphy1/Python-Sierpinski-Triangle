import matplotlib.pyplot as plt
import random as rand

nx = [0.5] # initial x value
ny = [0.5] # initial y value

tx = [0,0.5,1] # limiting triangle x values 
ty = [0,1,0] # limiting triangle x values 

for i in range(1, 10000): # loop 
  ri = rand.randint(0,2) # random integer from 0 to 2
  x = 0.5*(nx[i-1] + tx[ri])
  y = 0.5*(ny[i-1] + ty[ri])
  nx.append(x)
  ny.append(y)

plt.plot(tx, ty, ls='None', color='r', marker='^', ms=10)
plt.plot(nx, ny, ls='None', marker='.', ms=1)
plt.grid(True)
plt.xlim(-0.1,1.1)
plt.ylim(-0.1,1.1)
plt.show()
