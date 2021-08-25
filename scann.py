import os 
import re 
import sys
import scapy.all as scapy
import socket 
import colorama
import scapy 
from colorama import Fore 
from colorama import init

init()

def exit():
    print("[!] Exiting [!]")
    sys.exit() 
    
def checkinter():
    wlan_pattern = re.compile("^wlan[0-9]+")
    check_wifi_result = wlan_pattern.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())
    # No adapter above wlan0 is connected
    if len(check_wifi_result) == 0:
        print("Please connect a WiFi adapter and try again.")
        exit()

def check():
    if not 'SUDO_UID' in os.environ.keys():
        print("Try running this program with sudo.")
        exit()

def scan1():
    ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
    while True:
        print(Fore.RED+"")
        t.sleep(2)
        print("----------------------------------------------------------------")
        t.sleep(0.1)
        print(" MAKE SURE ITS A RANGE (ex 192.168.1.0/24) ")
        t.sleep(0.1)
        print(" MAKE SURE YOU RAN THIS PROGRAM AS ROOT ")
        t.sleep(0.1)
        print(" MAKE SURE YOU ARE ON THE CURRENT NETWORK ")
        t.sleep(0.1)
        print(" MAKE SURE YOU HAVE PREMISSION TO DO THIS ")
        t.sleep(0.1)
        print("----------------------------------------------------------------")
        ip_add_range_entered = input("\nIPA to send ARP to ==> ")
        if ip_add_range_pattern.search(ip_add_range_entered):
            print(f"{ip_add_range_entered} is a valid IP range")
            break
    print(Fore.GREEN+"")
    arp_result = scapy.arping(ip_add_range_entered)

if __name__ == "__main__":
    checkinter()
    check()
    scan1()
