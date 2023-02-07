#!/usr/bin/python3

def factorial(number):
    """Calculates the factorial of a given number."""
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

print(factorial(5))

