# this is code for addition
def add(a, b):
    return a + b


# this is code for subtraction
def subtract(a, b):
    return a - b


# this is code for multiplication
def multiply(a, b):
    return a * b


# this is code for division
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# this is exponentiation code
def exponentiate(base, exponent):
    return base ** exponent


# this is modulus code
def modulus(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b
