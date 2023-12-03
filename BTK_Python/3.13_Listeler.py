#"BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz
carModels=["BMW", "Mercedes", "Opel", "Mazda"]

#Liste kaç elemanlıdır?
print(len(carModels))

#listenin ilk ve son elemanı nedir?
print(f"Listenin\n ilk elemani: {carModels[0]}\n son elemani: {carModels[-1]}")

#Mazda değerini Toyota ile değiştirin
carModels[3]="Toyota"
print(carModels)

#Mercedes listenin bir elemanı mıdır?
resuls= "Mercedes" in carModels
print(resuls)

#Listenin -2 indexindeki değer nedir?
print(carModels[-2])

#Lİstenin ilk 3 elemanını alın
print(carModels[0:3])

#Listenin son iki elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin
carModels[-2:]=["Toyota", "Renault"]
print(carModels)

#Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin
carModels+=["Audi", "Nissan"]
print(carModels)

#Listenin son elemanını silin
del carModels[-1]
print(carModels)

#Lİste elemanlarını tersten yazdırınız
print(carModels[::-1])

#Aşağıdaki verileri bir liste içerisinde saklayınız
#   StudentA: Yiğit Bilgi 2010, (70,60,70)
#   StudentB: Sena Turan 1999, (80,80,70)
#   StudentC: Ahmet Turan 1998, (80,70,90)   
StudentA=["Yiğit", "Bilgi", 2010, [70,60,70]] 
StudentB=["Sena", "Turan", 1999, [80,80,70]]
StudentC=["Ahmet", "Turan", 1998, [80,70,90]] 
list=[StudentA, StudentB, StudentC]
print(list)