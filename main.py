def vki_hesaplayici():
    """ Vücut kitle indexi hesaplar """
    kg = int(input("Kilonuzu giriniz(kg): "))
    boy = int(input("Boyunuzu giriniz(cm): "))
    if kg <= 0 or boy <= 0:
        print("Lütfen gerçek değerleri giriniz!")
    else:
        boy = boy/100
        vki = kg/boy**2
        if vki <= 18.5:
            a = "Vücut kitle indexiniz {} ve".format(vki)
            print(a, "Zayıfsınız!")
        elif vki > 18.5 and vki <= 24.9:
            b = "Vücut kitle indexiniz {} ve".format(vki)
            print(b, "Normal kilodasınız!")
        elif vki > 24.9 and vki <= 29.9:
            c = "Vücut kitle indexiniz {} ve".format(vki)
            print(c, "Şişmansınız! ")
        elif vki > 29.9 and vki <= 34.9:
            d = "Vücut kitle indexiniz {} ve".format(vki)
            print(d, "Obezsiniz! ")
        else:
            q = "Vücut kitle indexiniz {} ve".format(vki)
            print(q, " Ölüm riski var!")
def factorial_calculator():
    """ Faktöriyel hesaplar """
    factorial = 1
    n = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))
    if n < 0:
        print("Lütfen pozitif bir sayı giriniz.")
    elif n == 0:
        print("0'ın faktöriyeli 1'dir. ")
    else:
        for i in range(1, n+1):
            factorial = factorial*i
            l = "Girdiğiniz {} sayısının faktöriyeli: ".format(n)
        print(l, factorial)
def ehliyet():
    """ Ehliyet alıp alamayacağınızı hesaplar """
    date1 = int(input("Doğum tarihinizi giriniz: "))
    import time
    a = time.gmtime().tm_year
    age = a - date1
    if date1 <= 0:
        print("Lütfen doğru bir tarih giriniz!")
    else:
        if age >= 18:
            a = "Merhaba, yaşınız {} ve ehliyet alabilirsiniz.".format(age)
            print(a)
        elif age < 18:
            b = "Merhaba, yaşınız {} ve ehliyet alamazsınız.".format(age)
            print(b)
        else:
            pass
def permutasyon_kombinasyon():
    """ permutasyon-kombinasyon hesaplar """
    print("""permutasyon = n!/(n-r)! 
kombinasyon = n!/r!*(n-r)! şeklindedir.""")
    n = int(input("Lütfen n değerini giriniz: "))
    r = int(input("Lütfen r değerini giriniz: "))
    if n < 0 or r < 0:
        print("Lütfen pozitif değerler giriniz!")
    elif n == 0:
        nfactoriyel = 1
    elif r == 0:
        rfactoriyel = 1
    else:
        nfactoriyel = 1
        rfactoriyel = 1
        nrfactoriyel = 1
        for i in range(1, n+1):
            nfactoriyel = nfactoriyel*i
        for x in range(1, r+1):
            rfactoriyel = rfactoriyel*x
        for y in range(1, (n-r)+1):
            nrfactoriyel = nrfactoriyel*y
            permutasyon = nfactoriyel/nrfactoriyel
            kombinasyon = nfactoriyel/rfactoriyel*nrfactoriyel
        print("Permutasyon değeriniz: ", int(permutasyon))
        print("Kombinasyon değeriniz: ", int(kombinasyon))
from math import*
def kok():
    """ Kök buldurur """
    print("Girdiğiniz 2. dereceden denklem a*x**2+b*x+c şeklinde olmalıdır!")
    a = int(input("Lütfen a değerini giriniz: "))
    b = int(input("Lütfen b değerini giriniz: "))
    c = int(input("Lütfen c değerini giriniz: "))
    delta = b**2-4*a*c
    x1 = (-b+(sqrt(delta)))/2*a
    x2 = (-b-(sqrt(delta)))/2*a
    if delta == 0:
        print("Çakışık iki kök vardır ve kök: ",x1)
    elif delta > 0:
        print("Birinci kök: ", x1)
        print("İkinci kök: ", x2)
    else:
        print("Reel kök yoktur! ")
