import random
import timeit
import statistics
import matplotlib as plt
from HitOrMissMCIntegration import HMMonteCarloIntegral2d
from HitOrMissMCIntegration import HMMonteCarloIntegral3d
from Riemman import riemannSum
from Riemman import threeDimensionalRiemannSums

def f(x):
    return 3*x**2

error = []
for i in range(0,1000):
    expectedValue = 8
    observedValue = HMMonteCarloIntegral2d(f, 0, 2, 12, 10000)

    error.append(expectedValue - observedValue)

max = -99999
min = 99999

total = 0

for i in range(0,1000):
    if error[i] < min:
        min = error[i]
    if error[i] > max:
        max = error[i]
    total += error[i]

print(f"The average error for the Hit-or-Miss Monte Carlo Integration was {total/100}")
print(f"The max error was {max}")
print(f"The min error was {min}")
print(f"The standard deviation is {statistics.stdev(error)}")

expectedValue = 8
observedValue = riemannSum(f, 0, 2, 1000)

error = expectedValue - observedValue

print(f"The error of the Riemann Sums was {error}")

runs = 100

totalTimeMC = timeit.timeit(lambda : HMMonteCarloIntegral2d(f, 0, 2, 12, 10000), globals=globals(), number=runs)
print(f"The average runtime of the Hit-or-Miss Monte Carlo Integration is {totalTimeMC/runs}")

totalTimeRS = timeit.timeit(lambda : riemannSum(f, 0, 2, 1000), globals=globals(), number=runs)
print(f"The average runtime of the 2 Dimensional Riemman sums is {totalTimeRS/runs}")

print(f"On average it took the Monte Carlo methods {totalTimeMC/totalTimeRS} times longer than the Riemman Sums ")

def g(x, y):
    return x**2 + y**2

error3d = []

for i in range(0, 100):
    expectedValue3d = 2/3
    observedValue3d = HMMonteCarloIntegral3d(g,[0,0], [1,1], 2, 10000)
    error3d.append(expectedValue3d - observedValue3d)

min3d = 99999
max3d = -99999
total3d = 0

for i in range(0, len(error3d)):
    if error3d[i] < min:
        min = error3d[i]
    if error3d[i] > max:
        max = error3d[i]
    total3d += error3d[i] 

print(f"The average error for the Hit-or-Miss Monte Carlo Integration was {total3d/100}")
print(f"The max error was {max3d}")
print(f"The min error was {min3d}")
print(f"The standard deviation is {statistics.stdev(error3d)}")

observedValueRS3d = threeDimensionalRiemannSums(g,[0,0], [1,1], 1000)

print(f"The Error for the three dimensiona Riemann Sum was {expectedValue3d - observedValueRS3d}")

totalTime3dMC = timeit.timeit(lambda : HMMonteCarloIntegral3d(g,[0,0], [1,1], 2, 10000), number = 100)

totalTime3dRS = timeit.timeit(lambda : threeDimensionalRiemannSums(g,[0,0], [1,1], 1000), number = 100)

print(f"The average runtime of the 3 Dimensional Hit-or-Miss Monte Carlo Integration is {totalTime3dMC/runs}")

print(f"The average runtime of the 3 Dimensional Riemman sums is {totalTime3dRS/runs}")

print(f"On Average it took the 3d Riemman Sums {totalTime3dMC/totalTime3dRS} times longer than the Monte Carlo methods for similar accuracy rates")