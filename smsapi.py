# smsapi.py

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


def a101(number):
    try:
        url = "https://www.a101.com.tr/users/otp-login/"
        payload = {
            "phone" : f"0{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "A101: SMS gönderildi"
        else:
            return False, "A101: SMS gönderilemedi"
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
