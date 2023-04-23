import random
karakterler = "4-/* !&$#?—@abcdefghijkInopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWD(YZ1234567890"
sifre_uzunlugu = int(input("Sifrenin uzunlugunu giriniz:"))
sifre = ""
for i in range("sifre_uzunluğu"):
    sifre += random.choice(karakterler)
print(sifre)
