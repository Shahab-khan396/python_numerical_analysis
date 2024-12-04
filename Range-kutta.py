def runge_kutta(f, x0, y0, x_end, h):
    """
    Parameters:
    f: The function f(x, y) representing dy/dx = f(x, y)
    x0: Initial value of x
    y0: Initial value of y
    x_end: The value of x at which to stop
    h: Step size for the numerical solution
    
    Returns:
    A list of (x, y) tuples representing the solution.
    """
    x = x0
    y = y0
    solution = [(x, y)]  # Store the initial condition

    while x < x_end:
       
        #finding the values of K1,k2,k3,k4
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)

        # now find the y value
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h

        solution.append((x, y))  # Append the result to the solution list

    return solution

# Example usage:
# Define the ODE dy/dx = x-y
def f(x, y):
    return x-y

# Initial conditions and parameters
x0 = float(input("Enter the value of X0 :"))     # Initial x
y0 = float(input("Enter the value of Y0 :"))       # Initial y
x_end = float(input("Enter the end of the range :"))   # Endpoint of x
h = float(input("Enter the value of h :"))  # Step size

# Solve the ODE by 0
# calling the Runge-Kutta methodS
solution = runge_kutta(f, x0, y0, x_end, h)

# Print the results
print("Solution (x, y):")
for x, y in solution:
    print(f"x = {x:.2f}, y = {y:.4f}")

# Plot the solution
import matplotlib.pyplot as plt

x_vals, y_vals = zip(*solution)
plt.plot(x_vals, y_vals, label="Runge-Kutta Approximation")
plt.xlabel("x")
plt.ylabel("y")
plt.title("4th-Order Runge-Kutta Method")
plt.legend()
plt.grid()
plt.show()
