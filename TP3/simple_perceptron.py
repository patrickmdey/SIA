import numpy as np
import math


class SimplePerceptron:
    def __init__(self, limit, error, threshold) -> None:
        self.limit = limit
        self.error = error
        self.threshold = threshold

    def solve(self, training_set, correct_output, activation_func):  # inset: x, correct_output: y
        p = len(training_set)
        iteration = 0
        n = 0.1  # tasa de aprendizaje
        w = np.zeros(len(training_set[0]))  # np.zeros(n) usa float64 y se rompe
        delta_w = np.zeros(len(training_set[0]))
        self.error = 1
        min_error = p * 2
        w_min = np.zeros(len(training_set[0]))
        while self.error > 0 and iteration < self.limit:
            iteration += 1
            i_x = np.random.randint(0, p - 1)  # antes decia 1 y p
            excitation = np.dot(training_set[i_x], w)
            activation = SimplePerceptron.sign(excitation)
            for i in range(0, len(w)):
                delta_w[i] = n * (correct_output[i_x] - activation) * training_set[i_x][i]
                # aca no entiendo que x[i_x] tomar porque seria un array [-1, 1] ponele
                w[i] += delta_w[i]
            self.error = self.calculate_error(training_set, correct_output, w, p)
            if self.error < min_error:
                min_error = self.error
                w_min = w

        if iteration == self.limit:
            w = w_min
        print(w)
        return w

    @staticmethod
    def sign(n):
        return 1 if math.isclose(n, 0, rel_tol=1e-5) else -1

    # x -> conjunto de entrenamiento
    # y -> salida deseada
    @staticmethod
    def calculate_error(x, y, w, p):
        error = 0
        for i in range(p):
            output = SimplePerceptron.sign(np.dot(x[i], w))
            error += abs(output - y[i])
        return error
