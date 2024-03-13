import numpy as np

np.random.seed(1337)

MATRIX_SIZE = 64

def rec_matmul(A, B, C, n):
    # Base case
    if n == 1:
        return A[0][0] * B[0][0]
        # for x in range(n):
        #     for y in range(n):
        #         for z in range(n):
        #             C[x][y] += A[x][z] * B[z][y]
    
    # Divide
    # partition A,B,C into n//2 x n//2 submatrices
    rows, cols = A.shape
    
    A11 = A[:rows//2, :cols//2]
    A12 = A[:rows//2, cols//2:]
    A21 = A[rows//2:, :cols//2]
    A22 = A[rows//2:, cols//2:]

    B11 = B[:rows//2, :cols//2]
    B12 = B[:rows//2, cols//2:]
    B21 = B[rows//2:, :cols//2]
    B22 = B[rows//2:, cols//2:]

    A1 = A12 - A22
    A2 = A11 + A22
    A3 = A11 - A21
    A4 = A11 + A12
    A5 = A11
    A6 = A22
    A7 = A21 + A22

    B1 = B21 + B22
    B2 = B11 + B22
    B3 = B11 + B12
    B4 = B22
    B5 = B12 - B22
    B6 = B21 - B11
    B7 = B11

    C11 = C[:rows//2, :cols//2]
    C12 = C[:rows//2, cols//2:]
    C21 = C[rows//2:, :cols//2]
    C22 = C[rows//2:, cols//2:]

    # pag 46/155 dispensa pucci
    P1 = rec_matmul(A1, B1, np.zeros((rows//2, cols//2)).astype(np.float32), n//2)
    P2 = rec_matmul(A2, B2, np.zeros((rows//2, cols//2)).astype(np.float32), n//2)
    P3 = rec_matmul(A3, B3, np.zeros((rows//2, cols//2)).astype(np.float32), n//2)
    P4 = rec_matmul(A4, B4, np.zeros((rows//2, cols//2)).astype(np.float32), n//2)
    P5 = rec_matmul(A5, B5, np.zeros((rows//2, cols//2)).astype(np.float32), n//2)
    P6 = rec_matmul(A6, B6, np.zeros((rows//2, cols//2)).astype(np.float32), n//2)
    P7 = rec_matmul(A7, B7, np.zeros((rows//2, cols//2)).astype(np.float32), n//2)

    # Conquer
    C11 += P1 + P2 - P4 + P6
    C12 += P4 + P5
    C21 += P6 + P7
    C22 += P2 - P3 + P5 - P7

    # Join C11 and C12 horizontally (along the second axis)
    C1 = np.hstack((C11, C12))
    # Join C21 and C22 horizontally (along the second axis)
    C2 = np.hstack((C21, C22))
    # Join C1 and C2 vertically (along the first axis)
    return np.vstack((C1, C2))


if __name__ == "__main__":
    S = np.zeros((MATRIX_SIZE,MATRIX_SIZE)).astype(np.float32)

    A = np.random.randn(MATRIX_SIZE, MATRIX_SIZE).astype(np.float32)
    B = np.random.randn(MATRIX_SIZE, MATRIX_SIZE).astype(np.float32)

    print(rec_matmul(A, B, S, MATRIX_SIZE))

    print(A@B)










































# def strassen_matmul(A,B):
#     rows, cols = A.shape
#     # print("ROWS " + str(rows) + "\t COLS " + str(cols))
#     if rows == 1:
#         return [[A[0][0] * B[0][0]]]

#     for i in range(0,rows, rows//2):
#         for j in range(0,cols, cols//2):
#             print(str(i) + " | " + str(j))
#             tmp = np.add(strassen_matmul(np.matrix(A[i,0]), np.matrix(B[0,j])), strassen_matmul(np.matrix(A[i,1]), np.matrix(B[1,j])))
            
#             pos_y, pos_x = i, j  # offset
#             v_range1 = slice(max(0, pos_y), max(min(pos_y + tmp.shape[0], S.shape[0]), 0))
#             h_range1 = slice(max(0, pos_x), max(min(pos_x + tmp.shape[1], S.shape[1]), 0))

#             v_range2 = slice(max(0, -pos_y), min(-pos_y + S.shape[0], tmp.shape[0]))
#             h_range2 = slice(max(0, -pos_x), min(-pos_x + S.shape[1], tmp.shape[1]))

#             S[v_range1, h_range1] += tmp[v_range2, h_range2]

         
#     return S

