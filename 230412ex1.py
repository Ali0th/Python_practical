#!/usr/bin/python

#1. birthday
for i in range(1, 61):
    print ("You are " + str(i) + " years old, so only " + str(50-i) + " years for your 50th birthday.")

# 2. cube

def cubesurf(a):
    return 6*a*a

print(cubesurf(11))


# 3. List
names=["Maria", "Carla", "Efi", "Fay", "Gerrich", "Leonidas", "Andreas"]

for x in names:
    print (x)

# 4. print
print(names[2])

#5. Hello
for x in names:
    if x=="Fay":
        print ("Hello Mister super " + x)
    else:        
        print (x)

#6. print list
def prlt(lst):
    p=1
    for x in lst:
        print(str(p) + ":" + x)
        p=p+1

#7. Helge
names[4]= "Helge"

#Exchange
def exchg(lst):
    lst[4], lst [2] = lst[2], lst [4]
    return lst

print (exchg(names))

#9. sort len
names.sort(key=len)
print(names)

