import numpy as np

A = np.array(eval(input("Enter the coefficient matrix as a nested list (e.g., [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]): ")))

B = np.array(eval(input("Enter the constants as a list (e.g., [8, -11, -3]): ")))

print("\nThe coefficient matrix (A) is:")
print(A)

print("\nThe constant terms (B) are:")
print(B)

try:
    solution = np.linalg.solve(A, B)
    print("\nThe solution is:")
    print(solution)
except np.linalg.LinAlgError:
    print("The system of equations is inconsistent or has no unique solution.")



