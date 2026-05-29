#!/usr/bin/env python3
"""
Python Dictionary Operations
Demonstration of dictionary creation, access, update, and iteration.
"""

def demonstrate_dictionaries():
    """
    Showcase various dictionary operations.
    """
    # Create a dictionary
    user = {
        "name": "Puja",
        "age": 25,
        "city": "Bangalore",
        "hometown": "dhupguri",
        "salary": 6.2,
        "hobbies": ["dancing", "singing", "cooking"]
    }
    
    print("=" * 50)
    print("Dictionary Operations Demo")
    print("=" * 50)
    
    # Display entire dictionary
    print("\n1. Complete Dictionary:")
    print(user)
    
    # Access specific key
    print(f"\n2. Name: {user['name']}")
    
    # Access with string formatting
    print(f"\n3. Hometown: {user['hometown']}")
    
    # Using get() with default value
    hobby = user.get("hobby", "no hobbies found")
    print(f"\n4. Hobby (before update): {hobby}")
    
    # Update dictionary
    user.update({"hobby": "dancing"})
    print(f"\n5. Hobby (after update): {user.get('hobby')}")
    
    # Iterate through dictionary
    print("\n6. All key-value pairs:")
    for key, value in user.items():
        print(f"   {key}: {value}")
    
    # Get only keys
    print(f"\n7. Dictionary Keys: {list(user.keys())}")
    
    # Get only values
    print(f"\n8. Dictionary Values: {list(user.values())}")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    demonstrate_dictionaries()
