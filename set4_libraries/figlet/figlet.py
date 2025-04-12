import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

def main():
# Choose a font
    if len(sys.argv) == 1 :
        figlet.setFont(font = random.choice(figlet.getFonts()))
        ask_input()
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        font = sys.argv[2]
        if font in figlet.getFonts():
            figlet.setFont(font = font)
            ask_input()
        else:
            print(f"Font '{font}' is not available")
            sys.exit(1)
    else:
        print("Insufficient arguments")
        sys.exit(1)


def ask_input():
    user_input = input("Input: ")
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()
