import numpy as np
import time

"""
Matrix multiplication between two rectangular matrices A and B.

Args:
  A: Matrix A, with shape (m, n)
  B: Matrix B, with shape (n, p)

Returns:
  C: Matrix C, with shape (m, p)
"""
def rect_matmul(A, B):
  m, n = len(A) - 1, len(A[0]) - 1
  n, p = len(B) - 1, len(B[0]) - 1

  C = np.zeros((m, p))

  for i in range(m):
    for j in range(p):
      C[i,j] = A[i,0] * B[0,j]
      for k in range(1, n):
        C[i,j] = C[i,j] + A[i,k] * B[k,j]

  return C

def matrix_chain_mul(p):
  n = len(p) - 1
  m = np.zeros((n,n))
  s = np.zeros((n,n))

  for i in range(1, n):
    m[i,i] = 0
  for l in range(2, n):
    for i in range(1, n - l + 1):
      j = i + l - 1
      m[i,j] = -1
      for k in range(i, j-1):
        q = m[i,k] + m[k+1, j] + p[i-1] * p[k] * p[j]
        if q < m[i,j]:
          m[i, j] = q
          s[i, j] = k
  print(m)
  print()
  print(s)

def mcm(chain):
  return

if __name__ == "__main__":
  A = np.random.randn(10, 100).astype(np.float32)
  print("=== matrix A ===")
  print(A)
  B = np.random.randn(100, 5).astype(np.float32)
  print("=== matrix B ===")
  print(B)
  C = np.random.randn(5, 50).astype(np.float32)
  print("=== matrix C ===")
  print(C)

  start_time = time.time()
  D1 = rect_matmul(A, rect_matmul(B, C))
  end_time = time.time()
  print("=== matrix D1 ===")
  print(f"execution time: {end_time - start_time}")
  # print(D1)

  start_time = time.time()
  D2 = rect_matmul(rect_matmul(A, B), C)
  end_time = time.time()
  print("=== matrix D2 ===")
  print(f"execution time: {end_time - start_time}")
  # print(D2)

  mcm([10, 100, 5, 50])