# Calculator Module

A simple Python class for performing basic arithmetic operations. This `Calculator` class allows you to perform addition, subtraction, multiplication, division, and nth root calculations.

see package details at: <https://test.pypi.org/project/calculator-pkg-MAD/>

## Installation

You can use the `Calculator` class by importing it into your Python project. Here's how you can do it.

In Terminal:

```bash
pip install -i <https://test.pypi.org/simple/> calculator-pkg-MAD==0.1.1
```

In Python:

```python
from calculator_pkg_MAD.calculator import Calculator

# Create an instance of the Calculator
calculator = Calculator()
```

## Usage

### Initializing a calculator

You can create a Calculator instance and initialize it with an optional initial value.

```python
# Create a Calculator with an initial value of 10
calculator = Calculator(10)
```

### Performing Calculations

The `Calculator` class provides the following methods for performing calculations:

- `add(*args: float)`: Add numbers together.
- `subtract(*args: float)`: Subtract numbers from one another.
- `multiply(*args: float)`: Multiply numbers together.
- `divide(*args: float)`: Divide numbers.
- `n_root(nth_root: int)`: Take the nth root of a number.

Example Usage

```python
# Create a calculator instance
calculator = Calculator()

# Perform calculations
calculator.add(5, 3)  # Adds 5 and 3, result: 8
calculator.subtract(10)  # Subtracts 10 from the calculator value, result:-2
calculator.multiply(4)  # Multiplies calculator value by 4, result: -8.0
calculator.divide(2)  # Divides calculator value by 2, result: -4.0
calculator.n_root(2)  # Takes the square root of calculator value, result: (1.2246467991473532e-16+2j)
calculator.reset()  # Resets calculator value to 0, result: 0
```

### Controlling Output

The `Calculator` class allows you to control whether the value is printed to the console or not using the `hide_print` attribute.

### Exception Handling

The `Calculator` class raises a `ValueError` when attempting to divide by zero.

### License

This code is released under the [MIT License](https://opensource.org/license/mit/)
