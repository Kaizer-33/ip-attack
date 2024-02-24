import subprocess
import sys

try:
    import requests
    import urllib3
    import uuid
except ImportError:
    print("Gerekli modüller indiriliyor bekleyiniz...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests==2.28.2", "urllib3==1.26.7", "uuid==1.30"])

finally:
    import concurrent.futures
    import json
    import os
    import subprocess
    import sys
    import random
    import requests
    import string
    import time
    import urllib
    import urllib3
    import uuid
    import smsapi

def menu():
    print(" [1] SMS GÖNDER")
    print(" [2] ÇIKIŞ")

def secim_yap():
    secim = input(" ~ $ ")
    return secim

def smskont(numara):
    if len(numara) != 10:
        return False
    if numara[0] != "5":
        return False
    return True

api_list = [smsapi.a101, smsapi.bim, smsapi.defacto, smsapi.istegelsin,
            smsapi.Frink, smsapi.Pidem, smsapi.Baydoner, smsapi.Dominos, smsapi.Starbucks, smsapi.Beefull, smsapi.Yuffi, smsapi.YilmazTicaret, smsapi.Yapp, smsapi.Uysal, 
            smsapi.ToptanTeslim, smsapi.Tasimacim, smsapi.Tasdelen, smsapi.Taksim, smsapi.Porty, smsapi.KuryemGelsin, smsapi.Komagene, smsapi.Happy, smsapi.Clickme, smsapi.Akbati, smsapi.Akasya, 
            smsapi.Metro, smsapi.Koton, smsapi.Naosstars, smsapi.Ayyildiz, smsapi.Ucdortbes, smsapi.Evidea, smsapi.Suiste, smsapi.Icq, smsapi.Wmf, smsapi.KahveDunyasi, smsapi.anadolu, smsapi.aygaz, 
            smsapi.bisu, smsapi.ceptesok, smsapi.coffy, smsapi.englishhome, smsapi.file, smsapi.gez, smsapi.gofody, smsapi.goyakit, smsapi.hayat, smsapi.heyscooter, smsapi.hizliecza, smsapi.hop, smsapi.ikinciyeni, 
            smsapi.ipragraz, smsapi.jetle, smsapi.joker, smsapi.kalmasin, smsapi.karma, smsapi.kimgbister, smsapi.macrocenter, smsapi.marti, smsapi.migros, smsapi.mopas, smsapi.ninewest, smsapi.oliz, smsapi.pawapp, 
            smsapi.paybol, smsapi.petrolofisi, smsapi.pinar, smsapi.pisir, smsapi.qumpara, smsapi.rabbit, smsapi.roombadi, smsapi.saka, smsapi.scooby, smsapi.signalall, smsapi.superpedestrian, smsapi.sushico, smsapi.tazi, smsapi.tiklagelsin, 
            smsapi.total, smsapi.weescooter, smsapi.yotto]


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
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçenek!")
