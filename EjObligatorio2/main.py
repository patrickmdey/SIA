from pca import pca
import csv
import numpy as np


with open('europe.csv', newline='') as csvfile:
    # create np array with csv rows
    rows = np.array(list(csv.reader(csvfile, delimiter=',')))
    headers = np.array(rows[0][1:])
    rows = rows[1:] # ignoro headers
    countries = [row[0] for row in rows] # me quedo con los paises para poner los labels
    rows = np.array([row[1:] for row in rows]) # elimino pais
    
    csvfile.close()

    # Initialize to reduce the data up to the number of componentes that explains 95% of the variance.
    model = pca(n_components=0.95, normalize=True)

    print(headers)
    # Fit transform
    results = model.fit_transform(rows, col_labels=headers, row_labels=countries)
    print(results['loadings'])

    print()

    print(results['variance_ratio'])

    # Plot explained variance
    fig, ax = model.plot()

    # Scatter first 2 PCs
    fig, ax = model.scatter()

    # Make biplot with the number of features
    fig, ax = model.biplot()
