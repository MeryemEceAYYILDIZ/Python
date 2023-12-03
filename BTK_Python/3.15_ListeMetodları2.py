names=["Ali", "Yagmur", "Hakan", "Deniz"]
years=[1998, 2000, 1998, 1987]

#Cenk ismini listenin sonuna ekleyiniz
names.append("Cenk")
print(names)

#Sena değerini listenin başına ekleyiniz
names.insert(0,"Sena")
print(names)

#Deniz ismini listeden siliniz
names.remove("Deniz")
print(names)

#Ali listenin bir elemanı mıdır?
result= "Ali" in names
print(result)

#Lİste elemanlarını ters çeviriniz
names.reverse()
print(names)

#Liste elemanlarını alfabetik olarak sıralayınız
names.sort()
print(names)

#years listesini rakamsal büyüklüğe göre sıralayınız 
years.sort()
print(years)

#str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz
str="Chevrolet, Dacia"
str=str.split(",")
print(str)

#year listesinin en büyük ve en küçük elemanı nedir*
print(f"Lİstenin;\n En kucuk elemani= {min(years)}\n En buyuk elemani= {max(years)}")

#years listesinin bütün elemanlarını siliniz
years.clear()
print(years)

#Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız
markalar= []
marka= input("Bir marka giriniz: \n")
markalar.append(marka)
marka= input("Bir marka giriniz: \n")
markalar.append(marka)
marka= input("Bir marka giriniz: \n")
markalar.append(marka)
print(markalar)
