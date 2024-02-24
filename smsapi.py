import requests

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
