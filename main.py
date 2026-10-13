import random
import string

def sifre_olustur():
    print("--- PROFESYONEL ÜCRETSİZ ŞİFRE ÜRETİCİ ---")
    print("1. Karışık (Harf, Rakam, Özel Karakter)")
    print("2. Sadece Harf ve Rakam")
    print("3. Sadece Rakam (PIN Kodu)")
    
    secim = input("\nBir mod seçin (1/2/3): ")
    
    try:
        uzunluk = int(input("Şifre kaç haneli olsun? (Örn: 12): "))
    except ValueError:
        print("\nHata: Lütfen geçerli bir sayı girin!")
        return

    karakterler = ""
    if secim == "1":
        karakterler = string.ascii_letters + string.digits + string.punctuation
    elif secim == "2":
        karakterler = string.ascii_letters + string.digits
    elif secim == "3":
        karakterler = string.digits
    else:
        karakterler = string.ascii_letters + string.digits + string.punctuation

    sifre = "".join(random.choice(karakterler) for _ in range(uzunluk))
    
    print("\n" + "="*35)
    print(f"Oluşturulan Şifreniz: {sifre}")
    print("="*35 + "\n")

if __name__ == '__main__':
    sifre_olustur()

