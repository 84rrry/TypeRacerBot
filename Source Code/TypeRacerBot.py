from BotLogic import TypeRacerbot
import os
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

# Use 'cls' for Windows, 'clear' for Linux/MacOS
os.system('cls' if os.name == 'nt' else 'clear')
width = os.get_terminal_size().columns

#Custom color print functions
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk).center(width+10))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk).center(width+10))

cprint(figlet_format('Welcome!',justify="center",width = width), 'yellow', attrs=['bold'])

# Browser selection loop
browser_choice = ''
while True:
    print("\033[93m Choose your browser: \033[00m".center(width+10))
    print("\033[93m  1. Google Chrome \033[00m".center(width+10))
    print("\033[93m  2. Mozilla Firefox \033[00m".center(width+10))
    print("\033[93m  3. Microsoft Edge \033[00m".center(width+10))
    browser_choice = input("Enter choice (1-3): ".center(width - 2)) # Adjusted for better centering
    if browser_choice in ['1', '2', '3']:
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        prRed('Invalid browser choice! Please try again.')

# Speed selection loop
while True:
    print("\033[93m Choose the desired Speed: \033[00m".center(width+10))
    print("\033[93m  -enter 0 to type like my grandma \033[00m".center(width+10))
    print("\033[93m  -enter 1 to type using two fingers like a boomer \033[00m".center(width+10))
    print("\033[93m  -enter 2 to type like you have two hands \033[00m".center(width+10))
    print("\033[93m  -enter 3 to type like a touchtyping world champ \033[00m".center(width+10))
    print("\033[93m  -enter 4 and they'll eat your dust \033[00m".center(width+10))
    print("\033[93m  -enter 5 fu*k it i'm a hacker \033[00m".center(width+10))
    speed_choice = input("Enter speed choice (0-5): ".center(width-4)) # Adjusted for better centering
    
    speed_map = {
        '0': 20,
        '1': 40,
        '2': 80,
        '3': 180,
        '4': 220,
        '5': 10000
    }
    
    if speed_choice in speed_map:
        speed_wpm = speed_map[speed_choice]
        prCyan(f"Selected speed: {speed_wpm} WPM. Initiating bot...")
        prCyan('#'*100)
        print('Loading....')
        TypeRacerbot(browser_choice, speed_wpm)
        break
    else: 
        os.system('cls' if os.name == 'nt' else 'clear')
        prRed('Invalid speed choice! Please try again.')
