#!/usr/bin/env python3
"""
Loop Testing Script
Demonstration of for loops and conditionals.
"""

def demonstrate_loops():
    """
    Show loop and conditional examples.
    """
    print("\n" + "=" * 50)
    print("Loop and Conditional Demo")
    print("=" * 50)
    
    # Simple for loop
    print("\n1. Simple for loop (0-4):")
    for i in range(5):
        print(f"   {i}")
    
    # Loop with conditionals
    print("\n2. Environment access check (3 attempts):")
    for i in range(3):
        print(f"\n   Attempt {i + 1}:")
        env = input("   Enter environment (dev/stg/prod): ").lower()
        
        if env == "dev":
            print("   ✓ User has access to DEV environment")
        elif env == "stg":
            print("   ✓ User has access to STAGING environment")
        elif env == "prod":
            print("   ✓ User has access to PROD environment")
        else:
            print(f"   ✗ Unknown environment: {env}")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    demonstrate_loops()
