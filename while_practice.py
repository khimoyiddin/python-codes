# -*- coding: utf-8 -*-
"""
Created on Sat May 10 22:45:49 2025

@author: abdur
"""

###01. Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
# ism = input('Ismingiz nima? ')
# kitob = f"Salom, {ism.title()}. Yaxshi ko'rgan kitobingizni kiriting (dasturni to'xtatish uchun 'stop' deb yozing): "
# book = ''
# while book != 'stop':
#     book = input(kitob)
#     if book != 'stop':
#         print(f"Juda soz {book.title()} ajoyib kitob!")
# print("Dastur tugadi!")

# ism = input('Ismingiz nima? ')
# kitob = f"Salom, {ism.title()}. Yaxshi ko'rgan kitobingizni kiriting (dasturni to'xtatish uchun 'stop' deb yozing): "
# ishora = True
# while ishora:
#     book = input(kitob)
#     if book == 'stop':
#         ishora = False
#     else:
#         print(f"Juda soz {book.title()} ajoyib kitob!")
# print("dastur tugadi")

# ism = input('Ismingiz nima? ')
# kitob = f"Salom, {ism.title()}. Yaxshi ko'rgan kitobingizni kiriting (dasturni to'xtatish uchun 'stop' deb yozing): "

# while True:
#     book = input(kitob)
#     if book == 'stop':
#         break
#     else:
#         print(f"WOW, {book.title()} ajoyib kitob")
# print("Dastur tugadi!")


###02. Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
# savol = 'Assalomu alaykum! Yoshingiz nechada? '
# yosh = ''
# while True:
#     yosh = input(savol)
#     if yosh == 'exit' or yosh == 'quit':
#         break
    
#     yosh = int(yosh)
#     if yosh <= 7:
#         narx = 2000
#     elif yosh <= 18:
#         narx = 3000
#     elif yosh <= 65:
#         narx = 10000
#     elif yosh > 65:
#         narx = 0
    
#     if narx == 0:
#         print('Sizga kirish bepul')
#     else:
#         print(f"Sizga kirish {narx} so'm")
# print('Dastur tugadi')    


print("Kiritilgan sonning ildizini qaytaruvchi dastur.\n")
savol = "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    # qiymat = int(qiymat)
    if qiymat=='exit':
        break
    elif float(qiymat) < 0:
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")

