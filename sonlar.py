# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 21:59:22 2025

@author: abdur
"""

#a = 20
#b = 2.3
#temp = 36.6
#print(type(b))

#aholi_soni = 7_567_458_245
#print("Aholi soni ", aholi_soni)

#x, y, z = 12, 5.5, -45
#print(x + y + z)

#c = a*b
#d = 100/5

#radius = 20
#PI = 3.14159
#diametr = 2*radius
#print("Aylana uzunligi=", PI*diametr)

#ism = "Jobir"
#yosh = 24
#yosh = str(yosh) #str matn holiga o'tkazar ekan. Odatda bunday usulda o'zgartirish yaxshi emas ekan. Chunki kelajakda biz yosh degan o'zgaruvchidan yana foydalanishimiz mumkin

#xabar = ism + ' '+ str(yosh) + 'yoshda'
#print(xabar)

#t_yil = int(input("Tug'ilgan yilingiz qachon2?\n>>>"))# Bu yerda int()funksiyasi berilgan matnni butun son ko'rinishiga o'tkazar ekan.

#yosh = 2025-t_yil
#print("Siz ", yosh, "yoshda ekansiz")


#a = int("10")
#b = float("10")
#c = str(5.5)

import re

text = "Call 408-555-1234 or 203-555-1324 for assistance."
matches = re.findall(r'\d{3}-\d{3}-\d{4}', text)
print(matches)  # Output: ['408-555-1234', '203-555-1324']
