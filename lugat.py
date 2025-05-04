# -*- coding: utf-8 -*-
"""
Created on Sat May  3 12:35:47 2025

@author: abdur
"""
####Lug'at turidagi ma'lumotlar bilan ishlash
# car_0 = {'model': 'ferrari', 'rang': 'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

# eng_uz = {'car':'mashina', 'home':'uy', 'apple':'olma'}
# print(eng_uz)
# print(eng_uz['car'])

mevalar = {'olma': 20000, 'banan':'5000', 'qulupnay':'13000'}
# print(f"Qulupnay narxi {mevalar['qulupnay']} so'm")


# men_haqimda = {'ism':'Khimoyiddin', 'yosh':'24', 't_yil':'2001'}
# print(f"{men_haqimda['ism'].title()}, \
#       {men_haqimda['t_yil']}-yilda tug'ilgan, \
#        {men_haqimda['yosh']} yoshda")

# men_haqimda['kasbi'] = 'matematik'
# men_haqimda['qiziqishi'] = 'futbol'
# men_haqimda['kurs'] = 2
# men_haqimda['yosh'] = 25

#### bo'sh lug'atga elementlar qo'shish
# talaba = {}
# talaba['ism'] = 'abbos abduraxmonov'
# talaba['kurs'] = 4
# talaba['yosh'] = 24
# #print(talaba)
# print(f"Talaba {talaba['ism'].title()} {talaba['kurs']}-kursda o'qiydi")


#### Lug'atdan biror elementnio'chirib tashlash
# men_haqimda = {'ism':'Khimoyiddin', 'yosh':'24', 't_yil':'2001'}
# del men_haqimda['yosh']
# print(men_haqimda)


#### Lug'atlarni bir necha qatorda yozish mumkin
# sport_t = {
#     'abbos':'futbol',
#     'vohid':'volleyball',
#     'yusuf':'tennis',
#     'atham':'basketball'
#     }

# sport = sport_t['abbos']
# print(f"Abbosning yoqtirgan sport turi {sport}")

# ####Endi lug'atda ismi yo'q bo'lgan odamni kiritib ko'ramiz

# sport = sport_t['hasan']
# print(f"Hasanning sevimli sport turi {sport}")

# sport = sport_t.get('alisher','Bunday ism mavjud emas')
# print(sport)


# sport = sport_t.get('hasan')
# print(sport)



# ####01. otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
# otam = {'ism':'Sayfiddin', 't_yil':1973}
# onam = {'ism':'Oyzira', 't_yil':1976}
# print(f"Otamning ismlari {otam['ism']}, Tug'ilgan yili {otam['t_yil']}")
# print(f"Onamning ismlari {onam['ism']}, Tug'ilgan yili {onam['t_yil']}")

###Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
# taomlar = {
#     'otam':'osh',
#     'onam':'manti',
#     'opam1':'kabob',
#     'opam2':'xonim',
#     'ukam':'qozon kaobob'
#     }
# print(f"Otamning sevimli taomi {taomlar['otam']}")
# print(f"Onamning sevimli taomi {taomlar['onam']}")
# print(f"Katta opamning sevimli taomi {taomlar['opam1']}")



######Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.

izohli_lugat = {
    'integer':'butun son',
    'float':"o'nli kasr",
    'string':'matn',
    'if':'agar',
    'else':'aks holda',
    'error':'xato',
    'for':'uchun',
    'dictionary':"lug'at",
    'tuple':"o'zgarmas",
    'print':'chop etish'
    }
#print(izohli_lugat)
# word = input("Python keywordlaridan birortasini kiriting: ")
# if word in izohli_lugat:
#     print(f"Siz kiritgan so'z {izohli_lugat[word]} degan ma'noni anglatadi")
# else:
#     print("Lug'atda bunday so'z mavjud emas")


# word = input("Biror kalit so'z kiriting: ").lower()
# print(izohli_lugat.get(word, "Bunday so'z mavjud emas"))

# word = input("Kalit so'z kiriting: ").lower()
# tarjima = izohli_lugat.get(word)
# if tarjima == None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{word.title()} so'zi {tarjima} deb tarjima qilinadi")



















































