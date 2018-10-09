# -*- coding: utf-8 -*-
"""
GOAL:
Full path test cases + fixing the code using your induction on the relation of the function
  
TODO:    
  1) Give the test cases for the given codes that explore all condition?  
  2) Fixed to code to handle a negative input value. 
  

"""

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
        
# WHAT are the corner boudaries for this fib function? 


    
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


def fib_neg(n):
    '''
    take any integer n and return fibonacci number 
    defined as the following 
        f(0) = 0, f(1) = 1, f(n) = f(n-1) + f(n-2) 
    '''
    #put your code here










