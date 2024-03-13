import numpy as np

# matrix = np.array([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12],
#                    [13, 14, 15, 16]])
# print(matrix)

# rows, cols = matrix.shape

# print(matrix[:rows//2, :cols//2])
# print(matrix[:rows//2, cols//2:])
# print(matrix[rows//2:, :cols//2])
# print(matrix[rows//2:, cols//2:])



m1 = np.array([[1,2],[3,4]])
m2 = np.array([[4,3],[2,1]])

print(m1+m2)

print(np.add(m1,m2))