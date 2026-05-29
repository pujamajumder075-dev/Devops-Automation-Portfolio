#!/usr/bin/env python3
"""
Multiplication Table Generator
Generate and display multiplication tables with user interaction.
"""

def generate_multiplication_table():
    """
    Generate multiplication table for a user-specified number.
    """
    print("\n" + "=" * 50)
    print("Multiplication Table Generator")
    print("=" * 50 + "\n")
    
    # Quick test
    print("Quick test (numbers 1-10):")
    for i in range(1, 11):
        print(f"  {i}", end=" ")
    print("\n")
    
    # Get user input
    try:
        num = int(input("Enter a number to see its multiplication table: "))
        
        print(f"\nMultiplication Table of {num}:")
        print("-" * 30)
        
        # Generate table
        for i in range(1, 11):
            result = num * i
            print(f"  {num} × {i:2d} = {result:3d}")
        
        print("-" * 30)
        
        # Ask for confirmation to quit
        print("\n")
        while True:
            choice = input("Do you want to quit? (yes/no): ").lower()
            
            if choice in ["yes", "y"]:
                print("\nThank you for using the Multiplication Table Generator!")
                print("=" * 50)
                break
            elif choice in ["no", "n"]:
                print("\nLet's continue...\n")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    generate_multiplication_table()
