# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 09:46:37 2018

@author: Ojo
"""

def stamps(k,m,n):
    '''
    Input an integer k >= 8 
          non empty list m,n 
    output: None,  print('k:%d =5* %d + 3*%d' % (k, m[0],n[0]))  
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
a = [1]
b = [1]
stamps(13,a,b)



def stamps2(k,m,n):
    '''
    Input an integer k >= 8 
          non empty list m,n 
    output: None,  print('k:%d =5* %d + 3*%d' % (k, m[0],n[0]))  
    '''
    # BASE CASE
    if k == 8:
        m[0] = 1
        n[0] = 1
        print('k:%d =5* %d + 3*%d' % (k, m[0],n[0]))  

    else:
        #Recurse on the smaller input
        stamps(k-1,m,n)
        
        # กรณีที่ เรามีเเสตมราคา 3 บาทอยู่ใน current solution (ค่า n ไม่เท่ากับ 0)
        # เราสามารถ เพิ่มค่า k = k +1 ได้โดยการ เอาแสตมราคา 5 บาทเข้าไป 2 ดวง แล้วเอาแสตมราคา
        # 3 บาท สามดวงออก 
        
        if n[0] > 0:
            n[0] = n[0] - 3
            m[0] = m[0] + 2
            print('k:%d =5* %d + 3*%d' % (k, m[0],n[0]))  

        else:
            
        # หรือ ถ้าเราไม่มีเเสตมราคา 3 บาทอยู่ใน current solution
        # เราสามารถ เพิ่มค่า k = k +1 ได้โดยการ เอาแสตมราคา 5 บาทออก 1 ดวง แล้วเอาแสตมราคา
        # 3 บาท สองดวงใส่เข้าไป 
        
            m[0] = m[0] - 1
            n[0] = n[0] + 2
            print('k:%d =5* %d + 3*%d' % (k, m[0],n[0]))  
            

def stamps_memo(k,d):
    '''
    Adding memorization:  
    '''
    print ('I am calling  stamps_memo(', k,d,')')
    if k in d:
            # Check in data dict
            print('return form base case k =',k)
            return(d[k])
    else:    
        # if there is no key k yet
            (m,n) = stamps_memo((k-1),d) 
            if m > 0:
                ans = (m-1,n+2)
                print('add',k,'=', ans)
                d[k] = ans
            else:
                ans = (m+2,n-3)  
                print('add',k,'=', ans)
                d[k] = ans
            return (ans)

d = {8:(1,1)}

def stamps_iter(k):
    '''
    Input an integer k >= 8 
         
    output: None,  print('k:%d =5* %d + 3*%d' % (k, m,n)) 
    
Ex  stamps_iter(15)
    
k:8 =5* 1 + 3*1
k:9 =5* 0 + 3*3
k:10 =5* 2 + 3*0
k:11 =5* 1 + 3*2
k:12 =5* 0 + 3*4
k:13 =5* 2 + 3*1
k:14 =5* 1 + 3*3
k:15 =5* 0 + 3*5
    '''
    
    for i in range(8,k+1):
        if i == 8:
            m = 1
            n = 1
            print('k:%d =5* %d + 3*%d' % (i, m,n))  
        elif m == 0:
            m = m + 2
            n = n - 3
            print('k:%d =5* %d + 3*%d' % (i, m,n))  

        else:
            m = m - 1
            n = n + 2
            print('k:%d =5* %d + 3*%d' % (i, m,n))  

        