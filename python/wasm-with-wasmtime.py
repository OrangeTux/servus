import os
import sys
import wasmtime

__dir__ = os.path.dirname(os.path.realpath(__file__))
sys.path.append(__dir__ + '/pkg/')

import servus_bg as servus

sum = servus.sum(3, 7)
print(f'wasmtime: sum of 3 and 7 is {sum}')
