#!/usr/bin/env python3
"""
Function Testing Script
Demonstration of function definition and parameter validation.
"""

def sum_of_numbers():
    """
    Calculate and display the sum of two user-provided numbers.
    Includes validation for positive numbers only.
    """
    try:
        print("\n" + "=" * 50)
        print("Sum Calculator")
        print("=" * 50 + "\n")
        
        n1 = int(input("Enter number 1: "))
        n2 = int(input("Enter number 2: "))
        
        # Validation
        if n1 <= 0 or n2 <= 0:
            print("\n✗ Error: Both numbers must be greater than 0")
            print(f"  Number 1: {n1}")
            print(f"  Number 2: {n2}")
            return False
        
        # Calculate sum
        total = n1 + n2
        
        print(f"\n✓ Calculation successful")
        print(f"  {n1} + {n2} = {total}")
        print("\n" + "=" * 50)
        return True
    
    except ValueError:
        print("\n✗ Error: Please enter valid integers")
        return False

if __name__ == "__main__":
    sum_of_numbers()
