# -*- coding: utf-8 -*-
"""
Goals:  1) Understand basic concept of Mathermatical Induction

        2) Connection between recursive function and mathermatical induction
            - advantage and disadvantage of recursive fn
            ##############################################################################        
Example: 
       
     แนวคิด:  
     การพิสูจน์ในลักษณะนี้สามารถเปรียบเทียบได้กับ การที่เราเรียงตัวต่อโดมิโนแบบไม่มีที่สิ้นสุดแล้วบอกว่า หากโดมิโนตัวเเรกล้ม ตัวถัดไปจนถึงตัวสุดท้ายจะล้มตามไปด้วย  
     การพิสูจน์ในลักษณะนี้จะสมบูรณ์ได้ เราจำเป็นต้องอธิบายจุดเริ่มต้นด้วยการพิสูจน์หรือเเสดงให้เห็นว่าโดมิโนตัวเเรกล้มอย่างถูกต้อง และวิธีการล้มของตัวโดมิโนตัวถัดไป  
     
     ตัวอย่าง:
     
     Theorem: ค่าแสตมไปรษณียากรใด ๆ ที่มากกว่าหรือเท่ากับ 8 บาท สามารถเเทนได้ด้วย 
     การใช้เเสตมป์ในราคา 3 และ 5 บาท;  k = 5m + 3n forall m,n in NAT
     
     Ex:  8 = 5x1 + 3x1  
          9 = 3x3
          10 = 5x2
          11 = 5x1 + 3x2 
          
          and so on. 
          
          
     
     Proof:  
         
         Step 0)
         Let k >= 8 be our inductive vairable: k = 5m + 3n for all nat m,n 
         กำหนดให้ inductive variable เป็นตัวแปร k แทนค่าอากรตั้งแต่แปดบาทขึ้นไป 
         จาก Theorem สามารถเขียนได้ว่า เราสามารถหาจำนวนเต็มบวก m,n ใด ๆ ที่ ทำให้ สมการ
         k = 5m + 3n >= 8 เป็นจริงได้เสมอ 
         
         Step 1)
         Base Case (BC): ค่าอากรไปรษณีย์ราคา 8 บาท = สามารถใช้แสตมป์ 5 บาท และ 3 บาท อย่างละหนึ่งดวง (m = 1, n = 1)
         (เปรียบเทียบได้กับการล้มของโดมิโนตัวเเรก)
          
         Step 2)
         Inductive Hypothesis (IH): assume the Theorem    is true for all  k >= 8
         *** สมมุติให้ theorem นั้นเป็นจริง สำหรับทุก ๆ จำนวนนับที่มีค่ามากกว่าหรือเท่ากับแปดจนถึงค่า k ***
         (สมมุติให้ โดมิโนได้ล้มมาเรื่อย ๆ จนถึงตัวลำดับที่ k) 
        
         Step 3)
         Inductve Step(IS): ต้องแสดงให้เค้าเห็นว่า โดมิโนตัวถัดไปจะล้มได้อย่างไร โดยใช้สมมติฐานที่เราตั้งขึ้น  ***แต่อย่าลืมว่าเราไม่สามารถ
         ใช้สมมติฐานของเรากับค่าอากรไปรษณีย์ราคา (k+1) ได้โดยตรง เพราะเราสมมุติว่า สมุมติฐานของเราถูกจนมาถึงเพียงแค่ตัวที่ k 
         ดังนั้นเราต้องแสดงให้ เคาเห็นว่าตัวถัดไป (k+ 1) จะล้มได้อย่างไร
         
         for k+1: our hypothesis is still hold.
         Remember that our goal is to show that: K+1 = 5m' + 3n' 
         
         
         CASES 
         NOTE: Observation both m and n cannot be 0
         ข้อสังเกตุ: ค่า m และ n ที่ทำให้สมมติฐานที่ตั้งไว้เป็นจริง ไม่สามารถเป็น 0 พร้อมกันได้
         
         กรณีที่ค่า m มีค่ามากกว่า 0 
             if m > 0
             # REMOVE one 5 and add two 3s
             จากสมมติฐานที่ว่า ค่าอากรราคา k สามารถ เเสตมป์ 5 บาท m ดวงและ 3 บาท n ดวง
             ซึ่งถ้าค่าอากรเพิ่มเป็น k+1 เราสามารถเอาเเสตมป์ 5 บาท ออกหนึ่งดวง แล้วเอาเเสตมป์ราคา 3 บาทสองดวง ใส่เข้าไปแทน
             
             k+1 = (5m + 3n) + 1   from IH
             k+1 = 5(m-1) + 3(n) + 6 
                 = 5(m-1) + 3(n+2)
             else
             # REMOVE three 3 and add two 5s 
             หรือกรณีที่ m == 0 เราสามารถเอา เราสามารถเอาเเสตมป์ 5 บาทใส่เข้าไปสองดวง แล้วเอาเเสตมป์ราคา 3 บาทสามดวงออก
             k+1 = (5m + 3n) + 1   from IH
             k+1 = 5(m+2) +3(n-3)
             
         
         จากการพิสูจน์ในส่วนของ BC และความสอดคล้องของ สมมติฐานเเละ IS ทำให้ สรุปได้ว่า Theorem ที่กำหนดให้นั้นถูกต้อง
         
         
         ในส่วนถัดไปน้อง ๆ จะได้เห็นถึงความสัมพันธ์ของ Mathermatical induction กับ การเขียน โปรแกรมในแบบ recursion.   
         ให้เราลองศึกษา code และเอาไปลอง run ดูใน pythontutor แล้วลองแก้ปัญหานี้โดยใช้ loop ธรรมดาแทนการเรียนโดยใช้ recursion
         ลองแก้ recursion code ให้เป็นการใช้ dict เพื่อบันทึกคำตอบ ลองดูตัวอย่างจาก fibonacci function ใน class 
         ในกรณีนี้ base case เป็น store_data = {8:(1,1)}
"""

    
## This code uses pass by reference    
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


def stamps_iter(n):
    '''
    Input an integer n >= 8
    output: None, print for k=1 to n :  k = 5m+3n
    '''



