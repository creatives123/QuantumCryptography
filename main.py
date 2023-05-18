import subprocess
import colorama
from colorama import Fore, Style


def main():
    colorama.init()

    print(Fore.MAGENTA + "===== Quantum Message Channel Demo =====")
    print(Fore.YELLOW + "Sender: " + Fore.RED + "Wasp")
    print(Fore.CYAN + "Receiver: " + Fore.BLUE + "Antman")
    print(Fore.MAGENTA + "---------------------------------------")

    # Open sender script in a new terminal window
    sender_process = subprocess.Popen(['python', 'wasp.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)

    # Open receiver script in a new terminal window
    receiver_process = subprocess.Popen(['python', 'antman.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)

    # Wait for the sender and receiver scripts to finish
    sender_process.wait()
    receiver_process.wait()

    colorama.deinit()


if __name__ == '__main__':
    main()
