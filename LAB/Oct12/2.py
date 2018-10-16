# -*- coding: utf-8 -*-
"""
TODO 
 RECURSIVE vs ITERATIVE
    1.1)     เขียนฟังก์ชั่นจาก program specification ที่กำหนดให้ โดยใช้ iterative หรือ recursive programming styles  
    (Write codes for a given program specification using iterative fn and recursive fn )
    
        a) complete function iter_mul
        b) complete function recur_mul
        c) complete function power(a,b)
  
    
    1.2) ทำการแปลงโคดจาก iterative function เป็น recursive function และจาก recursive เป็น iterative 
    (Convert a given recursive fn to iterative fn and the otherway around)
    
        a) implement fib  using iterative method 
"""


def iter_mul(a,b):
      '''
      Implement multiplication function using iterative style: 
      
      input: an interger a and a natural number b 
      output a*b  
      NOTE: only allow to use build in + function cannot use *
      '''
      # Put your code here 



def recur_mul(a,b):
      '''
      Implement multiplication function using recursive style: 
      input: an interger a and a natural number b 
      output a*b  
      NOTE: only allow to use build in + function cannot use *
      '''
      # Put your code here 
        # Base case 
      
        # Recur on the smaller problem   


def power(a,b):
      '''
      Implement power function using recursive style (without buildin **)
      input: an interger a and a natural number b
      output a^b  
      '''
      # Put your code here 




################################
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
    


##################################
def iter_fib(n):
    '''
    Implement fib in iterative style
    
    take a natural number n and return fibonacci number 
    defined as the following 
    f(0) = 0, f(1) = 1, f(n) = f(n-1) + f(n-2) 
    '''
    

