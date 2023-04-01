'''
name: Colored_text.py
author: realjema
date: 01/2023
description: How to print colored text in terminal :)
'''

#first we have to install the module colorama with => pip install colorama
# once its done we can now import it 

import colorama 
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLUE+Back.YELLOW+"Hi My name is Aman realjema "+ Fore.YELLOW+Back.BLUE+"I am a python developer")
print(Back.CYAN+"Hi My name is realjema")
print(Fore.GREEN + Back.RED + "I am a software developer") 