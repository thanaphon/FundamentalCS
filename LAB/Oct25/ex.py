# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 14:02:52 2018

@author: computer
"""

# TRY EXCEPTION
# SYNTAX 

# Build in exceptions https://docs.python.org/3/library/exceptions.html#bltin-exceptions

try:
    
    #NameError statement 1
#    print("Try accessing a non defined variable")
#    a_non_defineVar
    
    #Index error
    x = ['item0']
#    x[1]
    
    #AttributeError
#    print(dir(x))  # list all attibute of a  
#    x.tryToReachAnUndefinedAttribute 
    
    #Type error 
#    3 + 'a'
    
    raise Exception    
    assert len(x) <= 0 
    
    print('Ohhh')
    
except NameError:
    print('Name error')

except IndexError:
    print('Try to access an unallocated memory')

except AttributeError:
    print('Try accessing a non defined attribute')

except TypeError:
    print('expect a different input')
    
except ValueError:
    print('Value error')

except AssertionError:
    print ('Precondition does not meet')
    
except Exception:
    print('BOO BOO')



    


    
    