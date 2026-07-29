import random
import numpy as np 



def f(x):
    return 3*x**2

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def generatePoint():
    return Point(random.uniform(0,2), random.uniform(0,12))
    
def isBellow(p, func):
    if func(p.x) >= p.y:
        return True
    else: 
        return False
        
def HMMonteCarloIntegral(func):
    count = 0
    for i in range(0,10000):
        p = generatePoint()
        if isBellow(p, func):
            count += 1
    print(24*count / 10000)
    
HMMonteCarloIntegral(f)