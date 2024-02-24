import time
import smsapi  # smsapi modülünü ekledim

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

def sms_gonder(numara, adet):
    api_list = [smsapi.a101, smsapi.bim, smsapi.defacto, smsapi.istegelsin]
    for api in api_list:
        success, message = api(numara)
        if success:
            print(message)
        else:
            print(message)

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
