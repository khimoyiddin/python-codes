# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 17:54:05 2025

@author: abdur
"""

####01. Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

# son = int(input("Juft son kiriting: "))
# if son % 2 == 0:
#     print("Rahmat")
# else:
#     print("Bu juft son emas")

####02. Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:

# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

# yosh = int(input("Yoshingizni kiriting\n>>>"))

# if yosh < 4 or yosh > 60:
#     narx = 0
# elif yosh < 18:
#     narx = 10000
# else:
#     narx = 20000
    
# print(f"Sizga kirish {narx} so'm")

####03. Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))
# if a > b:
#     print("a > b")
# elif a == b:
#     print('a = b')
# else:
#     print("a < b")

####04. mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar = ['tuz', 'shakar', 'yog\'', 'non', 'suv', 'bodom', 'magiz', 'olma', 'anor', 'makaron']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}- mahsulotni qo'shing: "))
    
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot} do'konimizda bor")
#     else:
#         print(f"{mahsulot} do'konimizda yo'q")
        

        

####05. Biror O'quv markazning fanlar degan ro'yxatini yaratamiz. Ixtiyoriy o'quvchi kelib 3 fan tanlaganda unga bizda fan o'qitiladi yoki afsuski hozircha bu fan o'qitilmaydi degan yozuv chiqaramiz.
# fanlar = ['matematika', 'fizika', 'kimyo', 'biologiya', 'ingliz tili', 'rus tili', 'nemis tili', 'koreys tili', 'tarix', 'ona tili']
# savat = []

# for k in range(1,4):
#     savat.append(input(f"{k}-fanni kiriting: "))

# for fan in savat:
#     if fan in fanlar:
#         print(f"Tabriklaymiz bizda {fan} ustozlari mavjud")
#     else:
#         print(f"Afsuski hozirda bizda {fan} o'qituvchilari mavjud emas")



####06. Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

# mahsulotlar = ['tuz', 'shakar', 'yog\'', 'non', 'suv', 'bodom', 'magiz', 'olma', 'anor', 'makaron']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# for n in range(1,6):
#     savat.append(input(f"{n}-mahsulotni kiriting: "))
    
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append({mahsulot})
#     else:
#         mavjud_emas.append({mahsulot})
        
# print(f"Bor mahsulotlar: {bor_mahsulotlar}")
# print(f"Yo'q mahsulotlar: {mavjud_emas}")        
#######Shu yerdan pastini ustoznikidek qilib o'zgartiramiz mukammal kod hosil bo'ladi
# if len(mavjud_emas) == 0:
#     print("Siz so'ragan barcha mahsulot do'konimizda bor")
# else:
#     print(f"Quyidagi mahsulotlar do'konimizda bor {bor_mahsulotlar}")
# #####O'zgartma
# if mavjud_emas:
#     print(f"Do'konimizda quyidagi mahsulotlar yo'q")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
##### Ustozni kodi     
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")


#####07. foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

# foydalanuvchilar = ['tuzoq', 'killer', 'king', 'math', 'force']
# login = input("Iltimos yangi login kiriting\n>>>")
# if login.lower() in foydalanuvchilar:
#         print("Login band. Iltimos yangi login tanlang")
# else:
#         print("Xush kelibsiz, foydalanuvchi")


#####08Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

# butun_son = int(input("Biror butun son kiriting\n>>>"))
# if butun_son % 2 == 0:
#     print("2")
# if butun_son % 3 == 0:
#     print("3")
# if butun_son % 4 == 0:
#     print("4")
# if butun_son % 5 == 0:
#     print("5")
# if butun_son % 6 == 0:
#     print("6")
# if butun_son % 7 == 0:
#     print("7")
# if butun_son % 8 == 0:
#     print("8")
# if butun_son % 9 == 0:
#     print("9")
# if butun_son % 10 == 0:
#     print("10")


son = int(input("Istalgan butun son kiriting"))
for n in range(2,11):
    if son%n == 0:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")




