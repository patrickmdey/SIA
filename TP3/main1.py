from plotter import plot_error, plot
import sys
from simple_perceptron import SimplePerceptron
from utils import solve_type_step

if len(sys.argv) > 1 and sys.argv[1] == "xor":
    or_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
    or_out_set = [1, 1, -1, -1]
    print("Solving for XOR")
    w, e, m, weights = SimplePerceptron(0.1, 1000).solve({"in": or_in_set, "out": or_out_set},
                                                         {"in": [], "out": []}, solve_type_step, True)
    plot_error(e)
    plot(or_in_set, or_out_set, weights, 'Grafico')
    
else:
    # el -1 al principio de cada ejemplo de entrenamiento es el umbral
    and_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
    and_out_set = [-1, -1, -1, 1]

    print("Solving for AND")
    w, e, m, weights = SimplePerceptron(0.1, 1000).solve({"in": and_in_set, "out": and_out_set},
                                                         {"in": [], "out": []}, solve_type_step, True)
    plot_error(e)
    # print(weights)

    plot(and_in_set, and_out_set, weights, 'Grafico')

print("Final W:", w)
