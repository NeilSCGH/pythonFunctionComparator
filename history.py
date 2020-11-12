###############################################
##Faster
#import os.path
if os.path.isfile("main.py"):
    a=True

##Slower
#from pathlib import Path
if Path("main.py").is_file():
    a=True

###############################################
##Faster
a=[0]*50

##Slower
#import numpy as np
a=np.zeros(50)

###############################################
##Faster
a=random.random()

##Slower
#import numpy as np
a=np.random.random()

###############################################
##Identical
a=25*25*25

##Identical
a=25**3