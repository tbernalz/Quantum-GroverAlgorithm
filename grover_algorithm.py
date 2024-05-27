import numpy as np

def hadamard_transform(num_qubits):
    base_hadamard = 1/np.sqrt(2) * np.array([[1, 1],
                                              [1, -1]])
    hadamard_n_qubits = np.linalg.matrix_power(base_hadamard, num_qubits)
    return hadamard_n_qubits

def oracle_function(num_qubits, target_state):
    # Initialize the oracle matrix
    oracle_matrix = np.eye(2**num_qubits)
    # Flip the sign of the target state
    oracle_matrix[target_state, target_state] = -1
    return oracle_matrix

def diffusion_operator(num_qubits):
    # Initialize the diffusion operator
    diffusion_matrix = 2 * np.full((2**num_qubits, 2**num_qubits), 1/(2**num_qubits)) - np.eye(2**num_qubits)
    return diffusion_matrix

def grover_algorithm(num_qubits, target_state):
    # Initialize the quantum state
    quantum_state = np.full((2**num_qubits, 1), 1/np.sqrt(2**num_qubits))
    # Apply the oracle function
    oracle_matrix = oracle_function(num_qubits, target_state)
    # Apply the diffusion operator
    diffusion_matrix = diffusion_operator(num_qubits)
    
    # Perform the Grover iteration
    for _ in range(int(np.sqrt(2**num_qubits))):
        quantum_state = np.dot(diffusion_matrix, np.dot(oracle_matrix, quantum_state))
    
    return quantum_state

if __name__ == "__main__":
    num_qubits = 3
    target_state = 7
    quantum_state = grover_algorithm(num_qubits, target_state)
    print(f"The Quantum State is \n{quantum_state}")