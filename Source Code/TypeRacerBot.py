
from BotLogic import TypeRacerbot
import pprint as pp
import os
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
os.system('cls')
width = os.get_terminal_size().columns
#Custom color print functions
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk).center(width+10))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk).center(width+10))
cprint(figlet_format('Welcome!',justify="center",width = width), 'yellow', attrs=['bold'])
while True:
    print("\033[93m Choose the desired Speed: \033[00m".center(width+10))
    print("\033[93m  -enter 0 to type like my grandma \033[00m".center(width+10))
    print("\033[93m  -enter 1 to type using two fingers just like your sister \033[00m".center(width+10))
    print("\033[93m  -enter 2 to type like you have two hands \033[00m".center(width+10))
    print("\033[93m  -enter 3 to type like a touchtyping world champ \033[00m".center(width+10))
    print("\033[93m  -enter 4 and they'll eat your dust \033[00m".center(width+10))
    print("\033[93m  -enter 5 fu*k it i'm a hacker \033[00m".center(width+10))
    Choice=input()
    
    if Choice=='0':
        prCyan("let's type like my grandma!")
        prCyan('#'*100)
        print('Loading....')
        TypeRacerbot(5)
        break

    elif Choice=='1':
        prCyan("let's type using two fingers just like your sister!")
        prCyan('#'*100)
        print('Loading....')
        TypeRacerbot(30)
        
        break
    elif Choice=='2':
        prCyan("let's type like we actually have two hands!")
        prCyan('#'*100)
        print('Loading....')
        TypeRacerbot(80)
        
        break
    elif Choice=='3':
        prCyan("let's type like a touchtyping world champ!")
        prCyan('#'*100)
        print('Loading....')
        TypeRacerbot(180)
        
        break
    elif Choice=='4':
        prCyan("let them eat your dust!")
        prCyan('#'*100)
        print('Loading....')
        TypeRacerbot(220)
        
        break
    elif Choice=='5':
        prCyan("stop hacking please!")
        prCyan('#'*100)
        print('Loading....')
        TypeRacerbot(10000)
        
        break
    else: 
        os.system('cls')
        prRed('wrong Functionality pls try again!')
        


