import numpy as np

def matrix_transpose(X):
    X = np.asarray(X)

    rows = len(X)
    cols = len(X[0])

    transpose = np.zeros((cols, rows))

    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = X[i][j]

    return transpose