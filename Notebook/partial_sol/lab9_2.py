# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 18:20:09 2018

@author: computer
"""

class Person(object):
    def __init__(self,name = None ,surname = None ,age = None ):
        print('call init Person object')
        self.__name  = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return(self.__name)
        
    def set_name(self,newName):
        self.__name = newName
        
    def get_surname(self):
        return(self.__surname)
        
    def set_surname(self,newsurName):
        self.__surname = newsurName
        
    def get_age(self):
        return(self.__age)
        
    def set_age(self,newage):
        self.__age = newage    
        
    def __str__(self):
        return("My name is {}".format(self.get_name()))
        
class Student(Person):
    countStudent = 1
    def __init__(self,name = None ,surname = None ,age = None ):
        print('call init Student object')
        Person.__init__(self,name,surname, age)
        self.organization = []
        self._studentID = Student.countStudent
        Student.countStudent += 1

    def __str__(self):
        return('My name is {}. My ID is {}'.format( self.get_name(),self._studentID))
    
    def __eq__(self,other):
        return (self._studentID == other._studentID)
    
    def apply(self,organization):
        if organization in self.organization:
            print('{} is already in the organization'.format(self.get_name()))
        else:
            if organization.eval_apply(self):
                self.organization.append(organization)
            else:
                print('Application got rejected')
            
            
    
class StudentOrg(object):
    def __init__(self,clubName, founder):
        print('Call init StudentOrg object')
        assert len(founder.organization) == 0, 'Only one club per student'
        self.clubName = clubName
        self.president = founder 
        self.members = [self.president]
        founder.organization.append(self)          
    
    def add_mem(self,stud):
        if stud not in self.members:
            self.members.append(stud)
        
    def eval_apply(self, stud):
        if (len(stud.organization) > 0) : # ถ้ามีคลับ อยู่เเล้ว 

            return (False)
        else:
            print('Application approved')
            self.add_mem(stud)
            return (True)
        
    def __eq__(self,other):
        return (self.clubName == other.clubName)
    
    def __str__(self):
        msg =''  # ตัวเเปรสำหรับเก็บ string ที่ต้องการเเสดงผล 
        
        # สำหรับสมาชิกแต่ละคนในสโมสร  ดึงชื่อมาเก็บไว้ใน string tex 
        for item in self.members:
            msg += item.get_name() + '\t'  # \t ใช้สำหรับ แทนช่องว่างหรือการแทบ 
        # ถ้ามีสมาชิกเพียงคนเดียว รีเทอร์น ข้อความแบบนี้
        if len(self.members) == 1:
            return ('Please join our club {}. Our president is {}'.format( self.clubName, msg))
        # ถ้ามีสมาชิกมากกว่าหนึ่งคน รีเทอร์น ข้อความแบบนี้
        return ('We are club {}. Our members are {}'.format( self.clubName, msg))
        
   
    
s1 =Student('s1','sur1',12)
print(s1)
s2 =Student('s2','sur2',13)
print(s2)
s3 =Student('s3','sur3',14)  
print(s3)
c1 = StudentOrg('C1',s1)
print(c1)
c2 = StudentOrg('C2',s2)
print(c2)
c3 = StudentOrg('C3',s3)
print(c3)

s5 =Student('s5','sur5',12)

s6 =Student('s6','sur6',13)

s7 =Student('s7','sur7',14)

#c4 = StudentOrg('c4',s1)

s5.apply(c1)
s1.apply(c1)
s6.apply(c1)
s6.apply(c2)

print(c1.members)

print(c1) 

print(c2.members)

print(c2) 