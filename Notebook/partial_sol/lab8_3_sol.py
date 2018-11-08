# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 01:05:53 2018

@author: Ojo

ให้น้อง ๆ เขียนโปรแกรม เพื่อทำงานดังต่อไปนี้

1) ทำการรับอินพุทสามตัวจากยูสเซอร์โดยบังคับให้ อินพุท ตัวเเรกเป็น integer และตัวที่สองเป็น float  ตัวที่สามเป็น integer ระหว่าง [0...10]  
หากยูสเซอร์ คีย์ อินพุทนอกเหนือจากนี้ ให้เราทำการเอาท์พุทข้อความบอกยูสเซอร์ ว่า type ของอินพุท ที่ต้องการคืออะไร 
กำหนดให้ อินพุทเป็น variable x, y ,z ตามลำดับ

2) ทำการคำนวณ f(w) สำหรับค่า w ตั้งแต่ 0 ถึง z 
  แล้วบันทึกเก็บไว้ใน data dict d[w] = f(w)
  หาก f(w) ไม่สามารถหาค่าได้ ให้ เก็บเป็นค่าเป็น None และ print warning message เกี่ยวกับปัญหาที่เกิดขึ้น   
      
 f(w) = log(y+w) / (x - w)    

Hint: import math   for log function

3) output ผลลัพท์ของ data dict   

"""
import math
def main():
    
    # Loop for taking input x
    while True: 
        try:
            x = int(input('please enter an integer number \n'))        
            break
        except ValueError:
            print( "That doesn't look like an integer number!" )
            
    # Loop for y        
    while True: 
        try:
            y = float(input('please enter a float number \n'))                
            break
        except ValueError:
            print( "That doesn't look like a float number!" )

            
    #Loop for z    
    while True: 
        try:
            z = input('please enter an integer number [0 10]\n')
            intz = int(z)
            if 0 <= intz <= 10:
                z = intz
                break
        except:
            print( "That doesn't look like an integer number [0 10]!" )
            
    d = {}
    
    
    for w in range(0,z+1):  
        try:
            temp = math.log(y+w) / (x - w)
            d[w] = temp
        except ValueError:
            
            print(' log cannot take nagative value ')
            d[w] = None 
        except ZeroDivisionError:
            print(' denominator cannot be 0 value ')
            d[w] = None 
        except:
            print (' Something else')
            d[w] = None 
         
    
    print(d)
            
        
        
                