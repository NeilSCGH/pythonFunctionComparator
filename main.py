import time
import numpy as np

def f1():
    a=[0]*50

def f2():
    a=np.zeros(50)


def diff():
    if counter1 + counter2 == 0: return 0
    return (counter1 - counter2)/(counter1 + counter2)

def stillTesting(counter1, counter2, testTime):
    return counter1 + counter2<testTime

def compare(function1, function2, testTime=5, step=10000):

    #init
    startTime=time.time()
    n=0
    counter1=0
    counter2=0
    timer1 = 0
    timer2 = 0

    while stillTesting(counter1, counter2, testTime):
        timer1 = time.time()
        f1()
        counter1 += time.time() - timer1

        timer2 = time.time()
        f2()
        counter2 += time.time() - timer2

        n+=1

    return n, counter1, counter2

n, counter1, counter2 = compare(f1, f2, 5)
print("{} runs".format(n))
print("Total for f1: {} secs".format(round(counter1,3)))
print("Total for f2: {} secs".format(round(counter2,3)))

d=diff()
print()
if d<0:
    print("Best: f1 ({}%)".format(-round(d*100,2)))
else:
    print("Best: f2 ({}%)".format(round(d*100,2)))