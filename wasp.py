import colorama
from colorama import Fore
from pqc_kyber import kyber

def main():
    colorama.init()

    print(Fore.RED + "Welcome to the Quantum Message Sender (Wasp)!")
    print("Generating CRYSTALS-KYBER keys...")
    wasp_private_key = kyber.PrivateKey.generate()
    wasp_public_key = wasp_private_key.public_key()
    print("Keys generated successfully.")

    # Rest of the sender script...

    colorama.deinit()

if __name__ == '__main__':
    main()
