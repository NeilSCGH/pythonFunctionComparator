import core

tab=["2015","1912","209f","neil"]

def f1():
    for folder in tab:
        valid=False
        try:
            a=int(folder)
            valid = 1900<=a and a<=2099
        except:pass

def f2():
    for folder in tab:
        try:
            a=int(folder)
            assert 1900<=a and a<=2099
            valid = True
        except:
            valid=False


comp=core.comparator(f1, f2)
comp.compare(testTime=5)

comp.printResults(showDetails=True)
