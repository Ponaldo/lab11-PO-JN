"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


def square_root(a):
    # math.sqrt raises ValueError for negative numbers
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Cannot take the square root of a negative number")


def hypotenuse(a, b):
    # Negative side lengths are fine since each side is squared
    try:
        return math.hypot(a, b)
    except TypeError:
        raise ValueError("Hypotenuse sides must be numbers")


# First example
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # Returns b / a, so a is the divisor
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def logarithm(a, b):
    # Returns log base a of b
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive")
    return math.log(b, a)


def exponent(a, b):
    return a ** b

def add (a, b):
    return a + b

def sub (a, b):
    return a - b

def mul (a, b):
    return a * b

def div (a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Logarithm argument must be positive")
    return math.log(b,a)

def exp(a, b):
    return a ** b
