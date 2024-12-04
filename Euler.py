# Euler Method for solving dy/dx = f(x, y)
import matplotlib.pyplot as plt
def euler_method(f, x0, y0, x_end, h):
    """
    Parameters:
    f: The function f(x, y) defining the differential equation dy/dx = f(x, y)
    x0: Initial value of x
    y0: Initial value of y
    x_end: The value of x at which to stop
    h: The step size for the numerical solution
    Returns:
    A list of (x, y) tuples representing the solution
    """
    # Initialize variables
    x = x0
    y = y0
    solution = [(x, y)]  # Store the initial condition
    
    while x < x_end:
        # Compute the next value of y using Euler's formula
        y = y + h * f(x, y)
        x= x + h
        solution.append((x, y))  # Store the result
    
    return solution

# Example usage:
# Define the ODE dy/dx = x-y
def f(x, y):
    return  x - y

# Initial conditions and parameters
x0 = float(input("Enter the value of X0 :"))     # Initial x
y0 = float(input("Enter the value of Y0 :"))       # Initial y
x_end = float(input("Enter the end of the range :"))   # Endpoint of x
h = float(input("Enter the value of h :"))  # Step size

# Solve the ODE using Euler's method
solution = euler_method(f, x0, y0, x_end,h)

# Print the solution
print("Solution (x, y):")
for x, y in solution:
    print(f"x = {x:.2f}, y = {y:.4f}")

# Optionally, plot the solution
x_vals, y_vals = zip(*solution)
plt.plot(x_vals, y_vals, label="Euler Approximation")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Euler Method Approximation")
plt.legend()
plt.grid()
plt.show()