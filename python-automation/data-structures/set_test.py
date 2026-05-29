#!/usr/bin/env python3
"""
Python Set Operations
Demonstration of set creation, duplicate removal, and conversions.
"""

def demonstrate_sets():
    """
    Showcase various set operations.
    """
    print("=" * 50)
    print("Set Operations Demo")
    print("=" * 50)
    
    # Create a set of names
    user = {"Puja", "Alice", "Bob", "Charlie", "David"}
    print(f"\n1. User Set: {user}")
    print(f"   Data Type: {type(user)}")
    
    # Create a set with duplicate numbers
    num = {11, 1, 2, 1, 111, 8, 7, 9, 8}
    print(f"\n2. Numbers Set (duplicates removed): {num}")
    print(f"   Data Type: {type(num)}")
    print("   Note: Sets automatically remove duplicates")
    
    # List with duplicates
    list1 = [1, 2, 3, 4, 5, 6, 9, 9, 1, 2, 3, 4, 5, 6, 9, 9, 1, 2, 3, 4, 5, 6, 9, 9]
    print(f"\n3. Original List (with duplicates): {list1}")
    print(f"   Length: {len(list1)}")
    
    # Convert list to set to remove duplicates
    list1_set = set(list1)
    print(f"\n4. List converted to Set: {list1_set}")
    print(f"   Data Type: {type(list1_set)}")
    print(f"   Length: {len(list1_set)}")
    
    # Convert back to list
    list1_clean = list(list1_set)
    print(f"\n5. Set converted back to List: {list1_clean}")
    print(f"   Data Type: {type(list1_clean)}")
    print(f"   Length: {len(list1_clean)}")
    print(f"   Duplicates Removed: {len(list1) - len(list1_clean)}")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    demonstrate_sets()
