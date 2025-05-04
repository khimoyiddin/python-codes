# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 11:02:59 2025

@author: abdur
"""

### if/else operatorlari haqida
#avtolar = ['bmw', 'kia', 'audi', 'gm', 'hyundai']
#print(avtolar)
#for avto in avtolar:
#    print(avto)
#    print(avto.title())
    
#avtolar = ['bmw', 'kia', 'audi', 'gm', 'hyundai']
#for avto in avtolar:# avtolar ichidagi har bir element uchun
#    if avto == 'bmw':# agar avto bmw ga teng bo'lsa (== belgisi 'tengmi' degan ma'noni bildiradi)
#        print(avto.upper())# har bir harfini katta harflarda chiqar 
#    else:#aks holda...
#        print(avto.title())# faqat bosh harflarini katta harfga aylantirib chiqar
      
##### == - 'tengmi', != - 'teng emasmi' deganidir 
##### >= - 'katta yoki teng', <= - 'kichik yoki teng'
##### > - 'katta', < - 'kichik'       
      
           
#ism = "Ali"
#ism.lower() == 'ali'


#ism = input('Kechirasiz, ismingiz nima?\n>>>')
#if ism.lower() != 'ali':# agar ism ali bo'lmasa 
#    print(f"Uzr, {ism.title()} biz Alini kutyapmiz")# bu body ishlaydi
#else:# agar ism ali bo'lsa 
#    print("Salom, Ali")# bu body ishlaydi
    
    
#sonlar bilan ishlab ko'ramiz
#javob = float(input("12x6 nechiga teng?\n>>>"))
#if javob != 72:
#    print("Javob xato")# 72 dan ya'ni tog'ri javobdan boshqa sonlarni kiritganimizda konsolga Javob xato deb chiqaradi. 72 kiritilganda esa hech narsa chunki else qismini kiritmadik
    
#yosh = int(input("Iltimos yoshingizni kiriting: "))
#if yosh >= 18:
#   print("Xush kelibsiz")# yosh 18 dan kichik bo'lmasa bu body ishlaydi
#else:
 #   print("18 yoshdan kichiklarga kirish taqiqlanadi") # yosh 18 kichik bo'lsa bu body ishlaydi
 
 
 
#login = input("Iltimos loginingizin yarating: ")
#if len(login) <= 5:# kiritilgan login 5 dan kam bo'lmasa
#    print("Login kamida 5 ta harfdan iborat bo'lishi kerak")# bu body ishlaydi
#else:#aks holda
#    print("Davom etish uchun'continue' tugmasini bosing")# bu body ishlaydi
 
 
#yil = int(input("Iltimos tug'ilgan yilingizni kiriting: "))
#if 2025 - yil < 18:
#    print(f" Sizni yoshingiz {2025-yil} da ekan")
#    print("Kechirasiz sizga kirish mumkin emas")
#else:
#    print("Xush kelibsiz to'rlayverasiz")
 
#yosh = int(input("Yoshingiz nechida?\n>>>"))
#if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")
 

x, y = 68, 50
print('x>y') if x>y else print('x<y') ### if hamda else operatorlarini bir qatorda ham qo'llashimiz mumkin ekan. Bunda if ni body si if dan oldin, else niki esa else dan keyinga yoziladi  