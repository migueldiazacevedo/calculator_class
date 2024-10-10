class Calculator:
    """
    A simple calculator class for performing basic arithmetic operations.
    """
    def __init__(self, value=0.0):
        self.value = value
        self.hide_print = False

    def add(self, *args: float):
        """
        Add numbers.

        This method accepts a variable number of arguments and adds the
        current value by each argument.

        :param args: Numbers to add by.
        :type args: float
        """
        self.value += sum(args)
        if not self.hide_print:
            self._print_value()

    def subtract(self, *args: float):
        """
        Subtract numbers.

        This method accepts a variable number of arguments and subtracts the
        current value by each argument.

        :param args: Numbers to subtract by.
        :type args: float
        """
        value = self.value
        for num in args:
            value -= num
        self.value = value
        self._print_value()

    def multiply(self, *args: float):
        """
        Multiply numbers.

        This method accepts a variable number of arguments and multiplies the
        current value by each argument.

        :param args: Numbers to multiply by.
        :type args: float
        """
        product = 1.0
        for num in args:
            product *= num
        self.value *= product
        self._print_value()

    def divide(self, *args: float):
        """
        Divide numbers.

        This method accepts a variable number of arguments and divides the
        current value by each argument.

        :param args: Numbers to divide by.
        :type args: float

        :raises ValueError: If division by zero is attempted.
        """
        # handle cases when starting calculator value is 0 and all division occurs from user input
        if self.value == 0.0 or 0:
            self.value = args[0]**2
        # do not allow division by zero. Otherwise, re-assign division to calculator value
        for num in args:
            if num == 0:
                raise ValueError("Division by zero is not allowed.")
            else:
                self.value /= float(num)
        self._print_value()

    def n_root(self, nth_root: int):
        """
        Take nth root.

        This method accepts a single integer number takes that root of the
        current value.

        :param nth_root: The root to take. (e.g. 2 = square root)
        :type nth_root: int
        """
        self.value = self.value**(1/nth_root)
        self._print_value()

    def reset(self):
        """
        reset the calculator value to zero

        Takes no argument
        """
        self.value = 0
        self._print_value()

    def _print_value(self):
        """
        hidden method that allows user to change if calculator value is printed to the console or not

        Takes no argument

        example:
        calculator = Calculator()
        calculator.hide_print = True  # This will prevent printing the value
        calculator.add(5, 3)  # The value will be calculated but not printed
        """
        if not self.hide_print:
            print(self.value)
