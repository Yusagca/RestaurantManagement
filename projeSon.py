from collections import deque


class calisan:
    calisan_listesi = deque()
    menu_list = deque()
    hasilat = 0

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.calisan_listesi.append(self)
        yonetici.ise_al(self.calisan_listesi)


class servis():
    servisPassword = "password123"
    @staticmethod
    def masayı_topla():
        print("Masa Toplanıp Temizlendi")

    @staticmethod
    def servis_ac():
        print("Masaya Servis Açıldı")


class asci(calisan):
    __maas = 10000

    def yemek_ekle(self, yemek):
        self.menu_list.append(yemek)
        dosya = open("menu.txt", "w", encoding="utf-8")
        for i in range(len(self.menu_list)):
            dosya.write(
                "---------------\n" + self.menu_list[i].isim + "\n\n" + self.menu_list[i].acıklama + "\n\n" + str(
                    self.menu_list[i].fiyat) + " TL\n---------------\n")
        dosya.close()

    def getMaas(self):
        print(self.__maas)

    def setMaas(self, yeni_maas):
        self.__maas = yeni_maas


class garson(servis, calisan):
    __maas = 5500
    musteriler = deque()
    orders = deque()

    def getMaas(self):
        print(self.__maas)

    def setMaas(self, yeni_maas):
        self.__maas = yeni_maas

    def siparis_olustur(self, siparis, musteri):
        self.musteriler.append(musteri)
        self.orders.append(siparis)
        musteri.fatura += siparis.fiyat
        dosya = open("siparisler.txt", "w", encoding="utf-8")
        for i in range(len(self.musteriler)):
            dosya.write("------------------------------\n" + self.musteriler[i].isim + " " + self.musteriler[
                i].soyisim + "\n\n" + self.orders[i].isim + " istedi " + str(
                self.orders[i].fiyat) + " TL\n------------------------------\n")
        dosya.close()
        print("Yemek Servis edildi\n")


class kasiyer(calisan):
    __maas = 5200

    def fatura_ode(customer):
        calisan.hasilat += customer.fatura
        print("Ödenecek Tutar:",customer.fatura)
        customer.fatura = 0
        print("\nÜcret Ödendi\nTeşekkür Ederiz!\n")

    def getMaas(self):
        print(self.__maas)

    def setMaas(self, yeni_maas):
        self.__maas = yeni_maas


class komi(servis, calisan):
    def getMaas(self):
        print(self.__maas)

    def setMaas(self, yeni_maas):
        self.__maas = yeni_maas

    __maas = 4500


class yonetici(calisan):
    __maas = 15000
    adminPassword = "myPassword123"

    def menuye_icecek_ekle(self, icecek):
        self.menu_list.append(icecek)
        dosya = open("menu.txt", "w", encoding="utf-8")
        for i in range(len(self.menu_list)):
            dosya.write(
                "---------------\n" + self.menu_list[i].isim + "\n\n" + self.menu_list[i].acıklama + "\n\n" + str(
                    self.menu_list[i].fiyat) + " TL\n---------------\n")
        dosya.close()

    def ise_al(liste):
        dosya = open("calisanlar.txt", "w", encoding="utf-8")
        for i in range(len(liste)):
            dosya.write("Ad Soyad Yas: " + liste[i].name + " " + liste[i].surname + " " + str(liste[i].age) + "\n")
        dosya.close()

    def setAsciMaas(self, asci, yeni_maas):
        return asci.setMaas(yeni_maas)

    def setKomiMaas(self, komi, yeni_maas):
        return komi.setMaas(yeni_maas)

    def setYoneticiMaas(self, yonetici, yeni_maas):
        return yonetici.setMaas(yeni_maas)

    def setGarsonMaas(self, garson, yeni_maas):
        return garson.setMaas(yeni_maas)

    def setkasiyerMaas(self, kasiyer, yeni_maas):
        return kasiyer.setMaas(yeni_maas)

    def getMaas(self):
        print(self.__maas)

    def setMaas(self, yeni_maas):
        self.__maas = yeni_maas


class musteri:
    musteriler = deque()

    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim
        self.fatura = 0
        self.musteriler.append(self)

    def menu_goster(self):
        dosya = open("menu.txt", "r", encoding="utf-8")
        print(dosya.read())
        dosya.close()

    def fatura_ode(self):
        return kasiyer.fatura_ode(self)


class product:
    def __init__(self, isim, acıklama, fiyat):
        self.isim = isim
        self.acıklama = acıklama
        self.fiyat = fiyat

    def fiyat_duzenle(self, yeni_fiyat):
        self.fiyat = yeni_fiyat


