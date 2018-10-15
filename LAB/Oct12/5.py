# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 12:12:15 2018
White/ Glass box testing: Full paths cover and Equivalent classes


Definition: 
An equivalence-input class คือ เซตของค่าของอินพุท ที่เราคาดหวังว่าจะให้เอาพุทชุดที่คล้ายคลึงกัน ภายใต้โปรแกรมที่เราทำการทดสอบ  
(An equivalence class is a set or range of input domain values that can reasonably be expected to cause “similar”
responses from the application under test)
ยกตัวอย่างเช่น 

"""
def sign(x):
    ''' 
    input: an integer x
    output: sign of x 
    Ex: sign(-7) = 'negative', sign(3) = 'plus' sign(0) = 'zero' 
    '''
    if x > 0:
        return ('plus')
    elif x == 0:
        return ('zero')
    else:
        return ('negative')
"""
How many equivalence classes do we have here?
เราจะเห็นได้ว่าในกรณีฟังชัน sign เราสามารถแบ่ง equivalence classes ออกได้เป็น 3 classes ได้แก่ 
1) Equivalence-input class สำหรับ 'plus'  ได้แก่ x= [1,2,3,4,.... ) 
2) Equivalence-input class สำหรับ 'negative'  ได้แก่ x= ( ...., -3, -2 , -1]
3) Equivalence-input class สำหรับ 'zero' ได้แก่ x = [0]

ซึ่งเราจะสังเกตุได้ว่า ในการทดสอบ  fullpath testing นั้นเราไม่จำเป็นต้องทำการทดสอบ input ทุกจำนวน เพียงแค่
เลือกสมาชิกในแต่ละ class มาอย่างละหนึ่งตัวเพื่อทำการทดสอบ ก็เพียงพอแล้ว Ex x = [ -5, 0 ,1 ]

Self-check: ให้น้อง ๆ ลองลืมพยายามลืม definition ของ sign ฟังก์ชั่นแล้วดูที่ code อย่างเดียว
น้อง ๆ สามารถอนุมาน equivalence classes ของโปรแกรมได้หรือไม่

"""

     
def comp(x):
    if x<3:
        print('A')
    elif x > 10 :
        print('B')
    else:
        print('C')
        

"""
Note: เพื่อความสะดวกในการเเสดงผล น้อง ๆ สามารถคิดว่า print เป็น return output

0) โดเมนของ input คืออะไร  ?   set ของ output คืออะไร ?




1) ให้น้อง ๆ อธิบาย Equivalence classes ของตัวแปร x สำหรับ function comp(x)     




2) ให้น้อง ๆ ยกตัวอย่างเซตของ Test cases ที่ผ่านโปรแกรม path ทั้งหมด   
    





"""
        
def comp2(x,y):
    if x == y:
        print('A', end =' ')
    elif x < 5 and y > 2:
        print('B', end =' ')
    if x > 2 or y > 4:
        print('C', end= ' ')
    
"""
0) อธิบายชนิดโดเมนของ อินพุท  และ set ของ output คืออะไร ? 




1) ในการ call function comp2(x,y)  แต่ละครั้งจะมีการ print ค่าออกมาได้มากที่สุดกี่ครั้ง และน้อยที่สุดกี่ครั้ง




***2) ให้น้อง ๆ อธิบาย Equivalence classes ของตัวแปร (x,y) สำหรับ function comp2(x,y)     




3) ให้น้อง ๆ ยกตัวอย่าง Test cases ที่ครอบคลุม equivalence classes ทั้งหมดของโปรแกรม comp2(x,y)   





"""
