import core
import numpy as np
import random

def f1():
    a=np.random.random()

def f2():
    a=random.random()

comp=core.comparator(f1, f2)
comp.compare(testTime=5)

comp.printResults(showDetails=True)
