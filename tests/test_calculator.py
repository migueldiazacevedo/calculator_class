import pytest
from calculator_pkg.calculator import Calculator


def test_add():
    calculator = Calculator(5)
    calculator.add(3)
    assert calculator.value == 8.0


def test_add_result_type_int():
    calculator = Calculator(5)
    calculator.add(3)
    assert isinstance(calculator.value, int)


def test_add_result_type_float():
    calculator = Calculator(5.0)
    calculator.add(3.0)
    assert isinstance(calculator.value, float)


def test_add_many_no_initializing():
    calculator = Calculator()
    calculator.add(1, 1, 1, 1, 1, 1, 1, 1)
    assert calculator.value == 8.0


def add_negative():
    calculator = Calculator()
    calculator.add(-1, -1, -1, -1, -1, -1, -1, -1)
    assert calculator.value == -8.0


def test_subtract():
    calculator = Calculator(10)
    calculator.subtract(2)
    assert calculator.value == 8.0


def test_subtract_result_type_int():
    calculator = Calculator(5)
    calculator.subtract(3)
    assert isinstance(calculator.value, int)


def test_subtract_result_type_float():
    calculator = Calculator(5.0)
    calculator.subtract(3.0)
    assert isinstance(calculator.value, float)


def test_subtract_negative():
    calculator = Calculator(-4)
    calculator.subtract(-4)
    assert calculator.value == 0.0


def test_multiply():
    calculator = Calculator(4)
    calculator.multiply(2)
    assert calculator.value == 8.0


def test_multiply_negative():
    calculator = Calculator(4)
    calculator.multiply(-2)
    assert calculator.value == -8.0


def test_multiply_result_type():
    calculator = Calculator(5)
    calculator.multiply(3)
    assert isinstance(calculator.value, float)


def test_divide():
    calculator = Calculator(16)
    calculator.divide(2)
    assert calculator.value == 8.0


def test_divide_negative():
    calculator = Calculator(8)
    calculator.divide(-2)
    assert calculator.value == -4.0


def test_divide_result_type():
    calculator = Calculator(5)
    calculator.divide(3)
    assert isinstance(calculator.value, float)


def test_root_result():
    calculator = Calculator(4)
    calculator.n_root(2)
    assert calculator.value == 2.0


def test_root_of_negative_num_type():
    calculator = Calculator(-4)
    calculator.n_root(2)
    assert isinstance(calculator.value, complex)


def test_root_result_type():
    calculator = Calculator(4)
    calculator.n_root(2)
    assert isinstance(calculator.value, float)


def test_reset():
    calculator = Calculator(4)
    calculator.reset()
    assert calculator.value == 0.0


def test_reset_type():
    calculator = Calculator(4)
    calculator.reset()
    assert isinstance(calculator.value, int)


def test_divide_by_zero():
    calculator = Calculator(10)
    with pytest.raises(ValueError):
        calculator.divide(0)


if __name__ == '__main__':
    pytest.main()