class yemek(product):
    def __init__(self, isim, acıklama, fiyat, gramaj):
        product.__init__(self, isim, acıklama, fiyat)
        self.gramaj = gramaj


class icecekler(product):
    def __init__(self, isim, acıklama, fiyat, icecek_boyu):
        product.__init__(self, isim, acıklama, fiyat)
        self.icecek_boyu = icecek_boyu


class gazli_icecekler(icecekler):
    def __init__(self, isim, acıklama, fiyat, icecek_boyu):
        icecekler.__init__(self, isim, acıklama, fiyat, icecek_boyu)
        self.acıklama = self.acıklama + " Gazli İcecek"


class meyve_suyu(icecekler):
    def __init__(self, isim, neyli, fiyat, icecek_boyu):
        icecekler.__init__(self, isim, neyli, fiyat, icecek_boyu)
        self.acıklama = self.neyli + " Meyve Suyu"


boolean = True
custommer = False


while boolean == True:
    print("-------------------------------------------")
    print("PROJE SAHİPLERİ:")
    print("HALİL YUŞA AĞCA|-|02210201061")
    print("EREN CAN ÇELİK|-|02210201055")
    print("--------------------------------------------")
    print("Merhaba! Hoşgeldiniz. Lütfen erişmek istediğiniz menüyü seçiniz.")
    print("|1| Yönetici İşlemleri")
    print("|2| Sipariş İşlemleri")
    print("|0| Çıkış")
    print()
    value = input("Seçim:")


    # YÖNETİCİ MENÜSÜ
    if value == "1":
        password = input("Lütfen yönetici şifrenizi giriniz:")
        if password==yonetici.adminPassword:
            yoneticibool = True
            while yoneticibool==True:
                print("Yönetici menüsüne hoşgeldiniz. Lütfen yapmak istediğiniz işlemi seçin.")
                print()
                print("|1| Çalışan Ekleme")
                print("|2| Yemek Ekleme")
                print("|3| İçecek Ekleme")
                print("|4| Maaş İşlemleri")
                print("|0| Çıkış")
                print()
                value1 = int(input("Seçim:"))
                if value1==1:
                    if value1 == 1:
                        print("Eklemek istediğiniz elemanın türünü giriniz:")
                        print("|1| Yönetici")
                        print("|2| Aşçı")
                        print("|3| Garson")
                        print("|4| Komi")
                        print("|5| Kasiyer")
                        print("|0| Çıkış")
                        print()
                        value2 = int(input("Seçim="))
                        print("-------------------------")
                        if value2 == 1:
                            yonetici(input("Ad:"), input("Soyad:"), input("Yaş:"))
                            yonetici.ise_al(calisan.calisan_listesi)
                            print("Yönetici Eklendi.")

                        elif value2 == 2:
                            asci(input("Ad:"), input("Soyad:"), input("Yaş:"))
                            yonetici.ise_al(calisan.calisan_listesi)
                            print("Aşçı Eklendi.")
                        elif value2 == 3:
                            garson(input("Ad:"), input("Soyad:"), input("Yaş:"))
                            yonetici.ise_al(calisan.calisan_listesi)
                            print("Garson Eklendi.")
                        elif value2 == 4:
                            komi(input("Ad:"), input("Soyad:"), input("Yaş:"))
                            yonetici.ise_al(calisan.calisan_listesi)
                            print("Komi Eklendi.")
                        elif value2 == 5:
                            kasiyer(input("Ad:"), input("Soyad:"), input("Yaş:"))
                            yonetici.ise_al(calisan.calisan_listesi)
                            print("Kasiyer Eklendi.")
                        elif value2==0:
                            print("Çıkılıyor...")
                            yoneticibool = False
                        else:
                            print("Geçerli bir değer girmediniz!")
                elif value1==2:
                    ism = input("Yemek ismi:")
                    acikla = input("Malzemeler(Lütfen malzemelerin arasına virgül(,) koyunuz.):")
                    acikla = acikla.replace(",", "\n")
                    asci.yemek_ekle(asci, yemek(ism, acikla, float(input("Fiyat:")), input("Gramaj:")))
                elif value1==3:
                    print("İçecek Türünü Seçiniz:")
                    print("|1| Gazlı icecek")
                    print("|2| Meyve suyu")
                    print()
                    value2 = int(input("Seçim="))
                    print("-------------------------")
                    if value2 == 1:
                        yonetici.menuye_icecek_ekle(yonetici, gazli_icecekler(input("isim:"), input("Tür:"),float(input("fiyat:")),input("içecek boyu:")))
                    elif value2 == 2:
                        yonetici.menuye_icecek_ekle(yonetici,meyve_suyu(input("isim:"), input("Tür:"), float(input("fiyat:")),input("içecek boyu:")))
                    else:
                        print("Geçerli bir değer girmediniz!")
                elif value1==4:
                    print("İşleminizi Seçiniz.")
                    print("|1| Maaş göster")
                    print("|2| Maaş düzenle")
                    print()
                    value2 = int(input("Seçim="))
                    print("-------------------------")
                    if value2 == 1:
                        print("Maaşını görüntülemek istediğiniz çalışanı seçin.")
                        for i in range(len(calisan.calisan_listesi)):
                            print(i+1 , calisan.calisan_listesi[i].name, calisan.calisan_listesi[i].surname,
                                  calisan.calisan_listesi[i].age)
                        value3 = int(input("Seçim:"))
                        if 0 <= value3 < len(calisan.calisan_listesi):
                            print("Seçilen Çalışanın Maaşı:")
                            calisan.calisan_listesi[value3].getMaas()

                    elif value2 == 2:
                        print("Maaşını düzenlemek istediğiniz çalışanı seçin.")
                        for i in range(len(calisan.calisan_listesi)):
                            print(i + 1, calisan.calisan_listesi[i].name, calisan.calisan_listesi[i].surname,
                                  calisan.calisan_listesi[i].age)
                        value3 = int(input("Seçim="))
                        if 0 <= value3 < len(calisan.calisan_listesi):
                            calisan.calisan_listesi[value3].setMaas = float(input("Atamak İstediğiniz Maaş:"))

                    else:
                        print("Geçerli bir değer girmediniz!")
                elif value1==0:
                    yoneticibool=False

        else:
            print("Şifreniz Yanlış.Başlangıç menüsüne yönlendiriliyorsunuz...")


    #SİPARİŞ MENÜSÜ
    if value=="2":
        print("Merhaba! Sipariş menüsüne hoşgeldiniz.Lütfen Yapmak istediğiniz işlemi seçiniz.")
        print("|1| Müşteri Oluştur")
        print("|2| Menü Göster")
        if custommer==True:
            print("|3| Sipariş Oluştur")
            print("|4| Fatura ödeme")
        else:
            print("Sipariş Oluşturma veya Fatura Ödeme işlemi için Müşteri ekleyin!")
        deger = int(input("Seçim:"))
        if deger==1:
            sifre = input("Servis Görevlisi Şifrenizi giriniz:")
            if sifre==servis.servisPassword:
                print("Müşteri Bilgilerini Giriniz.")
                musteri(input("Ad:"), input("Soyad:"))
                custommer = True
                print("Müşteri Oluşturuldu.")
            else:
                print("Şifreniz yanlış. Bu işlem için yetkiniz yok")
        elif deger==2:
            musteri.menu_goster(musteri)
        elif deger==3 and custommer==True:
            print("Siparişi Verecek Müşteriyi Seçin")
            for i in range(len(musteri.musteriler)):
                print(i + 1, "-", musteri.musteriler[i].isim, musteri.musteriler[i].soyisim)
            print()
            value2 = int(input("Seçim=")) - 1
            print("Sipariş Vermek İstediğiniz Yemeği Seçin.")
            for i in range(len(calisan.menu_list)):
                print(i + 1, "-", calisan.menu_list[i].isim)
            print()
            value3 = int(input("Seçim:")) - 1
            print()
            if 0 <= value2 < len(musteri.musteriler) and 0 <= value3 < len(calisan.menu_list):
                garson.siparis_olustur(garson, calisan.menu_list[value3], musteri.musteriler[value2])
            else:
                print("Geçerli bir değer girmediniz!")
        elif deger==4 and custommer==True:
            print("Hesabı ödenecek müşteriyi seçin.")
            for i in range(len(musteri.musteriler)):
                print(i + 1, "-", musteri.musteriler[i].isim, musteri.musteriler[i].soyisim)
            value2 = int(input("Seçim=")) - 1
            if 0 <= value2 < len(musteri.musteriler):
                kasiyer.fatura_ode(musteri.musteriler[value2])
            else:
                print("Geçerli bir değer girmediniz!")

    if value=="0":
        print("Çıkış Yapılıyor...")
        print("Çıkış Yapıldı.")
        boolean==False
        break
