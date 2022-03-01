# Program to multiply two matrices using nested loops
import random
from matplotlib.pyplot import axis
import numpy as np

def matmult(N):
    #-- numpy
    # X = np.array([], dtype=int)
    # for i in range(N):
    #     np.append(X, [random.randint(0,100) for r in range(N)], axis=0)

    # Y = np.array([], dtype=int)
    # for i in range(N):
    #     np.append(Y, [random.randint(0,100) for r in range(N)], axis=0)

    #-- numpy + list

    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    X = np.asarray(X)

    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])    
    Y = np.asarray(Y)


    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    result = np.asarray(result)

    # # iterate through rows of X
    # for i in range(len(X)):
    #     # iterate through columns of Y
    #     for j in range(len(Y[0])):
    #         # iterate through rows of Y
    #         for k in range(len(Y)):
    #             result[i][j] += X[i][k] * Y[k][j]

    # print( X.size, X[0].size, Y[0].size, Y[1].size, result.size)

    # # iterate through rows of X
    # for i in range(X.shape[0]):
    #     # iterate through columns of Y
    #     for j in range(Y.shape[1]):
    #         # iterate through rows of Y
    #         for k in range(Y.shape[0]):
    #             # result[i][j] += X[i][k] * Y[k][j]
    #             result[i][j] += np.dot(X[i][k], Y[k][j])

    # iterate through rows of X
    for i in range(X.shape[0]):
        # iterate through columns of Y
        for j in range(Y.shape[1]):
            # iterate through rows of Y
            result[i][j] = np.dot(X[i], Y[:, j])
    '''
    for r in result:
        print(r)
    '''

def matmult2(N):
    X = np.random.randint(0, 100, size=(N,N))
    Y = np.random.randint(0, 100, size=(N,N))

    result = X * Y
    
# matmult(250)