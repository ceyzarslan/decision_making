tckn_girilen = input("Kimlik numaranızı giriniz : ")
if tckn_girilen.isnumeric():  # numeric olup olmadığını kontrol et
    tckn_int = int(tckn_girilen)
    print(tckn_int, type(tckn_int))
if len(str(
        tckn_int)) == 11:  # dönüştürülen kimlik numarasının kaç basamaktan oluştuğunu öğrenmek için tekrar string ifadeye dönüştürdük
    if tckn_int != 11111111110:
        ilk9 = tckn_int // 100 # 123456789 İLK 9'U BULMA
        son2 = tckn_int % 100
        tekler, ciftler = 0, 0

        b9 = ilk9 % 10
        tekler += b9
        ilk9 //= 10



    else:
        print("Girdiğiniz geçersiz")
else:
    print("Kimlik 11 no'dan oluşmalıdır")
