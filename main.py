import json, os, pyfiglet
from joiner import TokenJoiner
from itertools import cycle
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style
with open('tokens.txt', 'r') as tk:
        tokenss = tk.read().splitlines()
def Gettokens():
    with open('tokens.txt', 'r') as temp_file:
        token = [line.rstrip('\n') for line in temp_file]
    return token
token = Gettokens()
tokens_pool = cycle(token)
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
with open('Tokens.txt') as tk:
    if len(tk.read().splitlines())==0:
        print(f'{Style.BRIGHT}{Fore.RED}[!] No Tokens were Found, Please input some before Restarting This Program{Style.RESET_ALL}')
        input("[!] Press Enter To exit")
        exit()
invitecode = str(input(f"{Style.BRIGHT}{Fore.GREEN}Enter The Invite Code: --> {Style.RESET_ALL}"))
threadAmount = input(f"{Style.BRIGHT}{Fore.GREEN}{Style.BRIGHT}Number of threads --> {Style.RESET_ALL}")
def Joiner():
        try:
            for tucan in tokenss:
                tokens = next(tokens_pool)
                joiner=TokenJoiner(config["apikey"], invitecode, tokens)
                joiner.JoinServer()
        except Exception as e:
            print(f'Error occured. errcode: {e}')
            Joiner()
if __name__ == "__main__":
    threadAmount = 1 if threadAmount == "" else int(threadAmount)
    os.system("cls")
    threads = []
    with ThreadPoolExecutor(max_workers=threadAmount) as joiner:  
        for x in range(threadAmount):
            joiner.submit(Joiner)
