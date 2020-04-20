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


def one_directed_step(i, j, sim):
    A = return_pointwise_A(i, j, sim)
    rand = np.random.rand()
    nA = np.size(A, 0)
    exist = False # it turns into True if the element np.array([[1, -1]]) exists
    for fuck in range(0, nA):
        exist = np.array_equal(A[fuck], np.array([1, -1])) or exist

    if (rand > 0. and exist): #if it is possible to go take (1, -1) with a probability of 100% it takes it
        action = np.array([1, -1])
    else:
        chosen_action_id = np.random.randint(low=0, high=nA)
        action = A[chosen_action_id]
    print("action")
    print(action)  
    iprime, jprime = np.array([i, j]) + action
    print("iprime = "+str(iprime)+"  jprime = "+str(jprime))
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
step=0
while (i!=8 or j!=0 and step<1):
    step += 1
    iprime, jprime = one_directed_step(i, j, sim)

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
