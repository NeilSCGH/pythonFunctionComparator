import time
import numpy as np

def f1():
    a=[0,0,0,0,0,0,0]

def f2():
    a=[0]*7


def diff():
    if counter1 + counter2 == 0: return 0
    return (counter1 - counter2)/(counter1 + counter2)

def stillTesting():
    return counter1 + counter2<testTime


#Params
step=10000

testTime=3

#init
n=0
counter1=0
counter2=0
timer1 = 0
timer2 = 0

while stillTesting():
    timer1 = time.time()
    for i in range(step): f1()
    counter1 += time.time() - timer1

    timer2 = time.time()
    for i in range(step): f2()
    counter2 += time.time() - timer2

    n+=1*step


print("{} runs".format(n))
print("Total for f1: {} secs".format(round(counter1,3)))
print("Total for f2: {} secs".format(round(counter2,3)))

d=diff()
print()
if d<0:
    print("Best: f1 ({}%)".format(-round(d*100,2)))
else:
    print("Best: f2 ({}%)".format(round(d*100,2)))
