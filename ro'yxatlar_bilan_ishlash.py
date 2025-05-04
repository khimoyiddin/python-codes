# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 20:59:11 2025

@author: abdur
"""

#cars = ['bmw', 'audi', 'malibu', 'cobalt', 'nexia', 'toyota', 'kia']
#cars.sort()
#print(cars)

### KATTA VA KICHIK HARF
#cars = ['Bmw', 'audi', 'malibu', 'cobalt', 'nexia', 'toyota', 'kia']
#cars.sort()
#print(cars)#katta va kichik harflar birgalikda kelganida tartiblashda katta harflar birinchi keladi. Shu sababdan sort() ni ishlatishdan oldin bir xil kichik harflarga o'zgartirib olish kerak


### Alifboga teskari tartibda taxlash
#cars.sort(reverse=True)#Alifboga teskari tartibda taxlash uchun sort() funksiyasi ichiga reverse=True argumentini kiritamiz
#print(cars)
#print(sorted(cars))# sorted() funksiyasi yordamida asl ro'yxatni o'zgartirmagan holatda konsolga ro'yxatin alifboga mos holatda chiqarishimiz mumkin
#print(sorted(cars, reverse=True))# reverse=True argumentini sorted() funksiyasi bilan ham ishlatishimiz mumkin


### sort() hamda sorted() funksiyalarini sonlardan iborat ro'yxatlarni tariblashda ham foydalanishimiz mumkin
#sonlar = [1, 34, 54, 32, 12, 64, 26, -14, -45, 3.1]
#sonlar.sort()
#sonlar.sort(reverse=True)
#print(sonlar)

#print(sorted(sonlar))
#print(sorted(sonlar, reverse=True))
#print(sonlar) 

###RO'YXATNI ORTIDAN BOSHLAB CHIQARISH(TESKARI AYLANTIRIB CHIQARISH)
#cars = ['bmw', 'audi', 'malibu', 'cobalt', 'nexia', 'toyota', 'kia']
#cars.reverse()
#print(cars) 

### RO'YXAT UZUNLIGINI ANIQLASH
#uzunlik =len(cars)
#print(len(cars))#len() funksiyasi yordamida ro'yxat uzunligini aniqlar ekanmiz
#print(len(sonlar))
#print(uzunlik)

### RANGE() FUNKSIYASI HAQIDA
#sonlar = list(range(0, 10))#rane(0, 10) funksiyasi 0, 1, 2, ..., 9 gacha sonlarni qaytaradi. list() funksiyasi esa uni ro'yxat sifatida shakllantiradi
#print(sonlar)# range() funksiyasida ikkinchida turgan indeksni hiosblamaydi undan bitta avval to'xtaydi
#toq_sonlar = list(range(1,20,2))
#juft_sonlar = list(range(0,20,2))
#uchga_karrali = list(range(3,64,3))
#print(toq_sonlar)
#print(juft_sonlar)
#print(uchga_karrali)

### MAX, MIN, SUM
#narxlar = [12221, 1245410, 214521, 120000, 213546]
#maks_qiymat = max(narxlar)
#min_qiymat = min(narxlar)
#jami = sum(narxlar)
#rint("Eng qimmati: ", maks_qiymat, "\nEng arzoni: ", min_qiymat, "\nJami: ", jami)


### RO'YXATNI MA'LUM QISMINI KESIB OLISH
#cars = ['bmw', 'audi', 'malibu', 'cobalt', 'nexia', 'toyota', 'kia']
#print(cars[3])#istalgan raqamli indeksni chiqarib olishimiz mumkin
#print(cars[0:4])# Istalgan tanlangan oraliqni chiqarib olishimiz mumkin. Bunda ikkinchi yozilgan indeks kirmaydi. Masalan: [0:3] = 0, 1, 2 ni chiqaradi
#rint(cars[2:5])#bu 2 dan boshlab 4-elementni ham hisoblaydi
#print(cars[:3])#birinchiga indeks qo'ymasak avtomatik 0-dan boshlab hisoblaydi
#print(cars[4:])#oxiriga indeks qo'ymasak eng oxirgi elementgacha(uni ham) hisoblaydi


#my_cars = cars[:]# bunda bosh va oxirgi indekslarni kiritmaymiz. Natijada cars degan ro'yxatning barcha elementlaridan nusxa olib my_cars degan ro'yxatga joylanadi
#my_cars.remove('audi')
#my_cars.append('Tico')
#my_cars.insert(4, 'Matiz')
#print(my_cars)
#print(cars)




### O'zgarmaslar ro'yxatlar yaratish
mevalar = ('olma', 'anor', 'anjir', 'gilos', 'banan', 'shaftoli')
#print(mevalar[2])
#print(mevalar[2:4])
#print(mevalar[:5])
#mevalar[4] = 'apelsin' #bunda biz mevalar ro'yxatining 4-elementini o'zgartirmoqchio bo'ldik, ammo error berdi. Chunki o'zgarmas ro'yxatni o'zgartirib bo'lmaydi.
#print(mevalar)# 
#Bunday holatda o'zgarmas ro'yxatni o'zgartirishimiz kerak bo'lsa, quyidagi ishlarni amalga oshiramiz. Avvalo list funksiyasi orqali uni ro'yxatga aylantirib olamiz
mevalar = list(mevalar)
mevalar.append('olcha')
mevalar.insert(4, 'ananas')
mevalar.remove('anjir')
mevalar = tuple(mevalar)
print(mevalar)




















