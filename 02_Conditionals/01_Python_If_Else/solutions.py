import math
import os
import random
import re
import sys
n=int(input())
if n%2!=0:
    print("Weird")
elif 2<=n<=5: #here er can add else: and then if 2<=n<=5 or we can directly write it as elif statement it is easy to write the elif statmentwe cannot use every time else soo instead we can use elif 
    print("Not Weird")
elif 6<=n<=20:
    print("Weird")
else:
    print("Not Weird")
