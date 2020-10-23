from core import *
import numpy as np

def f1():
    a=[0]*50

def f2():
    a=np.zeros(50)

comp=comparator(f1, f2)
comp.compare(1)

comp.printResults()