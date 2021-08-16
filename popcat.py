import json, sys, cloudscraper, time, os, colorama, ctypes, datetime, platform
from colorama import Fore, Back, Style
from datetime import date
from time import gmtime, strftime

today = date.today()
d2 = today.strftime("%B %d, %Y")

starter = Style.BRIGHT +"Usage : "+ Fore.GREEN +"(example)" + Fore.BLUE + "python popcat.py popcat.txt"

if platform.system()=='Linux':
    os.system('clear')
    print('\33]0;POPCAT SPAM Loaded V2.0\a', end='', flush=True)
else:
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW(f'POPCAT SPAM Loaded V2.0 | {d2}')

print(f"""{Style.BRIGHT + Fore.RED}
 ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ 
 ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗
 ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║
 ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║
 ██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ 
                                                                                                             
{Fore.WHITE}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════
{Style.BRIGHT + Fore.YELLOW}  
                               POPCAT 800 Clicker Made By Manualize and Eagle Eye
                               Make Sure You Put URL Popcat Token List 'popcat.txt'
                                            https://dragonforce.io
                                            Telegram: dragonforceio
                                Get Started With (pip install -r requirements.txt)                                                 
                                      NOTE : CTRL + C (To stop the process)

{Fore.WHITE}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════
""")

def loadFile(word):
    try:
        file = open(word,"r")
        lines = file.readlines()
        return lines
    except:
        print(Style.BRIGHT + "                                           File {} does not exist!".format(word))
        sys.exit(0)

def fetchUrl(url):
    scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'firefox',
        'platform': 'linux',
        'mobile': False
    }
)
    return scraper.get(url)

def popit(x):
    stripx = loadFile(x)
    for strx in stripx:
        gotcha = fetchUrl(strx.replace("\n",""))
        if(gotcha.status_code>=200 and gotcha.status_code<=299):
            x = json.loads(gotcha.text)
            print(Style.BRIGHT+Fore.GREEN + "\t\tStatus -> {} :: Successfully Created at -> {} ".format(gotcha.status_code,x['Location']))
            time.sleep(30)
            continue

zombie = 1
try:
    if(len(sys.argv)>2):
        print(Fore.RED +"\t\t\t\t\t\tUnknown command! -> {}\n\n".format(sys.argv[2]))
        sys.exit(0)
    else:
        print("-------------------------------------------------.:: STARTING ::.-------------------------------------------------\n\n")
        while zombie!=0: #infinity
            try:
                popit(sys.argv[1])
            except KeyboardInterrupt:
                print(Fore.RED +'\t\t\t\t\t\tProcess Stopped!' + Fore.WHITE)
                try:
                    sys.exit(0)
                except SystemExit:
                    os._exit(0)
except: 
    print("\t\t\t\t    " + starter + Fore.WHITE + "\n\n")
