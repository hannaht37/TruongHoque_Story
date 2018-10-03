#This imports colorama, a UNIVERSAL package

from colorama import Fore, Back, Style

print(Fore.YELLOW+"This text is black."+Fore.RESET)
print(Back.GREEN+"This background is magenta."+Back.RESET)
print(Style.BRIGHT+"This is a bright style."+Style.RESET_ALL)

"""
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET. <- This is the text color.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET. <- This is the background.
Style: DIM, NORMAL, BRIGHT, RESET_ALL <- This is the text style.
"""

#This creates a class of different add-ons to our output
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.UNDERLINE + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)