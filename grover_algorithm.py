import numpy as np

def grover(n):
    # Initialize the state
    state = np.full((2**n, 1), 1/np.sqrt(2**n))
    return state