# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 13:55:26 2025

@author: abdur
"""

###01.Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
#oilam_azolari = ['ota', 'ona', 'katta opa', 'kichik opa', 'uka']
#for xabar in oilam_azolari:
 #   print(f"Assalomu alaykum {xabar} men sizni judayam so'ginganman In Shaa Allah yaqinda ko'rishamiz")
    
###02.Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
#print("Kod 5 marta takrorlandi") 


###03.10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
#toq_sonlar = list(range(11,100,2))
#for toq in toq_sonlar:
 #   print(f"{toq} ning kubi {toq**3} ga teng")
#print(toq_sonlar)


###04. Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
#kinolar = []
#print("5 ta eng sevimli kinolaringizni kiriting")
#for kino in range(1,6):
#    kinolar.append(input(f"{kino}-kinoingizni kiriting: "))
#print(kinolar)


###05. Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
#n_saram = int(input("Bugun kimlar bilan muloqotda bo'ldingiz?>>>"))
#bugungi_gumondorlar = []
#for n in range(n_saram):
#    bugungi_gumondorlar.append(input(f"{n+1}-odamni kiriting: "))
#print(bugungi_gumondorlar)


n_raqam = int(input("Bir nechta son ayting\n>>>"))
bu_sonlar = []
for n in range(n_raqam):
    bu_sonlar.append(input(f"{n+1}-sonni kiriting: "))
print(bu_sonlar)

    