def mukemmel_sayi():
    """Mükemmel sayı olup olmadığını söyler"""
    print("Matematikte bazı pozitif tam sayıların pozitif bölenleri toplamı, sayının kendisinin iki katına eşittir. Bu tür sayılara “mükemmel sayı” denir.")
    sayi = int(input("Lütfen kontrol etmek istediğniz sayıyı giriniz: "))
    if sayi < 0:
        print("Lütfen pozitif bir sayı giriniz: ")
    elif sayi == 0:
        print("0 mükemmel sayı değildir! ")
    else:
        sayac=0
    for i in range(1, sayi):
        if sayi % i == 0:
            sayac = sayac+i
        elif sayi % i != 0:
            continue
    if sayac == sayi:
        a = "Girdiğiniz {} sayısı mükemmel sayıdır.".format(sayi)
        print(a)
    elif sayac != sayi:
        b = "Girdiğiniz {} sayısı mükemmel sayı değildir".format(sayi)
        print(b)
def askerlik():
    """Askerlik hesaplatır"""
    import time
    a = time.gmtime().tm_year
    date2 = int(input("Lütfen doğum yılınızı giriniz: "))
    age = a - date2
    if age < 21:
        print("Henüz askerlik yaşınız gelmedi.")
    elif age >= 21:
        print("Askere gitme yaşınız gelmiş bulunmaktadır.")
    else:
        pass
def yukseklik_hesaplayici():
    """Havaya atılan topun yüksekliğini hesaplar"""
    print("formül h=1/2*g*t**2 şeklindedir.")
    g = int(input("Yerçekimi ivmesini(g) giriniz: "))
    t = int(input("Lütfen hareket süresince geçen süreyi giriniz: "))
    h = 1/2*g*t**2
    print("Topun çıktığı max yükseklik(m): ", h)
def asal_sayi():
    """Asal sayı sorgulatır"""
    sayi = int(input("Lütfen sorgulatmak istediğiniz sayıyı giriniz: "))
    a = "Girdiğiniz {} sayısı".format(sayi)
    sayac = 0
    for i in range(2, sayi+1):
        if sayi % i == 0:
            sayac += 1
    if sayac == 1:
        print(a, "asaldır.")
    elif sayi < 0:
        print("Negatif sayılarda asallık aranmaz.")
    else:
        print(a, "asal değildir.")
while True:
    secenekler = (int(input("****MIX(learn mode)****\n ----9 adet uygulamamız bulunmaktadır----\n 1: Vki\n 2: Faktöriyel\n 3: Ehliyet\n 4: Permutasyon-Kombinasyon\n 5: 2. Dereceden Denklemin Köklerini Bulma\n 6: Mükemel Sayı\n 7: Askerlik Kontrolü\n 8: Havaya Atılan Topun Yüksekliğini Hesaplama\n 9: Asal Sayı Sorgulama \n\n\n 10: ÇIKIŞ\n\n\n --> Kullanmak istediğiniz uygulama: ")))
    if secenekler == 1:
        vki_hesaplayici()
    elif secenekler == 2:
        factorial_calculator()
    elif secenekler == 3:
        ehliyet()
    elif secenekler == 4:
        permutasyon_kombinasyon()
    elif secenekler == 5:
        kok()
    elif secenekler == 6:
        mukemmel_sayi()
    elif secenekler == 7:
        askerlik()
    elif secenekler == 8:
        yukseklik_hesaplayici()
    elif secenekler == 9:
        asal_sayi()
    elif secenekler == 10:
      print("program kapanıyor...")
      break
    else:
        print("Lütfen geçerli bir sayı girin.")
