# importing Numpy package
import numpy as np

# creating a 2X2 Numpy matrix
# n_array = np.array([[50, 29], [30, 44]])
# n_array = np.array([[55, 25, 15],
#                     [30, 44, 2],
#                     [11, 45, 77]])
n_array = np.array([[5, 2, 1, 4, 6],
                    [9, 4, 2, 5, 2],
                    [11, 5, 7, 3, 9],
                    [5, 6, 6, 7, 2],
                    [7, 5, 9, 3, 3]])

# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)

# calculating the determinant of matrix
det = np.linalg.det(n_array)

print("\nDeterminant of given matrix:")
print(int(det))