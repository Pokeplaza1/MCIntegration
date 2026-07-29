# Hit or Miss Monte Carlo Integration
Contains a program that numerically approximates the definite integral $\int_{0}^{2} 3x^{2}\,dx$.

## How

1. Generate random points uniformly inside a rectangle containing the function.
2. Count how many points lie below the curve.
3. Estimate the fraction of the rectangle occupied by the region under the curve.
4. Multiply this fraction by the rectangle's area to estimate the integral.

## Limitations

This program currently utilizes hard coded a function
The methodology itself also requires knowing the absolute extrema of the function on the interval
The is bellow function only checks bellow the function which only works if the function value is positive at that point
