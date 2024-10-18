#!/usr/bin/python
def sqrt(x):
    return x**2

def evenor(y):
    if (y % 2) == 0:
        print ("even")
    else:
        print ("odd")

for i in range(1, 21):
    evenor(sqrt(i))
   