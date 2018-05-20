from colorama import *
import getip
import urllib
import os
import socket
init(autoreset=True)

os.system("cls")
print(Fore.BLUE + Style.BRIGHT + "______                    " + Fore.YELLOW + " ______      ")
print(Fore.BLUE + Style.BRIGHT + "| ___ \                   " + Fore.YELLOW + " | ___ \     ")
print(Fore.BLUE + Style.BRIGHT + "| |_/ /__  ___ __ _ _ __  " + Fore.YELLOW + " | |_/ /   _ ")
print(Fore.BLUE + Style.BRIGHT + "|  __/ _ \/ __/ _` | '_ \ " + Fore.YELLOW + " |  __/ | | |")
print(Fore.BLUE + Style.BRIGHT + "| | |  __/ (_| (_| | | | |" + Fore.YELLOW + " | |  | |_| |")
print(Fore.BLUE + Style.BRIGHT + "\_|  \___|\___\__,_|_| |_|" + Fore.YELLOW + " \_|   \__, |")
print(Fore.BLUE + Style.BRIGHT + "                          " + Fore.YELLOW + "        __/ |")
print(Fore.BLUE + Style.BRIGHT + "                          " + Fore.YELLOW + "       |___/ ")
print("")
print(Fore.GREEN + Style.BRIGHT + "|------ A Tool Made By Landfill ------|")
print(Fore.RED + Style.BRIGHT + "|--------------- Enjoy ---------------|")
print(Fore.BLUE + Style.BRIGHT + "|--- Give Credit For Any Code Used ---|")
print(Fore.MAGENTA + Style.BRIGHT + "Creator Is Not Responsible For Anything")
print("")
print(Fore.BLUE + Style.BRIGHT + "[1]" + Fore.YELLOW + " Get Your Info")
print("")
choice = input("Pecan>> ")

if choice == "1":
    Your_IP = socket.gethostbyname(socket.gethostname())
    Computer_Name = socket.gethostname()
    Ex_IP = getip.get()
    print("")
    print(Fore.RED + Style.BRIGHT + "Your IP Is...",Your_IP)
    print(Fore.GREEN + Style.BRIGHT + "On...",Computer_Name)
    print(Fore.BLUE + Style.BRIGHT + "Your External IP Is...",Ex_IP)
