# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:15:17 2018

@author: computer
"""


# WHY do we need OOP? 
# -> common data and methods 

C1_name = 'Jelly'
C1_age = 1
C1_color = 'brown'
C1_breeding = 'Siam'


C2_name = 'Tiger'
C2_age = 2
C2_color = 'black'
C2_breeding = 'Siam'

C3_name = 'TongDee'
C3_age = 3
C3_color = 'white'
C3_breeding = 'Persia'

C4_name = 'Bean'
C4_age = 5
C4_color = 'yellow'
C4_breeding = 'Persia'

C5_name = 'Jeff'
C5_age = 1
C5_color = 'grey'
C5_breeding = 'Persia'



R1_name = 'Kat'
R1_age = 2
R1_color = 'brown'
R1_maxHop = 4

R2_name = 'NumChok'
R2_age = 1
R2_color = 'black'
R2_maxHop = 3


R3_name = 'Jimmy'
R3_age = 3
R3_color = 'white'
R3_maxHop = 2



##################################
class Cat(object):
    def __init__(self,name,age,color,bleeding):
        self.name = name
        self.age = age
        self.color = color
        self.bleeding = bleeding 
        
class Rabbit(object):
    def __init__(self,name,age,color,hop_dist):
        self.name = name
        self.age = age
        self.color = color
        self.hop_dist = hop_dist
        
        

c1 = Cat('Jelly', 1, 'brown','Siam')
c2 = Cat('Tiger', 2, 'black','Persian')

r1 = Rabbit('Kapom', 1, 'brown',2)
r2 = Rabbit('Jimmy', 2, 'black',3)

#################################

