# Project Goal
Compare the runtimes and accuracy of different methods of numerical integration

# Methods tested

## Hit or Miss Monte Carlo Integration
Contains two programs numerically approximating the definite intergral or double intergral of a 2d or 3d function respectively

### How

1. Generate random points uniformly inside a rectangle containing the function.
2. Count how many points lie below the curve.
3. Estimate the fraction of the rectangle occupied by the region under the curve.
4. Multiply this fraction by the rectangle's area to estimate the integral.

### Limitations

-The methodology itself also requires knowing the absolute extrema of the function on the interval
-The is bellow function only checks bellow the function which only works if the function value is positive at that point

## Riemman sums
Contains two seperate functions one for 2 Dimensional Riemann sums and another for 3 Dimensional Riemman Sums

### How

1. Calculates the change in x per partition called delta 
2. Calculates the function at a given x on the interval
3. Multiply the length of delta by the function value
4. Sum this to get an approximation of the area under the curve

### Limitations

-The method used is the a left Riemman sum which is less accurate on some functions than a right Riemman sum but this averages out

# Current findings

The Monte Carlo intergration needs 10 times as many points to have a similar accuracy to the Riemman intgration in 2 dimensions. Due to this Monte Carlo methods take nearly 36 times longer to run than the Riemman sums. 




# Planned Features

1. modify functions to be multi dimensional
2. Add Expected value MCintergration 
3. Add trapezoid sums

