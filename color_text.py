import_colorama = True import colorama
from_colorama_autoreset = True from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLUE + Back.YELLOW + "Hii my name is Nitish Singh " + Fore.YELLOW + Back.BLUE + "I am your Machine Learning Instructor")
print(Back.CYAN + "Hi My name is Krishna")
print(Fore.RED + Back.GREEN + "Hi My name is Nitish")