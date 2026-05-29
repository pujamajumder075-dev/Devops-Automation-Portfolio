#!/usr/bin/env python3
"""
Environment Access Checker
Simple script to demonstrate conditionals and type casting.
"""

def check_environment_access():
    """
    Check user environment access based on input.
    """
    print("\n" + "=" * 50)
    print("Environment Access Checker")
    print("=" * 50)
    
    # Get user input
    user = input("\nEnter user name: ")
    print(f"User name: {user}")
    
    # Type casting example
    try:
        a = int(input("\nEnter number 1: "))
        b = input("Enter number 2: ")
        
        print(f"\nData type of a: {type(a)}")
        print(f"Data type of b: {type(b)}")
        
        # Environment check
        env = input("\nEnter environment name (dev/stg/prod): ").lower()
        
        print("\n" + "-" * 50)
        print("Access Decision:")
        print("-" * 50)
        
        if env == "dev":
            print("✓ User has DEVELOPMENT access")
            print("  - Full access to dev resources")
            print("  - Can deploy and test freely")
        
        elif env == "stg":
            print("✓ User has STAGING access")
            print("  - Access to staging environment")
            print("  - Pre-production testing")
        
        elif env == "prod":
            print("✓ User has PRODUCTION access")
            print("  - Limited production access")
            print("  - Production deployments")
        
        else:
            print("✗ User DOES NOT have access")
            print(f"  - Unknown environment: {env}")
        
        print("\n" + "=" * 50)
    
    except ValueError as e:
        print(f"Error: Invalid input - {e}")

if __name__ == "__main__":
    check_environment_access()
