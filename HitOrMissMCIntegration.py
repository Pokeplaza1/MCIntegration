import random

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def generatePoint(lowerBound, upperBound, absoluteMax):
    return Point(random.uniform(lowerBound, upperBound), random.uniform(0,absoluteMax))
    
def isBellow(p, func):
    if func(p.x) >= p.y:
        return True
    else: 
        return False
        
def HMMonteCarloIntegral(func, lowerBound, upperBound, absoluteMax, sampleSize = 100000):
    count = 0.0
    for i in range(0,sampleSize):
        p = generatePoint(lowerBound, upperBound, absoluteMax)
        if isBellow(p, func):
            count += 1
    return (upperBound*absoluteMax*count / sampleSize)
