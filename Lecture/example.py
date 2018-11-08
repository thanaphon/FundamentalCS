# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 09:00:53 2018

@author: computer
"""
class Person(object):    
    def __init__(self,name,age, h, w, gender):
        self.name = name
        self.age = age
        self.heigh = h
        self.weight = w
        self.gender = ""
        
    def __str__(self):
        return ("My name is {}.\n I am {} year old.\n I am {} cm tall. ".format(self.name, self.age, self.heigh) )

class Student(Person):
    def __init__(self,name, age, h,w,gender, ID):
        self.ID = ID
        Person.__init__(self,name,age,h,w,gender)
    
    def speak(self):
        print(" My name is {}.\n I am a good student.".format(self.name))
    
class TA(Person):

    def __init__(self,name, age, h,w,gender,  subject):
        self.subject = subject
        Person.__init__(self,name,age,h,w,gender)
    def speak(self): 
        print("My name is {}.\n I am an awesome TA".format(self.name))
        

MissA = Person("Apple", 12, 130, 40, 'Female')
MrB = Person("Bob", 13, 135, 50, 'Male')

print(MissA)
print(MrB)

StuA = Student("Bob", 13, 135, 50, 'Male',12345)
print(StuA)
StuA.speak()





    
    
    