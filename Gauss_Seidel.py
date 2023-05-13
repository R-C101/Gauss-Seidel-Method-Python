import numpy as np

## Taking Inputs as matrix form Ax=B

print(' ||| PLEASE INPUT EQUATION MATRIX THAT CAN BE CONVERTED TO DIAGONAL DOMINANCE OTHERWISE THIS METHOD WONT WORK! |||')
n = int(input("Enter the number of equations/variables: "))
print("Enter the entries of matrix A in a single line (separated by space): ")
entriesA = list(map(int, input().split()))
matrixA = np.array(entriesA).reshape(n, n)
print(matrixA)

print("Enter the entries of matrix B in a single line (separated by space): ")

entriesB = list(map(int, input().split()))
matrixB = np.array(entriesB).reshape(n, 1)
print(matrixB)

# ESTABLISHING DIAGONAL DOMINANCE

for i in range(n):
    max_row = i
    for j in range(i+1, n):
        if abs(matrixA[j][i]) > abs(matrixA[max_row][i]):
            max_row = j
    # Swap rows
    matrixA[[i, max_row]] = matrixA[[max_row, i]]
    matrixB[[i, max_row]] = matrixB[[max_row, i]]
    # Swap columns
    matrixA[:, [i, max_row]] = matrixA[:, [max_row, i]]

print("Matrix A after rearrangement:")
print(matrixA)
print("Matrix B after rearrangement:")
print(matrixB)

# INTIAL GUESS 

x = np.zeros((n, 1))
use_default_guess = input("Do you want to use zero as the default initial guess? (Y/N)").lower() == "y"
if not use_default_guess:
        print("Enter the initial guesses for x in a single line (separated by space): ")
        entriesX = list(map(int, input().split()))
        x = np.array(entriesX).reshape(n, 1)
        
        
# PERFORMING ITERATIONS


max_iter = 10000
tolerance = 1e-4

for k in range(max_iter):
    x_old = x.copy()
    for i in range(n):
        s1 = np.dot(matrixA[i,:i], x[:i])
        s2 = np.dot(matrixA[i,(i+1):], x_old[(i+1):])
        x[i] = (matrixB[i] - s1 - s2) / matrixA[i,i]
    # Print current solution vector at each iteration
    print("Iteration", k+1, "Solution vector: \n", x)
    # Check for convergence
    if np.max(np.abs(x - x_old)) < tolerance:
        print("Gauss-Seidel method converged after", k+1, "iterations.")
        print("Solution vector:")
        print(x)
        break
else:
    print("Gauss-Seidel method did not converge after", max_iter, "iterations.")
    print("Solution vector:")
    print(x)
