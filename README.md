#Hit or Miss Monte Carlo Integration
The file HitOrMissMCIntegration contains a program that numerically approximates the integral of the function $'3x^2'$

##How

It does this by randomly sampling points from a uniform distribution in a rectangular region and finding the portion located under the curve. It then divides by the number of sample and multiplies by the area of the rectangular region

##Limitations

This program currently utilizes hard coded values and functions
The methodology itself also requires knowledge of the extrema of the function on the given interval
The is bellow function only checks bellow the function which only works if the function value is positive at that point
