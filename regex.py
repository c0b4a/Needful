#!/usr/bin/env python
import sys
import re

word = '5600X-fer-this-samb-py'

found = re.findall(r'\d*\S\d\dX', word)

print(found)
