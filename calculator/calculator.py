"""calculator.py

This module provides a simple calculator class that supports
basic arithmetic operations and keeps a history of calculations.
"""

class Calculation:
    """Represents a mathematical calculation."""
 
    def __init__(self, operation: str, result: float):
        """Initialize a Calculation instance.

        Args:
            operation (str): The operation performed.
            result (float): The result of the operation.
        """
        self.operation = operation
        self.result = result

class Calculator:
    """A simple calculator to perform basic arithmetic operations and store history."""

    history = []

    @staticmethod
    def add(a: float, b: float) -> float:
        """Return the sum of two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of a and b.
        """
        result = a + b
        Calculator._store_in_history(f"{a} + {b}", result)
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Return the difference between two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The difference of a and b.
        """
        result = a - b
        Calculator._store_in_history(f"{a} - {b}", result)
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Return the product of two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of a and b.
        """
        result = a * b
        Calculator._store_in_history(f"{a} * {b}", result)
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Return the quotient of two numbers.

        Args:
            a (float): The numerator.
            b (float): The denominator.

        Raises:
            ZeroDivisionError: If b is zero.

        Returns:
            float: The quotient of a and b.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        Calculator._store_in_history(f"{a} / {b}", result)
        return result

    @classmethod
    def _store_in_history(cls, operation: str, result: float):
        """Store the calculation in history.

        Args:
            operation (str): The operation performed.
            result (float): The result of the operation.
        """
        cls.history.append(Calculation(operation, result))

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        """Retrieve the last calculation from history.

        Raises:
            ValueError: If there are no calculations in history.

        Returns:
            Calculation: The last calculation performed.
        """
        if cls.history:
            return cls.history[-1]
        raise ValueError("No calculations in history.")
