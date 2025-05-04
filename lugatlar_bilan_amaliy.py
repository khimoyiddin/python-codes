# -*- coding: utf-8 -*-
"""
Created on Sun May  4 15:03:23 2025

@author: abdur
"""
####01. Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.

# izohli_lugat = {
#     'integer':'butun son',
#     'float':"o'nli kasr",
#     'string':'matn',
#     'if':'agar',
#     'else':'aks holda',
#     'error':'xato',
#     'for':'uchun',
#     'dictionary':"lug'at",
#     'tuple':"o'zgarmas",
#     'print':'chop etish'
#     }
# for k,v in sorted(izohli_lugat.items()):
#     print(f"Kalit:{k}")
#     print(f"Qiymat:{v}")
    
###02. Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.    
davlatlar = {
    'uzbekistan':'tashkent',
    'south korea':'seoul',
    'kazakhstan':'astana',
    'russia':'moscow',
    'germany':'berlin',
    'italy':'rome',
    'australia':'sydney',
    'france':'paris'
    }
# print("Davlatlar nomlar: ")
# for kalit in sorted(davlatlar.keys()):
#     print(kalit.title())
# print("Poytaxtlari quyidagilar: ")
# for qiymat in sorted(davlatlar.values()):
#     print(qiymat.title())    
    
# davlat = input("Istalgan davlatni kiriting: ").lower()
# print(davlatlar.get(davlat, 'Bunday davlat mavjud emas').title())   
    
# if davlat in davlatlar:
#     print(f"Siz kiritgan davlat poytaxti {davlatlar[davlat].title()}")
# else:
#     print("Bizning lug'atda bunday davlat mavjud emas")

####03Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
# menu = {
#         'osh':30000,
#         'shashlik':8000,
#         'manti':3000,
#         'somsa':10000,
#         'norin':20000,
#         'qozon kabob':32000,
#         'qaynatma':22000,
#         "lag'mon":21000
#         }
# print('Uchta taomni kiriting!')
# buyurtma = []
# for n in range(3):
#     buyurtma.append(input(f"{n+1}-taomni kiriting: "))
    
# for taom in buyurtma:
#     if taom in menu:
#         print(f"{taom}ning narxi {menu[taom]}")
#     else:
#         print(f"Bizda {taom} yo'q")
    
# shaharlar = {
#     'tashkent':700,
#     'buxoro':760,
#     'samarqand':350,
#     'qarshi':200,
#     'nukus':1100,
#     'jizzax':600,
#     'termiz':100,
#     'dushanbe':400
#     }
# print('Ixtiyoriy ikkita shahargacha bo\'lgan masofani aytishim mumkin')
# shahar = []
# for n in range(2):
#     shahar.append(input(f"{n+1}-shaharni kiriting: "))
    
# for city in shahar:
#     if city in shaharlar:
#         print(f"{city}gacha bo'lgan masofa {shaharlar[city]} kilometr")
#     else:
#         print(f"Hozircha {city}gacha bo'lgan masofa haqida ma'lumotim yo'q")

#### (a**2)x+bx+c=0 ning barcha holatlari

a = float(input("Bririnchi koeffitsiyentning qiymatini kiriting: "))
b = float(input("Ikkinchi koeffitsiyentning qiymatini kiriting: "))
c = float(input("Ozod hadning qiymatini kiriting: "))
d = b**2-4*a*c
if d>0:
    print("Bu kvadrat tenglama 2 ta yechimga ega")
elif d<0:
    print("Bu kvadrat tenglama yechimga ega emas")
else:
    print("Bu kvadrat tenglama bitta yechimga ega")




