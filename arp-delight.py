from scapy.all import ARP, Ether, srp
import sys
import os
import time
import socket  
import random

os.system("clear")

print("[                    ] 0%")
time.sleep(3)
print("[=====               ] 25%")
time.sleep(3)
print("[==========          ] 50%")
time.sleep(3)
print("[===============     ] 75%")
time.sleep(3)
print("[====================] 100%")
time.sleep(3)

banner = """

 █████╗ ██████╗ ██████╗       ██████╗ ███████╗██╗     ██╗ ██████╗ ██╗  ██╗████████╗
██╔══██╗██╔══██╗██╔══██╗      ██╔══██╗██╔════╝██║     ██║██╔════╝ ██║  ██║╚══██╔══╝
███████║██████╔╝██████╔╝█████╗██║  ██║█████╗  ██║     ██║██║  ███╗███████║   ██║   
██╔══██║██╔══██╗██╔═══╝ ╚════╝██║  ██║██╔══╝  ██║     ██║██║   ██║██╔══██║   ██║   
██║  ██║██║  ██║██║           ██████╔╝███████╗███████╗██║╚██████╔╝██║  ██║   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝           ╚═════╝ ╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═
"""

print ("Author   : Firtual Official")
print ("You Tube : https://www.youtube.com/channel/UCk1ju-yBOPWmBfzzRdPGnOw")
print ("github   : https://github.com/FirtualOfficial")
print ("Discord  : F1rtualSec#6787")
time.sleep(3)

target_ip = "192.168.1.1/24"
# IP Address for the destination
# create ARP packet
arp = ARP(pdst=target_ip)
# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# stack them
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

# a list of clients, we will fill this in the upcoming loop
clients = []

for sent, received in result:
    # for each response, append ip and mac address to `clients` list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# print clients
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))
