from core import *
import numpy as np

def f1():
    a=2*2*2*2

def f2():
    a=2**4

comp=comparator(f1, f2)
comp.compare(testTime=1)

comp.printResults(showDetails=True)