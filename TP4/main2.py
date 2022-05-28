import json
import numpy as np
from hopfield_network import HopfieldNetwork
import math

with open('letters.json', "r") as letters_file:
    patterns = json.load(letters_file)
    letters_file.close()

patterns = np.array([np.array(pattern).flatten() for pattern in patterns])
best = []
min_dist = math.inf
for i in range(len(patterns) - 3):
    for j in range(i+1, len(patterns) - 2):
        i_j = np.dot(patterns[i], patterns[j])
        for k in range(j+1, len(patterns) - 1):
            i_k = np.dot(patterns[i], patterns[k])
            j_k = np.dot(patterns[j], patterns[k]) 
            for l in range(k+1, len(patterns)):
                i_l = np.dot(patterns[i], patterns[l])
                j_l = np.dot(patterns[j], patterns[l])
                k_l = np.dot(patterns[k], patterns[l])
                dist = sum([i_j, i_k, j_k, i_l, j_l, k_l])
                if dist < min_dist:
                    min_dist = dist
                    best = [i, j, k, l]


print([chr(ord('A') + i) for i in best])
patterns = [patterns[i] for i in best]
network = HopfieldNetwork(size=25, patterns=patterns)

noisy_patterns = np.copy(patterns)
for i in range(len(noisy_patterns)):
    for j in range(len(noisy_patterns[i])):
        if np.random.rand() < 0.05:
            noisy_patterns[i][j] = -noisy_patterns[i][j]

# print(noisy_patterns[1])
res, historic = network.solve(noisy_patterns[1])
for i in range(5):
    print(res[5*i: 5*(i+1)])
    
for idx, his in enumerate(historic):
    print("Paso", idx, ":")
    for i in range(5):
        print(his[5*i: 5*(i+1)])

# noisy_p = patterns[0]
# for i in range(len(noisy_p)):
#     if np.random.rand() < 0.3:
#         noisy_p[i] = -noisy_p[i]

# res, historic = network.solve(noisy_p)

# for idx, his in enumerate(historic):
#     print("Paso", idx, ":")
#     for i in range(5):
#         print(his[5*i: 5*(i+1)])

# # for i in range(5):
# #     print(res[5*i: 5*(i+1)])
