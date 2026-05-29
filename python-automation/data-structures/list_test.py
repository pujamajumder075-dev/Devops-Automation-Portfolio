#!/usr/bin/env python3
"""
Python List Operations
Demonstration of list creation, manipulation, and iteration.
"""

def demonstrate_lists():
    """
    Showcase various list operations.
    """
    print("=" * 50)
    print("List Operations Demo")
    print("=" * 50)
    
    # Create a list with mixed data types
    a = [1, 6.5, "hello", True]
    print(f"\n1. Original List: {a}")
    print(f"   Data Type: {type(a)}")
    
    # Slicing
    print(f"\n2. List Slice [0:4]: {a[0:4]}")
    
    # Append
    a.append("world")
    print(f"\n3. After append('world'): {a}")
    
    # Insert at specific position
    a.insert(2, "python")
    print(f"\n4. After insert(2, 'python'): {a}")
    
    # Length
    print(f"\n5. Length of list: {len(a)}")
    
    # Access last element
    print(f"\n6. Last element (a[-1]): {a[-1]}")
    
    # Remove specific value
    a.remove(6.5)
    print(f"\n7. After remove(6.5): {a}")
    
    # Pop element at index
    popped = a.pop(3)
    print(f"\n8. After pop(3) - Removed: {popped}, List: {a}")
    
    # Filter strings from list
    print(f"\n9. String elements in list:")
    for i in a:
        if type(i) == str:
            print(f"   - {i}")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    demonstrate_lists()
