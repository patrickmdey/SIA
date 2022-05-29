# library
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def plot_heatmap(matrix, title):
    # Create a dataset
    df = pd.DataFrame(matrix)

    # Default heatmap
    p = sns.heatmap(df)
    p.set_title(title)

    plt.show()