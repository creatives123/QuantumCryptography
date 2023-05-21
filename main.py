from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import Aer, execute
import random

# Number of bits in the key
key_length = 20  # Reduced for readability

# Define the quantum register
qreg = QuantumRegister(1)

# Define the classical register
creg = ClassicalRegister(1)

print("Step 1: Alice generates her bits and bases")

# Alice prepares qubits
alice_bits = [random.randint(0,1) for _ in range(key_length)]
alice_bases = [random.randint(0,1) for _ in range(key_length)]
print(f"Alice's bits: {alice_bits}")
print(f"Alice's bases: {alice_bases}")

# Define the quantum circuit
circ = QuantumCircuit(qreg, creg)
for i in range(key_length):
    if alice_bits[i] == 1:
        circ.x(qreg[0])
    if alice_bases[i] == 1:
        circ.h(qreg[0])

print("\nStep 2: Alice prepares her qubits based on her bits and bases")

print("\nStep 3: Bob generates his random bases")

# Bob measures qubits
bob_bases = [random.randint(0,1) for _ in range(key_length)]
print(f"Bob's bases: {bob_bases}")

for i in range(key_length):
    if bob_bases[i] == 1:
        circ.h(qreg[0])
    circ.measure(qreg[0], creg[0])

print("\nStep 4: Bob measures Alice's qubits using his bases")

# Execute the circuit
backend = Aer.get_backend('qasm_simulator')
job = execute(circ, backend, shots=key_length)
result = job.result()
counts = result.get_counts(circ)

print("\nStep 5: Bob measures the qubits")

# Check which bits Bob correctly measured
bob_bits = [int(bit) for bit in list(counts.keys())]
print(f"Bob's bits: {bob_bits}")

print("\nStep 6: Alice and Bob discard the bits where their bases didn't match")

shared_bits = [alice_bits[i] for i in range(key_length) if alice_bases[i] == bob_bases[i]]
print(f"Shared bits: {shared_bits}")

shared_key = ''.join(map(str, shared_bits))

print('\nStep 7: Alice and Bob generate the shared key')
print('Shared key: ', shared_key)
