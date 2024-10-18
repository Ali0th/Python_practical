#!/usr/bin/python


def rout(a):
    if a<=50:
        years=50-a
        print ("The person has " + str(years) + " left until their 50th birthday.")
    else:
        print ("They are over 50 already.")

age=74
rout(age)

age=22
rout(age)