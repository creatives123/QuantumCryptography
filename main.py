from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import Aer, execute
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from colorama import Fore, Style
from termcolor import colored
import random


# Número de bits da chave
key_length = 256  # 256 para uso na criptografia AES-256
color_match = "green"
color_no_match = "yellow"
color_share = "green"
empty_space = colored("_", color_no_match)


# Define the quantum register
qreg = QuantumRegister(1)

# Define the classical register
creg = ClassicalRegister(1)

print(Fore.GREEN + "Passo 1: Wasp gera os seus bits e bases" + Style.RESET_ALL)

# Wasp prepares qubits
wasp_bits = [random.randint(0,1) for _ in range(key_length)]
wasp_bases = [random.randint(0,1) for _ in range(key_length)]
print(f"Wasp bits:  {wasp_bits}")
print(f"Wasp bases: {wasp_bases}")

# Wasp's bits are the actual bits of information she wants to send.
# The bases determine the orientation that she'll use to encode these bits when she sends them over a quantum channel.
# Define the quantum circuit
backend = Aer.get_backend('qasm_simulator')
antman_bits = []
antman_bases = []  # Here's the change
for i in range(key_length):
    # Define the quantum register
    qreg = QuantumRegister(1)
    # Define the classical register
    creg = ClassicalRegister(1)
    # Define the quantum circuit
    circ = QuantumCircuit(qreg, creg)

    # Wasp prepares qubits
    print(Fore.GREEN + "\nPasso 2: Wasp prepara os seus qubits com base nos seus bits e bases." + Style.RESET_ALL)
    print("Ela prepara cada qubit em uma superposição de estados de acordo com os seus bits e bases.")
    if wasp_bits[i] == 1:
        circ.x(qreg[0])
    if wasp_bases[i] == 1:
        circ.h(qreg[0])

    # Ant-Man prepares bases
    print(Fore.GREEN + "\nPasso 3: Ant-Man gera as suas bases aleatórias" + Style.RESET_ALL)
    antman_base = random.randint(0, 1)
    antman_bases.append(antman_base)  # Here's the change
    print(f"Ant-Man's base for qubit {i}: {antman_base}")

    # Ant-Man measures qubits
    print(Fore.GREEN + "\nPasso 4: Ant-Man mede os qubits da Vespa usando as suas bases" + Style.RESET_ALL)
    print("Ant-Man mede cada qubit usando as suas bases.")
    if antman_base == 1:
        circ.h(qreg[0])
    circ.measure(qreg[0], creg[0])

    # Execute the circuit
    job = execute(circ, backend, shots=1)
    result = job.result()
    counts = result.get_counts(circ)
    antman_bits.append(int(next(iter(counts))))

print(f"Ant-Man bits: {antman_bits}")
print(f"Ant-Man bases: {antman_bases}")

print(Fore.GREEN + "\nPasso 5: Ant-Man mede os qubits" + Style.RESET_ALL)
print("Ele obtém uma sequência de bits como resultado dessas medições.")

# Check which bits Ant-Man correctly measured
antman_bits = [int(bit) for bit in list(counts.keys())]
print(f"Ant-Man bits: {antman_bits}")

print(Fore.GREEN + "\nPasso 6: Wasp e o Ant-Man descartam os bits onde as suas bases não coincidem" + Style.RESET_ALL)
print("Ant-Man compartilha as suas bases com a Wasp, que pode então verificar onde usaram a mesma base e onde não. Eles descartam os bits onde as suas bases não coincidiram.")

# Prepare colored bits strings for Wasp and Ant-Man
wasp_bits_color = ''
wasp_bases_color = ''
antman_bases_color = ''
shared_bits_str = ''
shared_bits = []

for i in range(key_length):
    wasp_bits_color += Fore.BLUE + str(wasp_bits[i]) + Style.RESET_ALL + " "
    if wasp_bases[i] == antman_bases[i]:
        antman_bases_color += Fore.GREEN + str(antman_bases[i]) + Style.RESET_ALL + " "
        wasp_bases_color += Fore.GREEN + str(wasp_bases[i]) + Style.RESET_ALL + " "
        shared_bits_str += Fore.GREEN + str(wasp_bits[i]) + Style.RESET_ALL + " "
        shared_bits.append(wasp_bits[i])
    else:
        antman_bases_color += Fore.RED + str(antman_bases[i]) + Style.RESET_ALL + " "
        wasp_bases_color += Fore.RED + str(wasp_bases[i]) + Style.RESET_ALL + " "
        shared_bits_str += Fore.RED + "_" + Style.RESET_ALL + " "

print("Wasp bits:  \t", wasp_bits_color)
print("Wasp bases:  \t", wasp_bases_color)
print("Ant-Man bases: \t", antman_bases_color)
print("Shared bits: \t", shared_bits_str)


shared_key = ''.join(map(str, shared_bits))

print(Fore.GREEN + '\nPasso 7: Wasp e o Ant-Man geram a chave partilhada' + Style.RESET_ALL)
print('Shared key: ', shared_key)
print('')
print(Fore.GREEN + "Wasp e o Ant-Man têm agora uma chave partilhada que podem usar para cifrar e decifrar mensagens.")
print("Esta chave foi gerada e trocada de forma segura usando distribuição quântica de chaves (QKD)." + Style.RESET_ALL)

# Convert shared key to a suitable format
key = urlsafe_b64encode(shared_key.encode()[:32])

cipher_suite = Fernet(key)

# Wasp sends a message to Ant-Man
wasp_message = b"Hello, Ant-Man! Let's go and save Cassie!"

# Wasp encrypts the message
encrypted_message = cipher_suite.encrypt(wasp_message)

print(Fore.GREEN + f"\nWasp envia a mensagem cifrada: {encrypted_message}" + Style.RESET_ALL)

# Wasp sends an encrypted message to Ant-Man.
# Only someone with the shared key can decrypt this message.

# Ant-Man receives the message and decrypts it
decrypted_message = cipher_suite.decrypt(encrypted_message)

print(Fore.GREEN + f"\nAnt-Man recebe e decifra a mensagem: {decrypted_message.decode()}" + Style.RESET_ALL)

# Ant-Man receives Wasp's message and uses the shared key to decrypt it.
