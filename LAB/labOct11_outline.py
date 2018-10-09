# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 10:05:38 2018

@author: Thanaphon Tangchoopong
Goals: 1) Understand basic concept of Mathermatical Induction
       2) Connection between recursive function and mathermatical induction
            - advantage and disadvantage of recursive fn
       3) The equivalent of iterative and Recursive function 
       4) TEST cases



Goals:  1) Understand basic concept of Mathermatical Induction

        2) Connection between recursive function and mathermatical induction
            - advantage and disadvantage of recursive fn
HW:     
0) Mathermatical induction 
    จงพสูจน์ ประโยคต่อไปนี้โดยอาศัย Mathermatical induction 
    Theorem: สำหรับจำนวนนับ x ใด ๆ  กำหนดให้ฟังก์ชัน f(n) =  from{i = 1}_to{ i = n } (2*i - 1)  then f(n) = n^2
    Theorem: sum from{i = 1}_to{ i = n } (2*i - 1)  = n^2  
    
    Proof: 
    Base case:
        

        
        
    IH:
        
        
        
        
    IS:
        
    
        
        
        
    
##############################################################################        
Example: 
        
     Theorem: ค่าแสตมไปรษณียากรใด ๆ ที่มากกว่าหรือเท่ากับ 8 บาท สามารถเเทนได้ด้วย 
     การใช้เเสตมในราคา 3 และ 5 บาท;  k = 5m + 3n forall m,n in NAT
     
     Ex:  8 = 5x1 + 3x1  
          9 = 3x3
          10 = 5x2
          11 = 5x1 + 3x2 
          
          and so on. 
          
          
     
     Proof:  
         
         Base Case: ค่าอากรไปรษณีย์ 8 บาท = สามารถใช้แสตม 5 และ 3 อย่างละหนึ่งดวง 
         
         
         Inductive vairable k = 5m + 3n for all nat m,n 
         กำหนดให้ inductive variable เป็น k แทนค่าอากรตั้งแต่แปดบาทขึ้นไป 
         จาก Theorem สามารถเขียนได้ว่า มีจำนวนเต็มบวก m,n ใด ๆ ที่ ทำให้ สมการ
         k = 5m + 3n  เป็นจริงเสมอ 
          
         IH: assume the Theorem    is true for all  n > k >= 8
         
         IS: let k = 5m + 3m -> for k+1
         Remember that our goal is to show that: K+1 = 5m' + 3n' 
         
         CASES 
         NOTE: Observation both m and n cannot be 0
         
         
             if m > 0
             # REMOVE one 5 and add two 3s
             k = 5m + 3n  from IH
             k+1 = 5m + 3n + 1
             k+1 = 5(m-1) + 3(n) + 6 
                 = 5(m-1) + 3(n+2)
                else
             # REMOVE three 3 and add two 5s 
             k+1 = 5(m+2) +3(n-3)
         
"""
    
## This code uses pass by reference    
def stamps(k,m,n):
    '''
    Input an integer k
          non empty list m,n 
    output: None, print k = 5m+3n
    '''
    # BASE CASE
    if k == 8:
        m[0] = 1
        n[0] = 1
        print('k:%d =5* %d + 3*%d' % (k, m[0],n[0]))  

    else:
        #Recurse on the smaller input
        stamps(k-1,m,n)
        
        # กรณีที่ เรามีเเสตมราคา 5 บาทอยู่ใน current solution (ค่า m ไม่เท่ากับ 0)
        # เราสามารถ เพิ่มค่า k = k +1 ได้โดยการ เอาแสตมราคา 5 บาทออก 1 ดวง แล้วเอาแสตมราคา
        # 3 บาท สองดวงใส่เข้าไป 
        
        if m[0] > 0:
            n[0] = n[0] + 2
            m[0] = m[0] - 1
            print('k:%d =5* %d + 3*%d' % (k, m[0],n[0]))  

        else:
            
        # หรือ ถ้าเราไม่มีเเสตมราคา 5 บาทอยู่ใน current solution
        # เราสามารถ เพิ่มค่า k = k +1 ได้โดยการ เอาแสตมราคา 3 บาทออก 3 ดวง แล้วเอาแสตมราคา
        # 5 บาท สองดวงใส่เข้าไป 
        
            m[0] = m[0] + 2
            n[0] = n[0] - 3
            print('k:%d =5* %d + 3*%d' % (k, m[0],n[0]))  

# Example 
stamps(13,[1],[1])

"""
Open the following link and trace how the above code work on Pythontutor

