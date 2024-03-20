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


def numpy_matmul(A,B):
    start_numpy = time.time()
    D = A@B
    end_numpy = time.time()

    print("numpy time: " + str(end_numpy - start_numpy))
    return D


def rec_matmul_call(A, B, C, n):
    # Base case
    if n <= 8:
        tmp = np.zeros((n,n)).astype(np.float32)
        for x in range(n):
            for y in range(n):
                for z in range(n):
                    tmp[x][y] += A[x][z] * B[z][y]
        return tmp 
    
    # Divide
    # partition A,B,C into n//2 x n//2 submatrices
    rows, cols = A.shape
    # dividing in quadrants clockwise
    A11 = A[:rows//2, :cols//2]
    A12 = A[:rows//2, cols//2:]
    A21 = A[rows//2:, :cols//2]
    A22 = A[rows//2:, cols//2:]

    B11 = B[:rows//2, :cols//2]
    B12 = B[:rows//2, cols//2:]
    B21 = B[rows//2:, :cols//2]
    B22 = B[rows//2:, cols//2:]

    C11 = C[:rows//2, :cols//2]
    C12 = C[:rows//2, cols//2:]
    C21 = C[rows//2:, :cols//2]
    C22 = C[rows//2:, cols//2:]

    # Conquer
    rec_matmul_call(A11, B11, C11, n//2)
    rec_matmul_call(A11, B12, C12, n//2)
    rec_matmul_call(A21, B11, C21, n//2)
    rec_matmul_call(A21, B12, C22, n//2)
    rec_matmul_call(A12, B21, C11, n//2)
    rec_matmul_call(A12, B22, C12, n//2)
    rec_matmul_call(A22, B21, C21, n//2)
    rec_matmul_call(A22, B22, C22, n//2)

    return C


def rec_matmul(A,B):
    C = np.zeros((MATRIX_SIZE,MATRIX_SIZE)).astype(np.float32)
    start_rec = time.time()
    rec_matmul_call(A, B, C, MATRIX_SIZE)
    end_rec = time.time()

    print("rec time: " + str(end_rec - start_rec))

    return C


if __name__ == "__main__":
    A = np.random.randn(MATRIX_SIZE, MATRIX_SIZE).astype(np.float32)
    B = np.random.randn(MATRIX_SIZE, MATRIX_SIZE).astype(np.float32)
    
    
    # print("----- MATRIX A -----")
    # print(A)
    # print("----- MATRIX B -----")
    # print(B)
    
    flop = MATRIX_SIZE*MATRIX_SIZE*2*MATRIX_SIZE # rows * columns * 2 operations * elements_number
    print(f"{flop/1e9} GFLOP")

    classic_matmul(A, B)
    numpy_matmul(A, B)
    rec_matmul(A, B)