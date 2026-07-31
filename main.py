import random
import timeit
import matplotlib as plt
from HitOrMissMCIntegration import HMMonteCarloIntegral2d
from HitOrMissMCIntegration import HMMonteCarloIntegral3d
from Riemman import riemannSum

def f(x):
    return 3*x**2

executionTime = timeit.timeit(lambda : HMMonteCarloIntegral2d(f, 0, 2, 12, 100000), globals=globals(), number = 1000)
print(f"2d Hit-or-Miss Monte Carlo integration Total time : {executionTime} seconds")
executionTime = timeit.timeit(lambda : riemannSum(f,0,2,100000), globals=globals(), number = 1000)
print(f"2d left Riemann sums Total time : {executionTime} seconds")


