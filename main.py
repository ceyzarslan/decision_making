# Hangi yöne gideceğimize karar vereceğiz
a, b = 15, 15

# IF (Eğer): Belirtilen mantıksal ifade sağlanıyorsa / True döndürüyorsa bir kod bloğu işletilir.

if a < b:
    print(a, "sayisi", b, "sayisindan küçüktür")
    # 5 sayisi 7 sayisindan küçüktür

# IF...ELIF (Eğer değilse eğer): Belirtilen mantıksal ifadelerden ilk hangisi sağlanırsa onun kod bloğu işletiir.

if a < b:
    print(a, "sayisi", b, "sayisindan küçüktür")
elif a > b:  # eğer bir seçenek sunacaksak elif yapısını kullanırız
    print(a, "sayisi", b, "sayisindan büyüktür")
else:  # eğer tek bir seçenek sunup çıktı istiyorsak else yapısını kullanırız
    print(a, "sayisi", b, "sayisina esittir")

girilen = input("Bir kelime yazınız: ")
print("Yazılan: ", girilen)  # İNPUT İLE KONSOLDAN GİRİŞ YAPMAMIZI SAĞLAR

girilen=input("Bir bilgi giriniz: ") # klavyeden rastgele bir şey giriyor bu şekilde
