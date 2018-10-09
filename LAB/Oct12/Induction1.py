# -*- coding: utf-8 -*-
"""
Goals:  1) Understand basic concept of Mathermatical Induction

        2) Connection between recursive function and mathermatical induction
            - advantage and disadvantage of recursive fn
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
a = [1]
b = [1]
stamps(13,a,b)


### TODO ####
"""
1)  Open the following link and trace how the above code work on Pythontutor

     https://goo.gl/dhQzau

ANSWER the following question:

2 ) How many local stamps' frame were created  when running  stamps(13,[1],[1])?  

3)  What would be the answer for stamps(1234,[1],[1])? 

4)  What would be the answer for stamps(123456,[1],[1])? 

5 ) Implement an iterative function for stamps problem.


"""




