#import numpy as np 

#BOYUTLAR
#birboyut = np.array([1,2,3]) = bir boyutlu dizi []
#print(birboyut)
#ikiboyut = np.array([[1,2,3],[4,5,6]]) = iki boyutlu dizi [[]]
#print(ikiboyut)
#ucboyut = np.array([[[1,2,3],[4,5,6],[7,8,9]]]) = üc boyutlu dizi  [[[]]]
#print(ucboyut)

#SIFIRLAR

#sifir=np.zeros(5) = default(float64) biciminde 5 tane sıfır olustur
#print(sifir)
#sifir2=np.zeros((4,3)) = default(float64) biciminde 4 satırlı 3 sütunlu 0 olustur
#print(sifir2)

#BİRLER

#bir=np.ones((5),dtype=int) = int veri biciminde 5 tane 1 olustur
#print(bir)
#bir2=np.ones((4,3),dtype=int) = int veri biciminde 4 satırlı 3 sütunlu 1 olustur
#print(bir2)
#bir3=np.ones((4,3)) = default(float64) biciminde 4 satırlı 3 sütunlu 1 olustur
#print(bir3)
#bir4=np.ones(5) = default(float64) biciminde 4 satırlı 3 sütunlu 1 olustur
#print(bir4)

#DEĞİŞİK RANDOM KOMUTLARI

#full=np.full((4,3),10) = 4 satırlı 3 sütunlu 10 sayısı olustur
#print(full)
#ser2=np.arange(1,30,2) = 1 den baslayıp 30  a kadar 2 ser arttırarak ilerle
#print(ser2)
#randoomm=np.random.randint(0,10,5) = 0 10 arası 5 tane sayı olustur
#print(randoomm)
#random2=np.random.randint(0,10,(4,3)) =  0 10 arası 4 satırlı 3 sütunlu sayı olustur
#print(random2)

#DİZİ KOMUTLARI

#a=np.array([[1,2,3],[4,5,6]])  = 2 boyutlu dizi
#print(a.shape) = a dizisinin satırını ve sütununu (2,3) şeklinde verir

#b=np.array([1,2,3,4,5]) = 1 boyutlu dizi
#print(b.ndim) = dizinin satır sayısını verir

#c=np.array([[1,2,3],[4,5,6]]) = 2 boyutlu dizi 
#print(c.ndim) = dizinin satır sayısını verir

#d=np.array([1.1,2.2,3.3]) = 1 boyutlu float64 dizi

#print(c.size) = dizi elemanlarını söyler
#print(b.dtype) = dizinin veri türünü söyler
#print(a.itemsize) = dizinin byte değerini söyler
#print(d.dtype) = dizinin veri türünü söyler