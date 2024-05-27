# Grover's Algorithm Implementation

This project implements Grover's algorithm in Python using matrix operations with NumPy. It avoids any libraries or functions that specifically implement quantum operations. Grover's algorithm is a quantum algorithm designed to solve the unstructured search problem. It can find a marked element in a set of N elements in O(√N) time, compared to O(N) time for classical algorithms.

## Table of Contents
1. [Technologies](#technologies)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Functions](#functions)
5. [Contributing](#contributing)
6. [Contact](#contact)


## Technologies
Project is created with:

| Dependency | Version | Icon | 
|---|---|---|
| Python | 3.x | [<img src="https://seeklogo.com/images/P/python-logo-A32636CAA3-seeklogo.com.png" alt="python" width="40" height="40">](https://www.python.org/) |
| NumPy | 1.x | [<img src="https://seeklogo.com/images/N/numpy-logo-479C24EC79-seeklogo.com.png" alt="python" width="40" height="40">](https://numpy.org/)|


## Installation
To run this project, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/tbernalz/Quantum-GroverAlgorithm.git
    ```

2. Install the required dependencies:

    ```sh
    pip install numpy
    ```

## Usage

After installation, you can run the script from the command line with:

```sh
python grover_algorithm.py
```

You will be prompted to enter the number of qubits and the target state.

## Functions

* `hadamard_transform(num_qubits)`: Computes the Hadamard transform for n qubits.
* `oracle_function(num_qubits, target_state)`: Flips the sign of the target state in the quantum state.
* `diffusion_operator(num_qubits)`: Applies a global phase flip to the quantum state.
* `grover_algorithm(num_qubits, target_state)`: Implements Grover's algorithm. It initializes the quantum state, applies the oracle function, applies the diffusion operator, and performs the Grover iteration for approximately \(\sqrt{2^n}\) times.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## Contact
Tomás Bernal Zuluaga - [tbernalz@eafit.edu.co](mailto:tbernalz@eafit.edu.co)

<a href="https://www.linkedin.com/in/tbernalz" target="_blank" rel="noreferrer">
    <img src="https://seeklogo.com/images/L/linkedin-new-2020-logo-E14A5D55ED-seeklogo.com.png" alt="Linkedin" width="40" height="40"/>
  </a>
