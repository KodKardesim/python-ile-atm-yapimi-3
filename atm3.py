from os import system


class Musteri:
    def __init__(self, ID, PAROLA, ISIM):
        self.id = ID
        self.parola = PAROLA
        self.isim = ISIM
        self.bakiye = 0


class Banka:
    def __init__(self):
        self.musteriler = list()

    def MusteriOl(self, ID, PAROLA, ISIM):
        self.musteriler.append(Musteri(ID, PAROLA, ISIM))


banka = Banka()
uyeislem = """
[1] Bakiye sor
[2] Para yatır
[3] Para gönder
[4] Para çek
[Q] Çıkış yap"""
while True:
    system("cls")
    idler = [i.id for i in banka.musteriler]
    print("""[1] Banka Müşterisiyim
[2] Banka Müşterisi olmak istiyorum""")
    secim = input("Seçiminiz : ")
    if secim == "1":
        gelenid = input("ID GİRİNİZ : ")
        gelenparola = input("Parola giriniz: ")

        if gelenid in idler:
            for musteri in banka.musteriler:
                if gelenid == musteri.id:  # musteri bulundu
                    if gelenparola == musteri.parola:
                        print("Giriş Başarılı.")
                        while True:
                            system("cls")
                            print("Hoşgeldiniz {}".format(musteri.isim))
                            print(uyeislem)
                            islem = input("İşlem seçiniz : ")
                            if islem == "1":
                                print(f"Mevcut bakiyeniz : {musteri.bakiye} TL")
                                input("Ana menüye ddönmek için 'enter'a basınız.")
                            elif islem == "2":
                                try:
                                    miktar = int(input("Yatırmak istediğiniz miktar : "))
                                    onay = input(f"Hesabınıza {miktar} TL yatırma işlemini onaylıyor musunuz. [E/e]")
                                    if onay == "E" or onay == "e":
                                        musteri.bakiye += miktar
                                        print(f"Hesabınıza {miktar} TL yatırıldı.")
                                        input("Ana menüye dönmek için 'enter'a basınız.")
                                    else:
                                        print("İşlem iptal edildi.")
                                        input("Ana menüye dönmek için 'enter'a basınız.")
                                except:
                                    print("Lütfen 'rakam' kullanarak miktar girin.")
                                    input("Ana menüye dönmek için 'enter'a basınız.")
                            elif islem == "3":
                                arananID = input("Müşteri ID : ")
                                if arananID in idler:
                                    for digermusteri in banka.musteriler:
                                        if arananID == digermusteri.id:
                                            print(f"Para gönderme işlemi : {digermusteri.isim} ")
                                            try:
                                                miktar = int(input("Göndermek istediğiniz miktar :"))
                                                if miktar <= musteri.bakiye:
                                                    onay = input(
                                                        f"{digermusteri.isim} adlı kişinin hesabına {miktar} TL yatırma işlemini onaylıyor musunuz. [E/e]")
                                                    if onay == "E" or onay == "e":
                                                        digermusteri.bakiye += miktar
                                                        musteri.bakiye -= miktar
                                                        print(f"{digermusteri.isim}'a {miktar} TL yatırıldı.")
                                                        input("Ana menüye dönmek için 'enter'a basınız.")
                                                    else:
                                                        print("İşlem iptal edildi.")
                                                        input("Ana menüye dönmek için 'enter'a basınız.")
                                                else:
                                                    print("Yetersiz bakiye")
                                                    input("Ana menüye dönmek için 'enter'a basınız.")
                                            except:
                                                print("Lütfen 'rakam' kullanarak miktar girin.")
                                                input("Ana menüye dönmek için 'enter'a basınız.")
                                else:
                                    print("Müşteri bulunamadı.")
                                    input("Ana menüye dönmek için 'enter'a basınız.")
                            elif islem == "4":
                                print("Para Çekme İşlemi")
                                try:
                                    miktar = int(input("Çekmek istediğiniz miktar : "))
                                    if miktar <= musteri.bakiye:
                                        onay = input(
                                            f"Hesabınızdan {miktar} TL çekme işlemini onaylıyor musunuz. [E/e]")
                                        if onay == "E" or onay == "e":
                                            musteri.bakiye -= miktar
                                            print(f"Hesabınızdan {miktar} TL çekildi.")
                                            input("Ana menüye dönmek için 'enter'a basınız.")
                                        else:
                                            print("İşlem iptal edildi.")
                                            input("Ana menüye dönmek için 'enter'a basınız.")

                                    else:
                                        print("Yetersiz bakiye")
                                        input("Ana menüye dönmek için 'enter'a basınız.")
                                except:
                                    print("Lütfen 'rakam' kullanarak miktar girin.")
                                    input("Ana menüye dönmek için 'enter'a basınız.")

                            elif islem == "Q" or islem == "q":
                                print("Çıkış yapıldı")
                                break
                    else:
                        print("ID veya Parola hatalı.")
                        input("Ana menüye dönmek için 'enter'a basınız.")
                        break
        else:
            print("ID veya Parola hatalı.")
            input("Ana menüye dönmek için 'enter'a basınız.")

    if secim == "2":
        print("Kayıt Formu")
        id = input("ID belirleyiniz: ")
        if id in idler:
            print("Bu ID alınmış :( Lütfen başka bir ID dene.")
            input("Ana menüye dönmek için 'enter'a basınız.")
        else:
            parola = input("Parola belirleyiniz :")
            isim = input("İsminiz : ")
            banka.MusteriOl(id, parola, isim)
            print("Bankamıza üye olduğunuz için teşekkür ederiz.")
            input("Ana menüye dönmek için 'enter'a basınız.")
