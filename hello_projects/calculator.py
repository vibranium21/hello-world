#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculator."""


def add(val1, val2):
    """Add val2 to val1."""
    return val1 + val2


def subtract(val1, val2):
    """Substract val2 to val1."""
    return val1 - val2


def multiply(val1, val2):
    """Multiply val1 by val2."""
    return val1 * val2


def divide(val1, val2):
    """Divide val1 by val2."""
    return val1 / val2


print("Select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division")
while True:
    choice = input(" Enter choice (1/2/3/4) : ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    print("Invalid Input")
