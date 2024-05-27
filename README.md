# Grover's Algorithm Implementation

This project aims to implement Grover's algorithm in Python using matrix operations with Numpy. It does not use any libraries or function libraries that implement quantum operations. Grover's algorithm is a quantum algorithm that solves the unstructured search problem. It can find a marked element in a set of N elements in time O(√N), compared to a classical computer which would take time O(N).

## Table of Contents
1. Technologies
2. Installation
3. Usage
4. Functions
5. Contributing
6. Contact


## Technologies
Project is created with:

| Dependency | Version | Icon | 
|---|---|---|
| Python | 3.x | [<img src="https://seeklogo.com/images/P/python-logo-A32636CAA3-seeklogo.com.png" alt="python" width="40" height="40">](https://www.python.org/) |
| NumPy | 1.x | [<img src="https://seeklogo.com/images/N/numpy-logo-479C24EC79-seeklogo.com.png" alt="python" width="40" height="40">](https://numpy.org/)|

## Installation
To run this project, you will need to follow these steps:

* Clone the repository
```python
git clone https://github.com/tbernalz/Quantum-GroverAlgorithm.git
```

* Install numpy
```python
pip install numpy
```

## Usage
After installation, you can run the script from the command line with:

```python
python grover_algorithm.py
```

You will be prompted to enter the number of qubits and the target state.

## Functions
* `hadamard_transform(num_qubits)`: This function computes the Hadamard transform for n qubits.
* `oracle_function(num_qubits, target_state)`: This function flips the sign of the target state in the quantum state.
* `diffusion_operator(num_qubits)`: This function applies a global phase flip to the quantum state.
* `grover_algorithm(num_qubits, target_state)`: This function implements Grover's algorithm. It initializes the quantum state, applies the oracle function, applies the diffusion operator, and performs the Grover iteration for approximately sqrt(2^n) times.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
Tomás Bernal Zuluaga - tbernalz@eafit.edu.co

<a href="https://www.linkedin.com/in/tbernalz" target="_blank" rel="noreferrer">
    <img src="https://seeklogo.com/images/L/linkedin-new-2020-logo-E14A5D55ED-seeklogo.com.png" alt="Linkedin" width="40" height="40"/>
  </a>
