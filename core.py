import time

class comparator():
    def __init__(self, function1, function2):
        self.f1 = function1
        self.f2 = function2

        self.n=0
        self.counter1=0
        self.counter2=0

    def diff(self):
        if self.counter1 + self.counter2 == 0: return 0
        return (self.counter1 - self.counter2)/(self.counter1 + self.counter2)

    def stillTesting(self):
        return self.counter1 + self.counter2<self.testTime

    def compare(self, testTime, step=10000):
        print("Starting...",end="")
        self.testTime=testTime

        timer1 = 0
        timer2 = 0

        while self.stillTesting():
            timer1 = time.time()
            self.f1()
            self.counter1 += time.time() - timer1

            timer2 = time.time()
            self.f2()
            self.counter2 += time.time() - timer2

            self.n+=1

        print(" Done\n")

    def getResults(self):
        d=round(self.diff()*100,2)
        return self.n, d ,round(self.counter1,3), round(self.counter2,3)

    def printResults(self):
        c1=round(self.counter1,3)
        c2=round(self.counter2,3)
        d=round(self.diff()*100,2)

        print("{} runs".format(self.n))
        print("Total for f1: {} secs".format(c1))
        print("Total for f2: {} secs".format(c2))

        print()
        if d<0:
            print("Best: f1 ({}%)".format(-d))
        else:
            print("Best: f2 ({}%)".format(d))