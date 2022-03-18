import json, os, pyfiglet
from joiner import TokenJoiner
from colorama import Fore, Style
with open('Tokens.txt') as tk:
    tokens = tk.read().splitlines()
with open('config.json') as tk:
    config = json.load(tk)
os.system("cls")
print(pyfiglet.figlet_format("Clips Joiner"))
print(f"Author: clipssender#2920")
with open("Proxies.txt") as tk:
    if len(tk.read().splitlines()) == 0:
        print(f"{Style.BRIGHT}{Fore.RED}[!] No Proxies were Found, Please input some before Restarting This Program{Style.RESET_ALL}")
        input("[!] Press Enter To Exit: ")
        exit()
if len(tokens) == 0:
    print(f"{Style.BRIGHT}{Fore.RED}[!] No Tokens were Found, Please input some before Restarting This Program{Style.RESET_ALL}")
    input("[!] Press Enter To Exit: ")
    exit()
invitecode = str(input(f"{Style.BRIGHT}{Fore.GREEN}Enter The Invite Code: \n--> {Style.RESET_ALL}"))
for token in tokens:
    joiner=TokenJoiner(config["apikey"], invitecode, token)
    joiner.joinServer()
