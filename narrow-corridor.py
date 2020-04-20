import numpy as np
np.random.seed(0)
import matplotlib.pyplot as plt
from RL_library import return_pointwise_A
from RL_library import Bellmann_iteration
from RL_library import Q_estimation_for_state_s

# Inputs
n = 10 #grid size along each direction
sim = True #if True particles can move simultaneously

# Policy $\pi$
pi = np.random.random_integers(low=0, high=4, size=(n, n))
print(pi)
np.savetxt('original_pi.dat', pi)

# values, v
v = np.zeros(shape=(n, n))

# reward
r = np.full((n, n), 0)

r[n-2, 0] = 1

# discount
gamma = 0.99

# policy evaluation
niteration = 0
for iteration in range(0, niteration):
    v = Bellmann_iteration(n, pi, r, v, gamma, sim)
print v
print(return_pointwise_A(4, 5, sim))
#input("Press Enter to continue...")
# policy improvement
niteration = 500
v = np.zeros(shape=(n, n))
step = 0
while (step < 500):
    new_pi = np.zeros(shape=(n, n)) 
    # policy evaluation
    v = Bellmann_iteration(n, pi, r, v, gamma, sim)
    # policy iteration
    for i in range(0, n):
        for j in range(0, n):
            Q_max = -1000
            A = return_pointwise_A(i, j, sim)
            nr_actions = np.size(A, 0)
            for candidate_action_id in range(0, nr_actions): #iterate over all candidate to find the largest Q
                Q = Q_estimation_for_state_s(i, j, gamma, r, v, candidate_action_id, sim)
                if Q >= Q_max :
                    Q_max = Q
                    new_pi[i, j] = candidate_action_id
    pi = new_pi + 0.0
    step += 1
    if (step%100 == 1):
        print("#iteration: "+str(step-1))
print(pi)        
print(v)
plt.imshow(v)
plt.show()

np.savetxt('optimal_pi.dat', pi)
