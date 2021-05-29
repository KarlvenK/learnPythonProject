"""
import my_module

my_module.make_pizza(16, '1')

import my_module as mp

mp.make_pizza(1, '2')

from my_module import make_pizza as mpp

mpp(1, '3')

from my_module import *

my_module.make_pizza(1, '4')
"""