import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from RL_library import return_pointwise_A
np.random.seed(0)

def plot_one_man(i, j, size, color1, color2):
    iy = jy = 0 
    ix = i
    jx = j
    if (i == 9):
        ix = 2
        iy = 1
    if (j == 9):
        jx = 2
        jy = 1
    plt.scatter(ix, iy, s=size, c=color1)
    plt.scatter(jx, jy, s=size, c=color2)


def one_random_step(i, j, sim):
    A = return_pointwise_A(i, j, sim)
    nA = np.size(A, 0)
    chosen_action_id = np.random.randint(low=0, high=nA)
    action = A[chosen_action_id]
    iprime, jprime = np.array([i, j]) + action
    return iprime, jprime

sim = True # True is simultaneous motion of particles are allowed 
n = 10
# simulation loop
i = 0
j = 8
plt.close('all')
plt.ion()
for x in range(0,9):
    plt.scatter(x, 0, s=750, c='white', marker='s',linewidths=1, edgecolor='black' )
plt.scatter(2, 1, s=750, c='white', marker='s',linewidths=1, edgecolor='black' )
plt.scatter(i, 0, s=100, c='red')
plt.scatter(j, 0, s=100, c='blue')
plt.axis([-2, n+1, -2, 3])
plt.axes().set_aspect('equal')
plt.scatter(i, j, c='red')
step = 0
plt.savefig('state_000.png')
while (i!=8 or j!=0):
    step += 1
    iprime, jprime = one_random_step(i, j, sim)

    #if they arrive they dont leave anymore; not a major intervation
    if (j == 0): 
        jprime = 0
    if (i == 8):
        iprime = 8

    plot_one_man(i, j, 100, '#C1C7C9', '#C1C7C9')
    plot_one_man(iprime, jprime, 100, 'red', 'blue')

    
    plt.pause(0.1)
    i = iprime
    j = jprime
    if (step < 10):
        filename = 'state_00'+str(step)+'.png'
    elif (step < 100):
        filename = 'state_0'+str(step)+'.png'
    elif (step < 1000):
        filename = 'state_'+str(step)+'.png'
    plt.savefig(filename)
