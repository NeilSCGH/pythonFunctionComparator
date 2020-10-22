import time
import numpy as np

def f1():
    a=[0]*10

def f2():
    a=[0]*1000



counter1=0
counter2=0

timer1 = 0
timer2 = 0

n=0

for i in range(1000000):
    timer1 = time.time()
    f1()
    counter1 += time.time() - timer1

    timer2 = time.time()
    f1()
    counter2 += time.time() - timer2

    n+=1


print(n)
print(counter1)
print(counter2)