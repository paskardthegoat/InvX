from time import sleep
import os
from typing_extensions import Self
from urllib import request
import requests
import time
import random, string
from discord_webhook import DiscordWebhook 
from colorama import init, Fore
init(convert=True)

try: 
    from discord_webhook import DiscordWebhook  
except ImportError:  
    
    input(
        f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nYou can ignore this error if you aren't going to use a webhook.\nPress enter to continue.")
    USE_WEBHOOK = False
try:  
    import requests  
except ImportError:  
    
    input(
        f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
    exit()  
try:  
    import numpy  
except ImportError:  
    input(
        f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
    exit()  

generator =''
caracteres = ['a','b','c','c','d','e','f','g','h','i','j','k','l','n','m','o','p','q','r','s','t','u','v','w','x','y','z']
nombre = ['5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
number = ['7','8','9']

nombredecaracteres = random.choice(number)

code = "https://discord.gg/%s" % (('').join(random.choices(string.ascii_letters + string.digits, k=(16))))

url = "https://github.com"
try:
    response = requests.get(url)  
    print(Fore.WHITE + "Internet check")
    time.sleep(.4)
    os.system("cls")
except requests.exceptions.ConnectionError:
    input("Tu n'est pas connecté à internet, redémarre ta connexion ou connecte toi à internet \npour utiliser le logiciel\nPress enter to exit")
    exit()  

print(f"""{Fore.BLUE}
                                             
                                            $$$$$$\                    $$\   $$\ 
                                            \_$$  _|                   $$ |  $$ |
                                              $$ |  $$$$$$$\ $$\    $$\\$$\ $$  |
                                              $$ |  $$  __$$\\$$\  $$  |\$$$$  / 
                                              $$ |  $$ |  $$ |\$$\$$  / $$  $$<  
                                              $$ |  $$ |  $$ | \$$$  / $$  /\$$\ 
                                            $$$$$$$ \$$|  $$ |  \$  /  $$ /  $$ |
                                            \______| \__| \__|   \_/   \__|  \__|
                                                    Dev by Paskard#9446
                                     
                                      
""".center(os.get_terminal_size().columns))
print(f"{Fore.RED}[{Fore.GREEN}>{Fore.RED}] {Fore.BLUE}If you want to use a Discord webhook, type it here or press enter to ignore".center(os.get_terminal_size().columns))
url = input('')
print(f"{Fore.RED}[{Fore.GREEN}>{Fore.RED}]  {Fore.BLUE}CAUTION : IF YOU USE WEBHOOK THERE MAY BE ERRORS AND LIMITED REQUESTS".center(os.get_terminal_size().columns))
input("")
    




webhook = url if url != "" else None

if webhook is not None:
                DiscordWebhook(  
                        url=url,
                        content=f"```Started checking urls\nI will send any valid codes here```"
                    ).execute()



while(True):
    invite = (('').join(random.choices(string.ascii_letters + string.digits, k=(10))))
    code = "https://discord.com/api/v6/invite/%s" + invite
    getcode = requests.get(code)

    if getcode.status_code ==200:
        print(f"{Fore.RED}[{Fore.GREEN}>{Fore.RED}]{Fore.GREEN} Valid | https://discord.gg/{invite}".center(os.get_terminal_size().columns))
    else:
        print(f"{Fore.RED}[{Fore.GREEN}>{Fore.RED}]{Fore.RED} Invalid | https://discord.gg/{invite}".center(os.get_terminal_size().columns))

    with open("invites.txt", "a") as invitefile:

        invitefile.write(f"{code}\n")
    
    if webhook is not None:
        DiscordWebhook(  
                        url=url,
                        content=f"{code}"
                    ).execute()

    
    
    
    

        
    

