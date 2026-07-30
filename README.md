# Project Goal
Compare the runtimes and accuracy of different methods of numerical integration

# Methods tested

## Hit or Miss Monte Carlo Integration
Contains a program that numerically approximates the definite integral

### How

1. Generate random points uniformly inside a rectangle containing the function.
2. Count how many points lie below the curve.
3. Estimate the fraction of the rectangle occupied by the region under the curve.
4. Multiply this fraction by the rectangle's area to estimate the integral.

### Limitations

-The methodology itself also requires knowing the absolute extrema of the function on the interval
-The is bellow function only checks bellow the function which only works if the function value is positive at that point

## Riemman sums
Contains a function that takes a left Riemman sum of a given 2-d function

### How

1. Calculates the change in x per partition called delta 
2. Calculates the function at a given x on the interval
3. Multiply the length of delta by the function value
4. Sum this to get an approximation of the area under the curve

### Limitations

-The method used is the a left Riemman sum which is less accurate on some functions than a right Riemman sum but this averages out
-The function only works for 2-d functions and single integrals

## Main function

Currently testing the accuracy of the Riemman sums vs. the Hit-or-Miss Monte Carlo Integration on the function $\int_{0}^{2} 3x^{2}\,dx$.

# Planned Features

1. modify functions to be multi dimensional
2. Add Expected value MCintergration 
3. Add trapezoid sums
4. Do runtime analysis to compare the runtime of the different methods over dimensions to see the scaling of different methods
5. Test accuracy of results as dimension of functions are increased

