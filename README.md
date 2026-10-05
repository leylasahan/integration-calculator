# Area Between a Curve and a Line: Numerical Integration Calculator

A Python program that calculates the area enclosed between a quadratic curve and a straight line over a chosen interval, and plots the result. It handles the three possible cases: the line lies below the curve, the line lies above the curve, or the two intersect within the interval.

Developed as a team project at OnCampus London (2024).

## What it does

Given a quadratic `y = ax² + bx + c`, a line `y = mx + k`, and lower and upper bounds, the program:

1. Checks the discriminant of `ax² + (b − m)x + (c − k) = 0` to see whether the curve and line intersect.
2. Solves for the intersection points and keeps only those that fall inside the bounds.
3. Splits the interval at each intersection point, so that regions where the curve is above the line and regions where it is below are handled separately.
4. Integrates the absolute difference between curve and line over each region and sums the results.
5. Plots the curve, the line and the shaded area between them.

## Methods

- **Numerical integration** (integration and the trapezium rule) to approximate the area.
- **Discriminant analysis** to decide whether, and where, the curve and line meet.
- **Symbolic solving** (SymPy) to find intersection points exactly.
- **Input validation** with a `while` loop and `try/except`, so invalid coefficients prompt the user to re-enter them rather than crashing the program.

## Example results

| Case | Curve | Line | Bounds | Area |
|---|---|---|---|---|
| No intersection | `y = 2x² + 4x + 3` | `y = 2x − 4` | 1 to 3 | 39.3 |
| Two intersections | `y = x² + 5x` | `y = 12x + 2` | −3 to 13 | 292.8 |

**Check on the first case:** the difference between curve and line is `2x² + 2x + 7`, whose discriminant is negative, so there is no intersection. Integrating analytically over [1, 3] gives 39.33, which matches the program's output.

In the second case the program splits the interval at the two intersection points (x ≈ −0.27 and x ≈ 7.27) and adds the three resulting areas, rather than integrating straight across, which would let the regions partly cancel.

## Validation

The program's output was compared with analytically calculated areas for a range of test cases (linear and quadratic functions, and each curve–line configuration) to check accuracy.

## Requirements

- Python 3
- NumPy
- SciPy
- SymPy
- Matplotlib

Install with:

```
pip install numpy scipy sympy matplotlib
```

## How to run

1. Download or clone this repository.
2. Open `integration-calculator.py` in Spyder (or any Python environment).
3. Run the file and follow the prompts:
   - Enter the quadratic coefficients `a b c`, separated by spaces.
   - Enter the line's gradient and intercept.
   - Enter the lower and upper bounds.
4. The area is printed and a plot is displayed.

## Possible extensions

- Support for parametric curves and three-dimensional surfaces.
- Adaptive numerical integration methods for greater precision and more complex curve shapes.

## Authors

Leyla Sahan, Naveesha Jain and Danish Majeed Chaudhary, ONCAMPUS London, 2024.

## What I learned

This project showed me that programming and calculus work best together: the maths decides *which* regions to integrate and where the curve and line cross, and the code makes that reliable for any input.
