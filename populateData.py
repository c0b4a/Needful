#!/usr/bin/env python
'''populateData.py: Rndint -> xls'''

#imports
import random

#constant variables
MAX_ROWS = 50
MAX_LEN = 100
MIN_VAL = 0
MAX_VAL = 10

#tmp variables
x = 0

#data structures
data = [None]*MAX_LEN

#populate data structure with random ints + initializer
random.seed()

for x in range(MAX_LEN):
    data[x] = random.randint(MIN_VAL, MAX_VAL)

print(data)
