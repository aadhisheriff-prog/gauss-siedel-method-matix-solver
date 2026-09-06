# Gauss-Seidel Method in Python

n = int(input("Enter the number of equations: "))

# Enter coefficient matrix
A = []

print("\nEnter the coefficients of the equations:")

for i in range(n):
    row = []
    for j in range(n):
        value = float(input(f"Enter A[{i+1}][{j+1}]: "))
        row.append(value)
    A.append(row)

# Enter constant values
b = []

print("\nEnter the constant values:")

for i in range(n):
    value = float(input(f"Enter b[{i+1}]: "))
    b.append(value)

# Enter initial guesses
x = []

print("\nEnter the initial guesses:")

for i in range(n):
    value = float(input(f"Enter initial x{i+1}: "))
    x.append(value)

# Tolerance and maximum iterations
tolerance = float(input("\nEnter the tolerance: "))
max_iterations = int(input("Enter maximum number of iterations: "))

# Gauss-Seidel iteration
for iteration in range(max_iterations):

    old_x = x.copy()

    for i in range(n):

        sum_value = 0

        for j in range(n):
            if j != i:
                sum_value += A[i][j] * x[j]

        x[i] = (b[i] - sum_value) / A[i][i]

    # Check convergence
    error = max(abs(x[i] - old_x[i]) for i in range(n))

    if error < tolerance:
        print("\nSolution converged!")
        break

else:
    print("\nMaximum number of iterations reached.")

# Display result
print("\nFinal Solution:")

for i in range(n):
    print(f"x{i+1} = {x[i]:.6f}")

print("\nNumber of iterations:", iteration + 1)
