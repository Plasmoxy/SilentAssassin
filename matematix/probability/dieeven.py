# evendieprobability.py by Plasmoxy

# This script rolls a die a "few" times and finds out
# the ratio between even number rolls and total number
# of rolls.

# As the number of rolls approaches infinity, the ratio
# approaches the probability of getting even number which
# is 1/2 .

import random as r
import math

ITERNUM = math.pow(10, 7)

evens=0

i=0 # iterations

print ("Rolling a die {} times...".format(ITERNUM))

try :
    while i<ITERNUM :
        percent = (i/ITERNUM)*100.0
        if (percent%1.00 == 0):
            print(percent, "%")
        evens += r.randint(1, 6)%2
        i += 1 # after an iteration is complete, add to interations

except KeyboardInterrupt:
    pass
finally:
    print("100 %")
    print("even numbers : ", evens)
    print("iterations : ", i)
    print("evens/i : ", evens/i)
    print("target probability : 0.5")
    print("error : ",  abs(0.5-evens/i))
