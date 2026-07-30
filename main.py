import random
from HitOrMissMCIntegration import HMMonteCarloIntegral
from Riemman import riemmanSum

def f(x):
    return 3*x**2

print(HMMonteCarloIntegral(f, 0, 2, 12, 100000))
print(riemmanSum(f,0,2,100000))


