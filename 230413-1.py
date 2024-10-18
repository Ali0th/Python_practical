#!/usr/bin/python

class Animal:

    def __init__(self, name):
        self.age=1
        self.name=name
        self.c=0
            
    def nam(self):
        print ("Hello, my name is " + self.name)

    def baptism(self, new_name):
        if self.c==0:
            self.name=new_name
            print("My new name is " + self.name + ". Thanks!")
            self.c+=1
        else:
            print("You can change my name only once. Sorry!")


    def birthday(self):
        print("Happy birthday!")
        self.age+=1
    
    def sayAge(self):
        print("I am " + str(self.age) + " years old!")

    def breath(self):
        print ("Breath in, breath out.")



    
class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)    

    def nam(self):
        print ("My Dog name is " + self.name)

    def bark(self, times):
        for i in range(0, times):
            print ("Woof!")
        
    def birthday(self):
        print ("Happy Dog Birthday!")
        self.age+=7
        



if __name__=="__main__":
    lassie=Dog("Max")
    lassie.nam()
    lassie.bark(2)
    lassie.sayAge()
    lassie.birthday()
    lassie.sayAge()
    lassie.baptism("Naja")
    lassie.bark(3)
    lassie.baptism("Rita")
    lassie.bark(1)



if __name__=="__main__":
    bear=Animal("Sussie")
    bear.nam()
    bear.sayAge()
    bear.birthday()
    bear.sayAge()
    bear.baptism("Dimi")
    bear.baptism("Daphne")
