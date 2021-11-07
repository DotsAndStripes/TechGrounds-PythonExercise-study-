# With these commands, a random number can be given by the computer.
# The number of values is 5, for the range is (0,5)
# The values are between 0 and 100 (randint)
# There are multiple ways. 2 are mentioned.
# to use the command random, we have to import the module random.

from random import randint
x5 = [randint(0, 100) for i in range(0, 5)]
for i in x5:
    print(i)

print("-x-x-x-x-x-")

import random
for x in range (5):
    x=random.randint(0,100)
    print(x)