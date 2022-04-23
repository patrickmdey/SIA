import numpy as np
import math
from plotter import plot


class SimplePerceptron:
    def __init__(self, limit):
        self.limit = limit

    def solve(self, training_set, correct_output, solve_type: dict):  # training_set: x, correct_output: y
        p = len(training_set)
        iteration = 0
        eta = 0.5  # tasa de aprendizaje
        w = np.zeros(len(training_set[0]))
        error = 1
        min_error = p * 2
        w_min = np.zeros(len(training_set[0]))
        weights = []

        while error > 0 and iteration < self.limit:
            iteration += 1
            i_x = np.random.randint(0, p)

            excitement = np.dot(training_set[i_x], w)
            activation = solve_type["activation"](excitement)

            for i in range(0, len(w)):
                delta_w = eta * (correct_output[i_x] - activation) * training_set[i_x][i] * (solve_type["mult"](excitement) if solve_type["mult"] != 1 else 1)
                w[i] += delta_w

            error =solve_type["error"](training_set, correct_output, w, p)
            print(error)
            if error < min_error:
                min_error = error
                w_min = w

            weights.append(np.copy(w))
            # print(w)
        
        plot(training_set, correct_output, weights, "Simple Perceptron")

        print("Iteration " + str(iteration))
        if iteration == self.limit:
            w = w_min
        print(error)
        print(w)
        return w
