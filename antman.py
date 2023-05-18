from time import sleep
import colorama
from colorama import Fore, Style


def main():
    colorama.init()

    print(Fore.BLUE + "Welcome to the Quantum Message Receiver (Antman)!")
    # Rest of the receiver script...

    colorama.deinit()
    sleep(10)


if __name__ == '__main__':
    main()
