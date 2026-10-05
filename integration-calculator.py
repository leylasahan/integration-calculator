#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from sympy import symbols, Eq, solve

# Function so as to calculate the area between a line and a curve
def area_between_line_and_curve(curve_func, line_func, a, b):
    integrand = lambda x: abs(curve_func(x) - line_func(x))
    area, _ = quad(integrand, a, b)
    return area

# Function so as to create a quadratic function from coefficients
def create_quadratic_function(a, b, c):
    return lambda x: a * x**2 + b * x + c

# Take input from user for quadratic coefficients and validate
while True:
    try:
        coefficients_input = input("Enter the coefficients a, b, c of the quadratic curve (separated by spaces): ")
        a, b, c = map(float, coefficients_input.split())
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter three numeric coefficients separated by spaces.")

# Create the quadratic curve function
curve_func = create_quadratic_function(a, b, c)

# Take input from user for the line (slope and intercept) and validate
while True:
    try:
        m = float(input("Enter the slope of the line (m): "))
        k = float(input("Enter the intercept of the line (c): "))
        break
    except ValueError:
        print("Invalid input. Please enter numeric values for the slope and intercept.")

line_func = lambda x: m * x + k

# Take input from user for the interval [a, b]
while True:
    try:
        lower_bound = float(input("Enter the lower bound of the interval (a): "))
        upper_bound = float(input("Enter the upper bound of the interval (b): "))
        if lower_bound >= upper_bound:
            raise ValueError("The lower bound must be less than the upper bound.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter valid numeric values for the interval.")

# Calculate the discriminant
A = a
B = b - m
C = c - k
discriminant = B**2 - 4*A*C
print(f"The discriminant is: {discriminant}")

# Find intersection points
if discriminant > 0:
    x = symbols('x')
    quadratic_eq = Eq(a * x**2 + (b - m) * x + (c - k), 0)
    intersection_points = solve(quadratic_eq, x)
    intersection_points = [float(pt) for pt in intersection_points if lower_bound <= pt <= upper_bound]
    intersection_points = sorted(intersection_points)
else:
    intersection_points = []

# Calculate and display the areas
total_area = 0
segment_areas = []

if len(intersection_points) == 0:
    area = area_between_line_and_curve(curve_func, line_func, lower_bound, upper_bound)
    segment_areas.append((lower_bound, upper_bound, area))
elif len(intersection_points) == 1:
    area1 = area_between_line_and_curve(curve_func, line_func, lower_bound, intersection_points[0])
    area2 = area_between_line_and_curve(curve_func, line_func, intersection_points[0], upper_bound)
    segment_areas.append((lower_bound, intersection_points[0], area1))
    segment_areas.append((intersection_points[0], upper_bound, area2))
else:
    area1 = area_between_line_and_curve(curve_func, line_func, lower_bound, intersection_points[0])
    segment_areas.append((lower_bound, intersection_points[0], area1))
    for i in range(len(intersection_points) - 1):
        area = area_between_line_and_curve(curve_func, line_func, intersection_points[i], intersection_points[i + 1])
        segment_areas.append((intersection_points[i], intersection_points[i + 1], area))
    area2 = area_between_line_and_curve(curve_func, line_func, intersection_points[-1], upper_bound)
    segment_areas.append((intersection_points[-1], upper_bound, area2))

for segment in segment_areas:
    print(f"Area between x={segment[0]} and x={segment[1]}: {segment[2]}")
    total_area += segment[2]

print(f"The total area between the line and the curve from x={lower_bound} to x={upper_bound} is: {total_area}")


# In[ ]:


# Plotting the curve, the line, and the shaded area between them
extended_range = (upper_bound - lower_bound) * 0.3  # Adjusted to zoom out more
x_vals = np.linspace(lower_bound - extended_range, upper_bound + extended_range, 400)  # Extended range for a complete graph
curve_vals = curve_func(x_vals)
line_vals = line_func(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, curve_vals, label='Quadratic Curve f(x)')
plt.plot(x_vals, line_vals, label=f'Line y = {m}x + {k}')

# Shade the area between the intersection points
for segment in segment_areas:
    plt.fill_between(x_vals, curve_vals, line_vals, where=((x_vals >= segment[0]) & (x_vals <= segment[1])), color='gray', alpha=0.3)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Area between Quadratic Curve and Line')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:





