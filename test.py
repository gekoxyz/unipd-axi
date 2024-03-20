import numpy as np
import time

MATRIX_SIZE = 512

def classic_matmul(A,B):
    C = np.zeros((MATRIX_SIZE,MATRIX_SIZE))

    start_classic = time.time()
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            for k in range(MATRIX_SIZE):
                C[i][j] += A[i][k] * B[k][j]
    end_classic = time.time()

    print("classic time: " + str(end_classic - start_classic))
    return C

def inv_classic_matmul(A,B):
    C = np.zeros((MATRIX_SIZE,MATRIX_SIZE))

    start_classic = time.time()
    for j in range(MATRIX_SIZE):
        for i in range(MATRIX_SIZE):
            for k in range(MATRIX_SIZE):
                C[i][j] += A[i][k] * B[k][j]
    end_classic = time.time()

    print("invclassic time: " + str(end_classic - start_classic))
    return C

if __name__ == "__main__":
    A = np.random.randn(MATRIX_SIZE, MATRIX_SIZE).astype(np.float32)
    B = np.random.randn(MATRIX_SIZE, MATRIX_SIZE).astype(np.float32)
    
    classic_matmul(A, B)
    inv_classic_matmul(A, B)
    