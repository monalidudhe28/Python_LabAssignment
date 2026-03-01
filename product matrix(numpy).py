import numpy as np

print("Enter elements for 5x3 matrix:")

matrix1 = []
for i in range(5):
    row = list(map(int, input(f"Enter 3 elements for row {i+1} separated by space: ").split()))
    matrix1.append(row)

matrix1 = np.array(matrix1)

print("\nEnter elements for 3x2 matrix:")

matrix2 = []
for i in range(3):
    row = list(map(int, input(f"Enter 2 elements for row {i+1} separated by space: ").split()))
    matrix2.append(row)

matrix2 = np.array(matrix2)

# Matrix multiplication
product = np.matmul(matrix1, matrix2)

print("\nMatrix 1 (5x3):")
print(matrix1)

print("\nMatrix 2 (3x2):")
print(matrix2)

print("\nProduct Matrix (5x2):")
print(product)