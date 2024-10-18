#!/usr/bin/python

# 10 + 11.Dictionary
data = {"Maria": 34 , "Carla": 73, "Dimitra": 22, "Gerrich": 2}
data=dict(sorted(data.items()))
for x in data:
    print("Key: " + x + " - Value: " + str(data[x]))



#12. textfile
with open("py_test1.txt", "w") as f:
    f.write("Hello World!")


#13. read
with open ("py_test1.txt", "r") as f:
    cont = f.read()
    print(cont)

#14. toString
def ReadToString(fln):
    with open(fln, "r") as f:
        cont = f.read()
    return str(cont)

tabl=ReadToString("table.csv")


def WriteStringToFile(fln, cont):
    with open(fln, "w") as f:
        f.write(cont)

WriteStringToFile("14write.txt", str(tabl))



#15. Table
print (ReadToString("table.csv"))


#16. print names
with open("table.csv", "r") as f:
    cont = f.read()
    lines=cont.split("\n")
    lines2=[]
    for i in lines:
        lines2.append(i.split(";"))

for i in lines2:
    print(i[0])




#17. sort rows
lines2.remove(lines2[0]) #remove [name age sex]
lines2.sort()
a=str(str(lines2))
WriteStringToFile("17sorted.txt", a)

#18. Sort age
lines2.remove(lines2[0])
# Python code to sort the tuples using second element
# of sublist Inplace way to sort using sort()
def Sort(sub_li):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    sub_li.sort(key = lambda x: x[1])
    return sub_li
 
# Driver Code
byage=Sort(lines2)


#19. Create dictionary
newdc={}
for i in lines2:
    newdc[i[0]]=i[1:]


if "Adam" in newdc:
    print (newdc["Adam"])
else: 
    print("Error: Name does not exist")

