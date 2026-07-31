import random

def riemannSum(func,lowerBound, upperBound, partitions = 100000):
    delta = (upperBound - lowerBound) / partitions
    x = lowerBound
    total = 0
    while x < upperBound:
        total += func(x) * delta
        x += delta
    return total

def f(x,y):
    return x**2 + y**2

def threeDimensionalRiemannSums(func,lowerBounds : list[int], upperBounds : list[int], partitions = 10000):
    deltaX = (upperBounds[0] - lowerBounds[0]) / partitions
    deltaY = (upperBounds[1] - lowerBounds[1]) / partitions
    y = lowerBounds[1]
    total = 0
    while y < upperBounds[1]:
        x = lowerBounds[0]
        while x < upperBounds[0]:
            total += func(x,y) * deltaX * deltaY
            x += deltaX
        y += deltaY
    return total
