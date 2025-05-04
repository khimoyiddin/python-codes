# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 09:03:17 2025

@author: abdur
"""

#mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]#Mevalar ro'yxatini matn shaklida saqladik
#narxlar = [20000, 15000, 16200, 14600, 22000, 36120]#Narxlar ro'yxatini sonlar ko'rinishida saqladik va buni xohlagancha kengaytirishimiz va kamaytirishimiz mumkin
#sonlar = ['bir', 'ikki', 3, 4, 5]#Matnlar va sonlar aralash ro'yxat
#ismlar = []#bo'sh ro'yxat

#print("Birinchi meva: ", mevalar[0])# dasturlashda elementlarni sanash 0, 1, 2, ... shaklda bo'lganligi sababli birinv=chi elemntga 0-element sifatida murojaat etamiz 
#print("Ikkinchi meva: ", mevalar[1])

#print("Birinchi meva: ", mevalar[0].title())
#print('Ikkinchi meva: ', mevalar[2].upper())

#print(narxlar[1] + narxlar[2])
#print(narxlar[1], narxlar[2])

#car_models = ('Toyota', 'GM', 'BMW', 'MERS', 'KIA', 'HYUNDAI')
#print(car_models[-1])#bunda ro'yxat oxiridagi element konsolga chiqadi. Elementlarga murojaat qilishda eng oxorgi elentga -1 bilan bitta oldingiga esa -2 bilan va hokazo murojaat era olishimiz mumkin

## Elementni o'zgartirish

#narxlar = [20000, 15000, 16200, 14600, 22000, 36120]
#narxlar[0] = 16000 #1-qiymatni 16000 ga o'zgartiramiz
#narxlar[1] = 23000 #2-qiymatni 23000 ga o'zgartiramiz
#narxlar[4] = 35000 #5-qiymatni 35000 ga o'zgartiramiz
#narxlar[3] = narxlar[3] -  4600 # 4-qiymatin 4600 ga kamaytiramiz
#print(narxlar)


# .append()

#mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
#mevalar.append("banan") # bu .append() metodi yordamida ro'yxatga yangi mevani qo'shamiz va bu metod yordamida qo'shilgan element doimo ro'yxat oxiriga qo'shiladi.
#print(mevalar)


#cars = [] # cars deb nomlab bo'sh ro'yxat yaratamiz
#cars.append("nexia") #shu bo'sh ro'yxatimizga nexiani qo'shamiz
#cars.append('cobalt') # ro'yxatga cobaltni qo'shamiz
#cars.append("malibu") #ro'yxatga malibuni qo'shamiz
#cars.insert(1, "damas")
#print(cars)


# .insert() metodi yordamida ro'yxatimizning istalgan o'riniga qiymat kirita olamiz
#cars = ['nexia', 'cobalt', 'malibu']
#cars.insert(0, "damas")# bu yerda 1-o'ringa yangi qiymat qo'shamiz
#cars.insert(2, "equinox")# bunda 3-o'ringa yangi qiymat kiritamiz
#print(cars)

## delfunksiyasi yordamida ixtiyoriy o'rindagi elementni o'chirib tashlay olamiz
#mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
#del mevalar[1] # bu yordamida 2-element anjirni o'chirib tashlaymiz
#print(mevalar)


## .remove() metodi yordamida biz o'chirmoqchi bo'lgan elementimizni nomini kiritish orqali o'chira olamiz. Bu usul o'chirmoqchi bo'lgan elementimizning turgan o'rni nechinchi ekanligini bilmaganimizda asqotadi.
#mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
#mevalar.remove('shaftoli')
#print(mevalar)

#hayvonlar = ["qo'y", 'sigir', 'ot', 'mushuk', 'sigir']
#hayvonlar.remove('sigir') # Bunda .remove() metodi yordamida o'chirmoqchi bo'lgan elementlarimizsoni bir nechta bo'lsa, u eng oldingisini o'chiradi keyingi urunishda keyingisini va taqlidda davom etish orqali hammasini tartib bilan o'chirish mumkin
#print(hayvonlar)


## .pop() metodi. Ro'yxatni ichidan biron narsani sug'urib olish

#bozorlik = ['piyoz', 'guruch', 'tarvuz', 'un', 'kartoshka']
#mahsulot = bozorlik.pop(2)# Ro'yxatni ichidan 2-o'rinda turgan tarvuzni sug'urib olamiz
#print("Men " + mahsulot + " sotib oldim")
#print("Hali olinmagan mahsulotlar: ", bozorlik)
#mahsulot2 = bozorlik.pop()# .pop() metodidan foydalanganda qavs ichiha hech qanday indeks kiritmasak avtomatik ravishda eng oxirgi mahsulotni sug'urib olarkanmiz
#print(bozorlik)
#print(mahsulot2)

## .sort() biz berilgan ro'yxatdagi elementlarni alfabet bo'yicha tartiblashimiz ham mumkin shu metod yordamizda
#bozorlik = ['piyoz', 'guruch', 'tarvuz', 'un', 'kartoshka']
#bozorlik.sort()
#print(bozorlik)

## .sort(reverse=True) metodi orqali ro'yxatni alfabetga teskari taribga o'zgartirish mumkin
#bozorlik.sort(reverse=True)
#print(bozorlik)


#mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
#print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
#print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)
#print(sorted(mehmonlar, reverse=True))

#ages = [12, 98, 34, 65, 34, 76, 11]
#ages.sort()
#print(ages)
#print(sorted(ages, reverse=True))


#fruits = ['pear','banana','apple','watermelon','lemon']
#fruits.reverse()
#print(fruits)

## len() metodi ro'yxatdagi elementlar sonini aniqlash uchun foydalaniladi
#print("Elementlar soni: ", len(fruits))


##range() funksiyasi
#sonlar = list(range(0, 10)) ### DIQQAT! range funksiyasi ikkinchi indeksdan bitta avval to'xtaydi
#print(sonlar)

#rangefunksiyasi yordamida qadamni ham berishimiz mumkin
#juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
#toq_sonlar = list(range(1,20,2)) # 1 dan 20 gacha 2 qadam bilan
#print("Juft sonlar: ", juft_sonlar)
#print("Toq sonlar: ", toq_sonlar)

# Agar sonlar 0 dan boshlansa, range() funksiyasida yakuniy indeksni kiritish kifoya. Masalan range(0,10) deb emas range(10) kabi


#narxlar = [20000, 15000, 16200, 14600, 22000, 36120]
#arzon = min(narxlar)# min() funksiyasi yordamida eng kichik elementni aniqlashimiz mumkin
#qimmat = max(narxlar)# max() funksiyasi yordamida eng katta elementni aniqlashimiz mumkin
#jami = sum(narxlar)# sum() funksiyasi yordamida hamma sonlar(elementlar) yi'gindisini aniqlashimiz mumkin
#print("Eng arzoni: ", arzon, "\nEng qimmati: ", qimmat, "\nJami: ", jami)

### Ro'yxatni kesish
#mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
#my_mehmon = mehmonlar[0:3]# bu usulda ro'yxatning boshidan istalgancha elementni kesib olamiz
#print(my_mehmon)
#kelolmaydiganlar = mehmonlar[2:4]# Shu usul orqali ro'yxatning istalgan oralig'idagi elementlarni kesib olarkanmiz. Unutmaslik kerakki pythonda yozilgan o'rindan bitta oldinga kelib to'xtaydi. [2:5] shaklda bo'lsa 4-o'rindagi elementda to'xtaydi
#print(kelolmaydiganlar)
#keladi = mehmonlar[:4]
#aniqmas = mehmonlar[4:]
#print(keladi)
#print(aniqmas)



### Ro'yxatdan nusxa olish
sonlar = [1, 2, 3, 4, 5]# sonlar degan ro'yxat yaratamiz
sonlar2 = sonlar[:]# ro'yxatni to'liq ko'chirib oladi
sonlar2.append(6)
sonlar2.append(7)
print("Bu sonlar ro'yxati: ", sonlar)
print("Bu sonlar2 ro'yxati: ", sonlar2)
sonlar2.insert(5, 9)

print("Bu sonlar2 ro'yxati: ", sonlar2)


#Tuples. O'zgarmas qiymatlar
#Dastur yaratish davomida o'zgarmas ro'yxat tuzish talab qilinishi mumkin. Pythonda bunday ro'yxatlar tuples deb yuritiladi. Tuple ichidagi qiymatlarni bir marta, dastur boshida beriladi va so'ngra o'zgartirib bo'lmaydi. List dan farqli ravishda, Tuple e'lon qilishda kvadrat qavslar [] o'rniga oddiy qavslar () ishlatiladi:
#Tuple e'lon qilishda kvadrat qavslar [] o'rniga oddiy qavslar () ishlatiladi:

tomonlar = (22, 35, 16)
print(tomonlar)

#Tuple ichidagi elementlarga huddi ro'yxat elementlariga murojat qilingani kabi murojat qilinaveradi:
toys = ('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])


toys = ('bus', 'ayiqcha', 'mushukcha', 'qogirchoq', 'poyezd')
toys = list(toys)
toys.append('dino')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys)
print(toys)



