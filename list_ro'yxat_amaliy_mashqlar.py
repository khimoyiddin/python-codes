# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 16:48:55 2025

@author: abdur
"""
### 01
#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
#countries = ['Uzbekistan', 'South Korea', 'Saudi Arabia', 'Australia', 'Malaysia']
#print(countries)


### 02
# Ro'yxatning uzunligini konsolga chiqaring
#print("Bu ro'yxatning uzunligi: ", len(countries))


### 03
#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
#print("alifbo tartibida: ", sorted(countries))

### 04
#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
#print("alifboga teskari tartibda: ", sorted(countries, reverse=True))


###05
#Asl ro'yxatni qaytadan konsolga chiqaring
#print(countries)

### 06
#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
#countries.reverse()
#print(countries)


###07
#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
#print("Alifbo tartibida: ", sorted(countries))
#print("alifboga teskari tartibda: ", sorted(countries, reverse=True))


### 08
#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
#juftlar = list(range(120,1200,2))
#print(juftlar)
#quyidagi usulda ham yozish mumkin
#juftlar = range(120,1200,2)
#print(list(juftlar))

### 09
#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
#yigindi = sum(juftlar)
#print("Ro'yxatdagi sonlar yig'indisi: ", yigindi)


### 10
#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
#katta = max(juftlar)
#kichik = min(juftlar)
#print("Ro'yxatdagi eng katta va kichik sonlar ayirmasi: ", katta-kichik)

### 11
#Ro'yxatdagi elementlar sonini hisoblang
#print("Bu ro'yxatning uzunligi: ", len(juftlar))

### 12
#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
#boshi = juftlar[0:20]
#ortasi = juftlar[260:282]
#oxiri = juftlar[521:542]
#print("Boshidan 20 ta: ", boshi, "\nO'rtasidan 20 ta: ", ortasi, "\nOxiridan 20 ta: ", oxiri)

### 13
#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh', 'kabob', 'somsa', 'manti', "sho'rva"]

#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]
#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
#print(nonushta)
#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
nonushta.remove('kabob')
nonushta.remove('manti')
nonushta.append('sut')
nonushta.append("sariyog'")


#print(taomlar)
#print(nonushta)

nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non" #bu yerda nonushta ro'yxatini o'zgarmasga aylantirib keyin 1-o'rindagi elementini o'zgartirishga harakat qilib ko'rdik. Ammo o'zgarmas ro'yxatga o'zgartirish kiritib bo'lmaydi.

















