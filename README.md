# Mathematical Utility Functions

This project contains a collection of mathematical utility functions implemented in Python.

## Functions

The project includes the following functions:

1. `factorial(n)`: Calculates the factorial of a non-negative integer n
2. `is_prime(n)`: Determines if a number is prime
3. `is_power_of_5(n)`: Checks if a number is a power of 5
4. `is_power_of_2(n)`: Checks if a number is a power of 2

## Usage

To use these functions, import them from the `utils` module:

```python
from utils import factorial, is_prime, is_power_of_5, is_power_of_2

# Calculate factorial
result = factorial(5)  # Returns 120

# Check if number is prime
is_prime(7)  # Returns True
is_prime(4)  # Returns False

# Check if number is a power of 5
is_power_of_5(125)  # Returns True (5^3 = 125)
is_power_of_5(100)  # Returns False

# Check if number is a power of 2
is_power_of_2(16)  # Returns True (2^4 = 16)
is_power_of_2(18)  # Returns False
```

## Running Tests

Run the main.py file to test all functions:

```bash
python main.py
```

This will run a series of tests for each function with various input values. 