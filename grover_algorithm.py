import numpy as np

def hadamard_transform(num_qubits):
    # The Hadamard transform for n qubits is the nth tensor power of the base Hadamard matrix
    base_hadamard = 1/np.sqrt(2) * np.array([[1, 1], [1, -1]])
    # Initialize the Hadamard transform for n qubits as the base Hadamard matrix
    hadamard_n_qubits = base_hadamard
    
    # Compute the nth tensor power of the base Hadamard matrix
    for _ in range(num_qubits - 1):
        hadamard_n_qubits = np.kron(hadamard_n_qubits, base_hadamard)
    
    return hadamard_n_qubits

def oracle_function(num_qubits, target_state):
    if target_state >= 2**num_qubits:
        raise ValueError("Target state must be less than 2^num_qubits")
    # The oracle function flips the sign of the target state in the quantum state
    oracle_matrix = np.eye(2**num_qubits)
    oracle_matrix[target_state, target_state] = -1
    return oracle_matrix

def diffusion_operator(num_qubits):
    # The diffusion operator applies a global phase flip to the quantum state
    diffusion_matrix = 2 * np.full((2**num_qubits, 2**num_qubits), 1/(2**num_qubits)) - np.eye(2**num_qubits)
    return diffusion_matrix

def grover_algorithm(num_qubits, target_state):
    if num_qubits <= 0:
        raise ValueError("Number of qubits must be greater than 0")
    # Initialize the quantum state
    quantum_state = np.full((2**num_qubits, 1), 1/np.sqrt(2**num_qubits))
    # Apply the oracle function
    oracle_matrix = oracle_function(num_qubits, target_state)
    # Apply the diffusion operator
    diffusion_matrix = diffusion_operator(num_qubits)

    # Perform the Grover iteration for approximately sqrt(2^n) times
    for _ in range(int(np.pi/4*np.sqrt(2**num_qubits))):
        quantum_state = np.dot(diffusion_matrix, np.dot(oracle_matrix, quantum_state))

    return quantum_state

if __name__ == "__main__":
    try:
        num_qubits = int(input("Enter the number of qubits: "))
        target_state = int(input("Enter the target state: "))
        result = grover_algorithm(num_qubits, target_state)
        print(f"The final quantum state is:\n{result}")
        print(f"\nThe most probable state is: |{format(np.argmax(result), '0' + str(num_qubits) + 'b')}> ({np.argmax(result)})")
        # Print the states and their probabilities
        for i in range(2**num_qubits):
            print(f"State |{format(i, '0' + str(num_qubits) + 'b')}>: probability = {abs(result[i][0])**2:.8f}")

    except ValueError as e:
        print(f"Error: {e}")