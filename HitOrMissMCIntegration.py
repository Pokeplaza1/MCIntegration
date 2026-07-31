import random

class Point2d():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def generatePoint2d(lowerBound, upperBound, absoluteMax):
    return Point2d(random.uniform(lowerBound, upperBound), random.uniform(0,absoluteMax))
    
def isBellow2d(p, func):
    if func(p.x) >= p.y:
        return True
    else: 
        return False
        
def HMMonteCarloIntegral2d(func, lowerBound, upperBound, absoluteMax, sampleSize = 100000):
    count = 0.0
    for i in range(0,sampleSize):
        p = generatePoint2d(lowerBound, upperBound, absoluteMax)
        if isBellow2d(p, func):
            count += 1
    return (upperBound*absoluteMax*count / sampleSize)

class Point3d():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def generatePoint3d(lowerBounds : list[int], upperBounds : list[int], absoluteMax):
    return Point3d(random.uniform(lowerBounds[0], upperBounds[0]), random.uniform(lowerBounds[1], upperBounds[1]), random.uniform(0,absoluteMax))

def isBellow3d(p, func):
    if func(p.x, p.y) >= p.z:
        return True
    else:
        return False

def HMMonteCarloIntegral3d(func, lowerBounds : list[int], upperBounds : list[int], absoluteMax, sampleSize = 100000):
    count = 0.0
    for i in range(0,sampleSize):
        p = generatePoint3d(lowerBounds, upperBounds, absoluteMax)
        if isBellow3d(p, func):
            count += 1
    return (upperBounds[0]*upperBounds[1]*absoluteMax*count / sampleSize)
