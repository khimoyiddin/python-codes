# -*- coding: utf-8 -*-
"""
Created on Sun May  4 11:56:07 2025

@author: abdur
"""
###.items() metodi. Bu metod lug'atning har bir elementini oladi.

# talaba_0 = {
#     'ism':'Sunnatillo',
#     'familiya':'Hayitov',
#     'yosh':'22',
#     'fakulteti':'Matematika',
#     'kurs':4
#     }
# #print(talaba_0)
# #print(talaba_0.items())

# for kalit,qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")


####Yana bir misol
# telefonlar = {
#     'abbos':'redmi 9',
#     'vohid':'samsung',
#     'yusuf':'iphone 14',
#     'islom':'samsung s10',
#     'wonje':'ziffler'
#     }
# # for i,t in telefonlar.items():## Bu yerda i va t o'zgaruvchilar ketma ket kiritildi.
# #Ular telefonlar lug'atidagi kalit va qiymatlarni ketma-ket qabul qiladi. Mn: i abbosga teng. t uning teli redmi 9 ga teng qiymatni shu tarzda qolganlarini ham oladi
# #     print(f"{i.title()} ning telefoni {t}")
# print(f"Abbosning telefoni {telefonlar['abbos']}")  


##### .keys() metodi haqida. keys-kalitlar

telefonlar = {
    'abbos':'redmi 9',
    'vohid':'samsung',
    'yusuf':'iphone 14',
    'islom':'samsung s10',
    'wonje':'ziffler'
    }
# for ism in telefonlar.keys():
#     print(ism.title())

####.keys() metodidan foydalanayotganda .keys() yozmasdan bajarsak lug'atning keylari konsolga chiqaverar ekan

# for ism in telefonlar:
#     print(ism.title())


# mahsulotlar = {
#     'olma':15000,
#     'anor':20000,
#     'makaron':5000,
#     'banan':18000,
#     'guruch':14000,
#     }


# bozorlik = ['un', 'olma', 'banan', 'sabzi', 'guruch']
# # for mahsulot in mahsulotlar:
# #     if mahsulot in bozorlik:
# #         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

# ###Bu ikkala kodimiz ham bir xil natija berarkan

# for mahsulot in bozorlik:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]}")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Itlimos, keyingi safar {buyum} ham olib keling")
        
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# ######.values() metodidan foydalanib biz faqat lug'atlarning qiymatlarini chiqarishimiz mumkin.
# print(mahsulotlar.values())     

# print("Mening do'stlarim quyidagi markadagi telefonlardan foydalanishadi")
# for tel in telefonlar.values():
#     print(tel)     
        
    
        
#### set() funksiyasi. bu funksiya yordamida biz lug'atda bir necha bor takrorlangan qiymatlarni ekranga chiqaroyatganda hammasi emas ichidan bir necha bor takrorolanganlaridan ham bir marta chiqarish foydalanar ekanmiz
    
telefonlar = {
    'abbos':'redmi 9',
    'vohid':'samsung',
    'yusuf':'iphone 14',
    'islom':'samsung s10',
    'wonje':'ziffler',
    'eshboy':'samsung s10',
    'jahon':'redmi 9',
    'baxtiyor':'ziffler'
    }
### shu yerda qiymatlarni chiqarayotganimizda ko'pchilik insonlar bir teldan foydalanishar ekan. Faqat bittasini chiqaramiz
# for tel in telefonlar.values():
#     print(tel)    
    
# for tel in set(sorted(telefonlar.values())):
#     print(tel)
    
##### sets degan yana bir ma'lumotlar turi ham bor ekan. 
fanlar = {'algebra', "geometriya", 'ona tili', 'adabiyot', 'algebra', "adabiyot"}
print(fanlar)    
 ## bu ma'lumot turini konsolga chiqarganimizda takrorlangan elementlardan faqat bittasini chiqarar ekan   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        











