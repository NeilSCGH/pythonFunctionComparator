import time
import numpy as np

def f1():
    a=np.zeros(10000)

def f2():
    a=[0]*10000


def diff():
    if counter1 + counter2 == 0: return 0
    return (counter1 - counter2)/(counter1 + counter2)

def stillTesting():
    if abs(diff()) > targetDiff: return False
    if counter1<minTime and counter2<minTime: return True
    if counter1>maxTime and counter2>maxTime: return False
    if abs(diff())<targetDiff: return True


#Params
step=10000

minTime=1
maxTime=5
targetDiff=0.10

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

print()
if d<0:
    print("Best: f1 ({}%)".format(-round(d*100)))
else:
    print("Best: f2 ({}%)".format(round(d*100)))
