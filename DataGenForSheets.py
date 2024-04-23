#!/usr/bin/env python
from datetime import datetime
import random
import sys

def PNGen(character: str, f) -> None:
    for y in range(10):
        for x in range(10):
            partNumber = ''.join(character + str(y) + '000' + str(x) + '\n')
            f.write(partNumber)

def PartNameGen(data, f, o) -> None:
    value = round(random.randint(1, 333))
    o.write(f.readline(value))

def PriceGen(min, max, o) -> None:
    for x in range(2300):
        value = round(random.randint(min, max))
        o.write(str(value) + '\n')

def main() -> None:
    random.seed(datetime.now().timestamp())
    data = []
    o = open('DataOut.txt', 'w+')
    f = open('FormattedWordList.txt', 'r')
    #letterList = 'ABCDEFGHJKMNPQRSTUVWXYZ'
    #splitLetterList = [z for z in letterList]
    #for character in splitLetterList:
    #    PNGen(character, f)
    #c = 0
    #while(c > 2400):
    #    PartNameGen(data, f, o)
    #    c += 1
    #print(data)
    PriceGen(1, 100, o)

    f.close()
    o.close()

if __name__ == '__main__':
    main()