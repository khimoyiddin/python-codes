# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 12:20:26 2025

@author: abdur
"""

#ism = "Khimoyiddin"
#shahar = "계룡시"
#viloyat = "Chungcheonamdo"
#smile = "🤩"
#print(smile)

#STRING ustida amallar
#ism = "Khimoyiddin"
#print("Mening ismim " + ism)

#ism = "Inomiddin"
#familiya = "Abduraxmonov"
#print(ism + familiya)
#print(ism + " " + familiya)


#f-string

#ism = "Inomiddin"
#familiya = 'Abduraxmonov'
#ism_sharif = f"{ism} {familiya}"
#print(ism_sharif)

#ism = "Khimoyiddin"
#familiya = "Abduraxmonov"
#sharif = "Sayfiddin ugli"
#print(f"Salom! Mening ismim {ism}, {familiya} {ism} {sharif}")

#MAXSUS BELGILAR
#print('Hello World')
#print('Hello \tWorld')
#print('Hello \nWorld')

#STRING METODLAR

#ism = "james"
#familiya = "bond"
#print(ism + " " +familiya)
#ism_sharif = f"{ism} {familiya}"
#print(ism_sharif.upper()) 
#Matnga biror metod qo'llashimiz uchun matn.metod() shaklda amalga oshiramiz.
#print(matn.metod()) shaklida metoddan foydalanganimizda faqatgina consoleda natija chiqishi o'zgaradi shu buyurilgan metodga. Masalan yuqoridagi misolimizda katta harfga o'zgardi consoledagi natija. Ammo ichkaridagi ma'lumot o'zgzarmaydi
#Ichkaridagi ma'lumotni ham shu foydalanilayotgan metodga o'zgartirmoqchi bo'lsak quyidagi usulda foydalanishimiz kerak bo'ladi.
#ism_sharif = ism_sharif.upper()
#print(ism_sharif.lower())
#ism_sharif = ism_sharif.lower()
#ism_sharif = ism_sharif.title() #Bu ichkaridagi ma'lumotga ta'sir beradi
#print(ism_sharif.title()) #Bu consoledagi natijaga ta'sir beradi
#ism_sharif = ism_sharif.capitalize() #Bu ichkari uchun
#print(ism_sharif.capitalize())


#meva = "     olma     "
#print(meva)
#print("Men " + meva.lstrip() + " yaxshi ko'raman")
#print("Men " + meva.rstrip() + " yaxshi ko'raman")
#print("Men " + meva.strip() + " yaxshi ko'raman")
#print("Men " + meva + " yaxshi ko'raman")


#INPUT funksiyasi haqida

ism = input("Ismingiz nima?") #Runni bosganimizda dastlab input funksiyasi bizdan ism yozishni talab qiladi. So'ngra ism kiritganimizdan keyin print buyrug'imiz bajarilib davomidan ismimiz ya'ni yozgan ma'lumotimiz chiqadi
print("Assalomu alaykum, " + ism)

ism = input("Ismingiz nima?\n>>>")
print("Assalomu alaykum, " + ism.title())