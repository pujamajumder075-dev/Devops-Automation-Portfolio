#!/usr/bin/env python3
"""
First Python Script - Basic Operations
Demonstration of basic arithmetic operations and type casting.
"""

def demonstrate_operations():
    """
    Show basic arithmetic operations in Python.
    """
    print("\nHello Puja!\n")
    print("=" * 50)
    print("Basic Arithmetic Operations")
    print("=" * 50)
    
    a = 10
    b = 20
    
    # Perform operations
    c = a + b  # Addition
    d = a - b  # Subtraction
    e = a * b  # Multiplication
    f = a / b  # Division
    g = "donoboti"  # String
    
    # Display results
    print(f"\na = {a}, b = {b}")
    print(f"\nAddition (a + b) = {c} [Type: {type(c).__name__}]")
    print(f"Subtraction (a - b) = {d} [Type: {type(d).__name__}]")
    print(f"Multiplication (a * b) = {e} [Type: {type(e).__name__}]")
    print(f"Division (a / b) = {f:.2f} [Type: {type(f).__name__}]")
    print(f"String = '{g}' [Type: {type(g).__name__}]")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    demonstrate_operations()
