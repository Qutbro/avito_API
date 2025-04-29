import os
import subprocess
import sys
from colorama import init, Fore, Back, Style
import time

init()


def console_picture():
    print(Style.BRIGHT + Fore.YELLOW)
    print("   ___            _              _                      _             _           _    ")
    time.sleep(0.5)
    print("  / _ \   _   _  | |_           | |__    _ __    ___   ( )  ___      | |__   ___ | |_  ")
    time.sleep(0.5)
    print(" | | | | | | | | | __|          | '_ \  | '__|  / _ \   \| / __|     | '_ \ / _ \| __| ")
    time.sleep(0.5)
    print(" | |_| | | |_| | | |_           | |_) | | |    | (_) |     \__ \     | |_) | (_) | |_  ")
    time.sleep(0.5)
    print("  \__\_\  \__,_|  \__|   _____  |_.__/  |_|     \___/      |___/     |_.__/ \___/ \__| ")
    time.sleep(0.5)
    print("                        |_____|                                                        ")
    time.sleep(0.5)


console_picture()
print("Нажми Enter чтобы запустить...")
input()
print(Style.NORMAL + Fore.WHITE)
process = subprocess.Popen([sys.executable, "refresh_token.py"])
process.wait()
