import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from RL_library import return_pointwise_A
np.random.seed(0)

##### plot_two_agents #####
# plots two agents at i, j
# with s = size
# and color 1 and color 2
def plot_two_agents(i, j, size, color1, color2):
    # ix, and iy are calculated by converting the point i into and x, y pair
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

##### one_step #####
# one action for agents at state i and j following
# policy pi
# given the allowance for sim(ultaneous) moves
def one_step(i, j, pi, sim):
    A = return_pointwise_A(i, j, sim)
    chosen_action_id = pi[i, j]
    action = A[chosen_action_id]
    iprime, jprime = np.array([i, j]) + action
    return iprime, jprime


#### The main program #####

#### 1. initialization #####
sim = True # True is simultaneous motion of particles are allowed 
policyfilename = 'optimal_pi.dat'

# 1.1 reading the policy
pi = np.loadtxt(policyfilename)
pi = np.array(pi, dtype = int)
n, n = np.shape(pi)

# 1.2 initial position of the agents
i = 0
j = 8


# 1.3 plotting the grid 
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


#### 2. simulation  ####

step = 0
plt.savefig('state_000.png')
while (i!=8 or j!=0): # while the agents haven't arrived at their desired positions
    # 2.1 one step following the policy
    step += 1
    iprime, jprime = one_step(i, j, pi, sim)

    # 2.2 checking if they have arrived
    #if they arrive they dont leave anymore; not a major intervation
    if (j == 0): 
        jprime = 0
    if (i == 8):
        iprime = 8

    # 2.3 plotting
    plot_two_agents(i, j, 100, '#C1C7C9', '#C1C7C9') # plotting gray traces of the agents
    plot_two_agents(iprime, jprime, 100, 'red', 'blue') # plotting the agents in their new states
    plt.pause(0.1)

    # 2.4 updating the position of the agents
    i = iprime
    j = jprime
    if (step < 10):
        filename = 'state_00'+str(step)+'.png'
    elif (step < 100):
        filename = 'state_0'+str(step)+'.png'
    elif (step < 1000):
        filename = 'state_'+str(step)+'.png'
    plt.savefig(filename)
