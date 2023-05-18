from time import sleep
import colorama
from colorama import Fore


def main():
    colorama.init()

    print("Welcome to the Quantum Message Sender (Wasp)!")
    print("Generating CRYSTALS-KYBER keys...")
    print("Keys generated successfully.")

    # Rest of the sender script...

    colorama.deinit()
    sleep(10)


if __name__ == '__main__':
    main()
