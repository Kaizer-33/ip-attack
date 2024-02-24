import phonenumbers as pnumb
import time
import smsapi
import glblapi

from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone


def menu():
    print(" [1] SMS GÖNDER")
    print(" [2] ARAMA GÖNDER")
    print(" [3] TEL SORGU GL")
    print(" [4] ÇIKIŞ")

def secim_yap():
    secim = input(" ~ $ ")
    return secim

def smskont(numara):
    if len(numara) != 10:
        return False
    if numara[0] != "5":
        return False
    return True

def arakont(arama):
    if len(arama) != 13:
        return False
    return True

def sms_gonder(numara, adet):
    print(f"'{numara}' numarasına {adet} adet SMS gönderildi.")
    smsapi.sms_gonder(numara, adet)

while True:
    menu()
    secim = secim_yap()
    if secim == "1":
        smsat = input("Telefon numarasını giriniz: ")
        if smskont(smsat):
            adet = input("Kaç SMS gönderilsin? Sınırsız gönderim için 0 basın: ")
            if adet.isdigit():
                adet = int(adet)
                if adet == 0:
                    print("Sınırsız SMS gönderimi başlatıldı.")
                elif 1 <= adet <= 500:
                    print(f"'{smsat}' numarasına {adet} adet SMS göndermek için işlem başlatılıyor...")
                    sms_gonder(smsat, adet)
                else:
                    print("Geçersiz SMS adeti! Lütfen 1 ile 500 arasında bir sayı girin.")
            else:
                print("Geçersiz giriş! Lütfen bir sayı girin.")
        else:
            print("Geçersiz telefon numarası! 10 haneli bir numara girin.")
    elif secim == "2":
        ara = input("+90 Şeklinde No Giriniz: ")
        if arakont(ara):
            print(f"'{ara}' Numarasına Arama Gönderildi.")
        else:
            print("Geçersiz telefon numarası! +90 ile başlayan bir numara girin.")
    elif secim == "3":
        glbl = input("Global No Sorgu İçin +90 Şeklinde Giriniz:")
        if arakont(glbl):
            print("Sorgu Sonuçları geliyor Bekleyiniz...")
            time.sleep(3)  # 3 saniye bekleme
            glblapi.sorgugl(glbl)  # glblapi modülündeki sorgugl işlevini çağırma
        else:
            print("Geçersiz telefon numarası! +90 ile başlayan bir numara girin.")
    elif secim == "4":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçenek! Lütfen 1 ile 4 arasında bir rakam girin.")
