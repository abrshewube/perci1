"""
Question 6: Insert Delete GetRandom O(1) (LeetCode 380)
========================================================
Implement the RandomizedSet class:
- RandomizedSet() Initializes the RandomizedSet object
- insert(val) Inserts an item val into the set if not present. Returns true if 
              the item was not present, false otherwise
- remove(val) Removes an item val from the set if present. Returns true if the 
              item was present, false otherwise
- getRandom() Returns a random element from the current set of elements. Each 
              element must have the same probability of being returned

You must implement the functions such that each function works in average O(1) time complexity.

Strategy:
To achieve O(1) for all operations, we use:
1. A dictionary (val -> index) for O(1) lookup and deletion
2. A list to store values for O(1) random access
3. When removing, swap the element to remove with the last element, then pop

Example:
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1);     // Inserts 1, returns true
randomizedSet.remove(2);     // Returns false, 2 doesn't exist
randomizedSet.insert(2);     // Inserts 2, returns true
randomizedSet.getRandom();   // Should return either 1 or 2 randomly
randomizedSet.remove(1);     // Removes 1, returns true
randomizedSet.insert(2);     // 2 already exists, returns false
randomizedSet.getRandom();   // Should return 2 (only element)
"""


import random


class RandomizedSet:
    """
    A set that supports O(1) insertion, deletion, and random element retrieval.
    
    Uses a combination of dictionary and list:
    - Dictionary: Maps value to its index in the list (for O(1) lookup)
    - List: Stores actual values (for O(1) random access)
    
    When removing, we swap the element with the last element and pop,
    maintaining O(1) average time complexity.
    """
    
    def __init__(self):
        """
        Initialize the RandomizedSet.
        
        Structure:
        - val_to_index: Dictionary mapping value -> index in the values list
        - values: List storing the actual values
        """
        # Dictionary: value -> index in values list
        # Used for O(1) lookup and deletion
        # self.val_to_index={1:0,3:1,6:2}
        self.val_to_index = {}

        # example={1,3,6}
        
        # List: stores the actual values
        # Used for O(1) random access via index
        # sef.values=[1,3,6]
        self.values = []
    
    def insert(self, val):
        """
        Insert an item into the set if not present.
        
        Args:
            val (int): The value to insert
        
        Returns:
            bool: True if the item was not present and was inserted, False otherwise
        
        Time Complexity: O(1) average
        
        Example:
            randomizedSet.insert(1)  # Returns True
            randomizedSet.insert(1)  # Returns False (already exists)
        """
        # Check if value already exists
        if val in self.val_to_index:
            return False
        
        # Add value to the list
        # index=len(self.values)=0
        # index=len(self.values)=1
        
        index = len(self.values)
        self.values.append(val)
        
        # Map value to its index
        self.val_to_index[val] = index
        
        return True
    
    def remove(self, val):
        """
        Remove an item from the set if present.
        
        Strategy: To maintain O(1), we swap the element to remove with the last
        element, then pop from the end of the list.
        
        Args:
            val (int): The value to remove
        
        Returns:
            bool: True if the item was present and was removed, False otherwise
        
        Time Complexity: O(1) average
        
        Example:
            randomizedSet.remove(1)  # Returns True if 1 exists
            randomizedSet.remove(2)  # Returns False if 2 doesn't exist
        """
        # Check if value exists
        if val not in self.val_to_index:
            return False
        
        # Get the index of the value to remove
        # index_to_remove=self.val_to_index[1]=0
        # index_to_remove=self.val_to_index[3]=1
        # index_to_remove=self.val_to_index[6]=2
        index_to_remove = self.val_to_index[val]
        
        # Get the last element in the list
        last_element = self.values[-1]
        
        # Swap: move last element to the position of element to remove
        self.values[index_to_remove] = last_element
        
        # Update the index of the last element in the dictionary
        self.val_to_index[last_element] = index_to_remove
        
        # Remove the value from the end of the list (O(1))
        self.values.pop()
        
        # Remove the value from the dictionary (O(1))
        del self.val_to_index[val]
        
        return True
    
    def getRandom(self):
        """
        Get a random element from the set.
        
        Returns:
            int: A random element from the current set
        
        Time Complexity: O(1)
        
        Precondition: The set is guaranteed to have at least one element
        
        Example:
            randomizedSet.getRandom()  # Returns a random element
        """
        # Use random.choice() to select a random element from the list
        # This is O(1) since we're just accessing a random index
        return random.choice(self.values)


# Example usage and test cases
if __name__ == "__main__":
    print("Example from LeetCode 380:")
    print("=" * 50)
    
    # Create RandomizedSet instance
    randomizedSet = RandomizedSet()
    
    # Test sequence from the problem
    operations = [
        ("insert", 1, True),      # Inserts 1, returns true
        ("remove", 2, False),     # Returns false, 2 doesn't exist
        ("insert", 2, True),      # Inserts 2, returns true
        ("getRandom", None, None), # Should return 1 or 2 (random)
        ("remove", 1, True),      # Removes 1, returns true
        ("insert", 2, False),     # 2 already exists, returns false
        ("getRandom", None, None)  # Should return 2 (only element)
    ]
    
    print("Operations and Results:")
    print("-" * 50)
    
    for i, (op, val, expected) in enumerate(operations):
        if op == "insert":
            result = randomizedSet.insert(val)
            print(f"randomizedSet.insert({val})")
            print(f"  Output: {result}")
            print(f"  Expected: {expected}")
            print(f"  Match: {result == expected}\n")
        
        elif op == "remove":
            result = randomizedSet.remove(val)
            print(f"randomizedSet.remove({val})")
            print(f"  Output: {result}")
            print(f"  Expected: {expected}")
            print(f"  Match: {result == expected}\n")
        
        elif op == "getRandom":
            result = randomizedSet.getRandom()
            print(f"randomizedSet.getRandom()")
            print(f"  Output: {result}")
            if expected is None:
                print(f"  Expected: 1 or 2 (random)" if i == 3 else "  Expected: 2 (only element)")
            print()
    
    # Additional examples
    print("Additional Examples:")
    print("=" * 50)
    
    # Create a new set for additional tests
    test_set = RandomizedSet()
    
    # Insert multiple values
    test_set.insert(10)
    test_set.insert(20)
    test_set.insert(30)
    test_set.insert(40)
    
    print("Inserted values: 10, 20, 30, 40")
    print(f"Current set size: {len(test_set.values)}\n")
    
    # Test getRandom multiple times (should be random)
    print("Random selections (10 samples):")
    random_samples = [test_set.getRandom() for _ in range(10)]
    print(f"  {random_samples}")
    print("  (Should contain values from {10, 20, 30, 40})\n")
    
    # Remove a value
    removed = test_set.remove(20)
    print(f"remove(20): {removed}")
    print(f"Current set size: {len(test_set.values)}")
    print(f"Remaining values: {set(test_set.values)}\n")
    
    # Try to remove non-existent value
    removed = test_set.remove(99)
    print(f"remove(99): {removed}")
    print(f"  (Should be False, 99 doesn't exist)\n")
    
    # Try to insert duplicate
    inserted = test_set.insert(30)
    print(f"insert(30): {inserted}")
    print(f"  (Should be False, 30 already exists)\n")
    
    # Get random from remaining values
    print("Random selections after removal (10 samples):")
    random_samples = [test_set.getRandom() for _ in range(10)]
    print(f"  {random_samples}")
    print("  (Should only contain values from {10, 30, 40})\n")
    
    print("Time Complexity:")
    print("  insert(): O(1) average")
    print("  remove(): O(1) average")
    print("  getRandom(): O(1)")

