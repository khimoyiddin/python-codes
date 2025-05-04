# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 15:15:44 2025

@author: abdur
"""

### if, elif, else operatorlari. Bu operatorlar yordamida biz bir nechta kiritishimiz mumkin ekan. if/else yordamida esa faqatgina bitta shartga tekshira olar ekanmiz

# yosh = int(input("Yoshingiz nechada?\n>>>"))
# if yosh <= 4:
#     print("Sizga kirish bepul")# 4 yoshdan katta bo'lmasa bu body ishlaydi
# elif yosh <= 12:
#     print("Sizga kirish 5000 so'm") # 4 dan katta 12 dan katta bo'lmasa bu body ishlaydi
# elif yosh <= 18:
#     print("sizga kirish 8000 so'm")# 12 dan katta 18 katta bo'lmasa bu body ishlaydi
# else:
#     print("Sizga kirish 10000 so'm")# 18 dan bo'lsa bu body ishlar ekan
    
    
    
###Xuddi shu tepadagi kodni yana ham soddaroq yozishimiz ham mumkin ekan
#yosh = int(input("Yoshingiz nechada?\n>>>"))
# if yosh <= 4:
#         narx = 0# 4 yoshdan katta bo'lmasa bu body ishlaydi
# elif yosh <= 12:
#         narx = 5000 # 4 dan katta 12 dan katta bo'lmasa bu body ishlaydi
# elif yosh <= 18:
#         narx = 8000 # 12 dan katta 18 katta bo'lmasa bu body ishlaydi
# else:
#         narx = 10000# 18 dan bo'lsa bu body ishlar ekan
        
# print(f" Sizga kirish {narx} so'm")


#### or(yoki) operatori
# kun = input("Bugun haftaning qaysi kuni?\n>>>")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni ekanku")



#### and operatori
# kun = input("Bugun qanday kun?\n>>>")
# harorat = float(input("Necha gradus?\n>>> "))
# if kun.lower() == 'yakshanba' and harorat >= 30:
#     print("let's swim")
# elif kun.lower() == 'yakshanba' and harorat <30:
#     print("let's rest at home")
# else:
#     print("Bilganingni qil")

#### or hamda and operatorlaridan birgalikda foydalanmiz
# kun = input("Bugun qanday kun?\n>>>")
# harorat = float(input("Necha gradus?\n>>> "))
# if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat >= 30:
#     print("Let's swim")
# elif (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat < 30:
#     print("Let's relax at home")



#### BOOLEAN
# narx = 15000
# choy = True# True aniq bajariladi
# salat = False# False bajarilmaydi

# if choy and salat:  ##### If/elif opereatining kamchiligi shuki birorta shart bajarilsa boshqalarini tekshirib ham o'tirmaydi
#     narx = narx +10000
# elif choy or salat:
#     narx = narx + 5000
    
# print(f"Sizdan {narx} so'm bo'ldi")



### endi bir-biriga aloqasi bo'lmagan ya'ni biri najariladimi yo'qmi boshqalarini, hammasini tekshiraveradigan kod yozamiz
# narx = 15000
# choy = True### Shu yerda True ni o'rniga 1 ni False ni o'rniga esa 0 yozib qo'yishimiz ham mumkin ekan
# kampot = False
# salat = True
# shirinlik = False
# if choy:
#     print('Choy oldi')
#     narx = narx + 3000
    
# if kampot:
#     print("Kampot oldi")
#     narx = narx + 4000
    
# if salat:
#     print("Salat oldi")
#     narx = narx + 2000
    
# if shirinlik:
#     print("Shirinlik oldi")
#     narx = narx + 6000
    
# print(narx)

##### in operatori

# menu =['Qozon kabob', 'kabob', "somsa", 'osh', 'manti']
# 'achchiq gosht' in menu

# ovqat = input("Nima ovqat yeysiz?\n>>>")
# if ovqat.lower() in menu:
#     print("Buyurtmangiz qabul qilindi")
# else:
#     print("Afsuski bizda bunday ovqat yo'q")
        
    
    
###Xuddi kodni not in operatori bilan yozib ko'ramiz
# menu =['Qozon kabob', 'kabob', "somsa", 'osh', 'manti']
# ovqat = input("Nima ovqat yeysiz?\n>>>")
# if ovqat.lower() not in menu:
#     print("Asuski bizda bu ovqat yo'q")
# else:
#     print("Buyurtmangiz qabul qilindi")
    
    
# menu =['Qozon kabob', 'kabob', "somsa", 'osh', 'manti']
# my_orders = ['kabob', 'somsa', 'lavash', 'gamburg']

# for taom in my_orders:
#     if taom in menu:
#         print(f"Bu {taom} menuda bor")
#     else:
#         print(f"Kechirasiz, {taom} menuda yo'q")
    
    
    
# if my_orders:
#     print(f"Ro'yxatda {len(my_orders)} ta taom bor")
# else:
#     print("Ro'yxat bo'sh")    

    
### Endi masalan bizning my_orders degan ro'yxatimiz bo'sh bo'lishi ham mumkin
menu =['Qozon kabob', 'kabob', "somsa", 'osh', 'manti']
#my_orders= ['kabob', 'somsa', 'lavash', 'gamburg']
my_orders = []
if my_orders:# ro'yxatda biror element bo'lsa bu ifoda true qaytaradi
    for taom in my_orders:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Menuda {taom} yo'q")
            
else:#agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh")
    
    
####### not operatorini boshqa shartlarning oldidan ham qo'yishimiz mumkin. Misol uchun: if not a==5 ifodasi if a!=5 ifodasi bilan bir hil natija qaytaradi.
####### if not a>5 means a kichik yoki teng 5 ga bo'lsa















