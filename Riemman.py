import random

def riemmanSum(func,lowerBound, upperBound, partitions = 100000):
    delta = (upperBound - lowerBound) / partitions
    x = lowerBound
    sum = 0
    while x < upperBound:
        sum += func(x) * delta
        x += delta
    return sum