https://goo.gl/dgSq1i

ANSWER the following question:
How many local stamps' frame were created  when running  stamps(13,[1],[1])?  

What would be the answer for stamps(1234,[1],[1])? 

What would be the answer for stamps(123456,[1],[1])? 


Implement iterative function for stamps problem. 
"""
def stamps_iter(n):
  '''
  
  '''  
    # define your code here 
    
 

"""
###############################################################################
##  OPTIONAL 
###############################################################################
use Bisection method to find what is an appoximate maximum depth of recursion 
your python can handle. (USE try and catch the exception on your bisection method)
Try to convert this recursive function to an iterative function. 

"""


import math

###############################################################################
#   Example of using global variable
def set_Global():
    global Gobalvar
    Gobalvar  = 1

def inc_Global():
    global Gobalvar
    Gobalvar = Gobalvar + 1
    
def print_Global():
    print(Gobalvar)



###############################################################################
#  Solution to the optional question
###############################################################################    
def bisec_depth(l,u,f):
    print (l,u)
    # termination condition
    if u<=l:
        print ("Limit of the current heap is:")
        print (l,u)
        return 
    
    try: 
        p = math.floor((l+u)/2)
        # calling f with p = middle value
        
        f(p,[1],[1])
        # if pass then adjust lower bound = p 
        print("Bisection current guess: p= %d" % p)
        l = p      
    except RecursionError:
        print( "RECURSION ERROR: p = %d " % p)
        # We hit the error -> have to reduce our upper bound
        u = p 
        
    finally:
        inc_Global()
        print_Global()
        bisec_depth(l,u,f)
        
        
###############################################################################        
# TEST 
set_Global()
bisec_depth(0,4000,stamps)

import sys
sys.getrecursionlimit()

# why it's not equal? 
###############################################################################



def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


#################################
def fib(n):
    '''
    take an integer n and return fibonacci number 
    defined as the following 
    f(0) = 0, f(1) = 1, f(n) = f(n-1) + f(n-2) 
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+ fib(n-2)
    

#  What are the test cases for this example that give explore all condition?  
    


    
########################################################################    
 # Fixed the above function to cover fibonacci of negative number 
########################################################################
#    HINT:  
#    F(n) = F(n-1) + F(n-2)
# 
######################################################################## 
#     F(n-2) = F(n) - F(n-1)  
#     F(-1)  = F(1) - F(0)
#     Can you guess the formula? of F(-n)?   
# 
#     use iteration method to enumerate F(-2),........ F(-10)
#     What is the relation between F(n) and F(-n) ?  
#     now it's time to fixed the code 
########################################################################
"""
1) RECURSIVE vs ITERATIVE
    1.1)     เขียนฟังก์ชั่นจาก program specification ที่กำหนดให้ โดยใช้ iterative หรือ recursive programming styles  
    (Write codes for a given program specification using iterative fn and recursive fn )
    
    
 

    
    
    1.2) ทำการแปลงโคดจาก iterative function เป็น recursive function และจาก recursive เป็น iterative 
    (Convert a given recursive fn to iterative fn and the otherway around)
    
        a) implement fib  using iterative method 
        b) implement plus and power funcrtion using both iterative and recursion methhods 


    
    

2) TEST CASES 
    Black box testing 
    2.1.1 given a function specification
    come up with hypothesis followed by test cases that might break the code 
    
    
    
    
    
    
    
    fill out the following table
        
    
    
    Glass box testing
    2.1 Identify the test cases that give path-complete for the given functions
    2.2 Understand the basic syntax for try and catch  
    
"""
