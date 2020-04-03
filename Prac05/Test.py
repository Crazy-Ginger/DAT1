from numpy import random as npRand
from matplotlib import pyplot as plt

sample = npRand.exponential(15, 100000)
print (sample)
plt.scatter(range(len(sample)), sample)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
