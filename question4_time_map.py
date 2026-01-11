"""
Question 4: Time-Based Key-Value Store (LeetCode 981)
======================================================
Design a time-based key-value data structure that can store multiple values for 
the same key at different timestamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
- TimeMap() Initializes the object
- set(key, value, timestamp) Stores the key with value at given timestamp
- get(key, timestamp) Returns value with largest timestamp_prev <= timestamp

If there are multiple values, returns the value associated with the largest 
timestamp_prev. If there are no values, returns "".

Example:
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);    // store key="foo", value="bar", timestamp=1
timeMap.get("foo", 1);           // return "bar"
timeMap.get("foo", 3);           // return "bar" (timestamp 1 is largest <= 3)
timeMap.set("foo", "bar2", 4);   // store key="foo", value="bar2", timestamp=4
timeMap.get("foo", 4);           // return "bar2"
timeMap.get("foo", 5);           // return "bar2" (timestamp 4 is largest <= 5)
"""





class TimeMap:
    def __init__(self):
        # key -> list of (timestamp, value)
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []

        # Append since timestamps are increasing
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.store:
            return ""

        values = self.store[key]
        result = ""

        # Linear scan to find the largest timestamp <= given timestamp
        for time, value in values:
            if time <= timestamp:
                result = value
            else:
                break

        return result



# Example usage and test cases
if __name__ == "__main__":
    # Create TimeMap instance
    timeMap = TimeMap()
    
    print("Example from LeetCode 981:")
    print("=" * 50)
    
    # Test sequence from the problem
    operations = [
        ("set", ["foo", "bar", 1]),
        ("get", ["foo", 1]),
        ("get", ["foo", 3]),
        ("set", ["foo", "bar2", 4]),
        ("get", ["foo", 4]),
        ("get", ["foo", 5])
    ]
    
    expected_outputs = ["null", "bar", "bar", "null", "bar2", "bar2"]
    
    print("Operations and Results:")
    print("-" * 50)
    
    output_idx = 0
    for op, args in operations:
        if op == "set":
            key, value, timestamp = args
            timeMap.set(key, value, timestamp)
            print(f'timeMap.set("{key}", "{value}", {timestamp})')
            print(f"  Output: null")
            print(f"  Expected: {expected_outputs[output_idx]}\n")
            output_idx += 1
        elif op == "get":
            key, timestamp = args
            result = timeMap.get(key, timestamp)
            expected = expected_outputs[output_idx]
            print(f'timeMap.get("{key}", {timestamp})')
            print(f"  Output: \"{result}\"")
            print(f"  Expected: \"{expected}\"")
            print(f"  Match: {result == expected}\n")
            output_idx += 1
    
    # Additional examples
    print("Additional Examples:")
    print("=" * 50)
    
    # Example 1: Multiple keys
    timeMap.set("user1", "Alice", 10)
    timeMap.set("user1", "Bob", 20)
    timeMap.set("user2", "Charlie", 15)
    
    print('timeMap.set("user1", "Alice", 10)')
    print('timeMap.set("user1", "Bob", 20)')
    print('timeMap.set("user2", "Charlie", 15)\n')
    
    result1 = timeMap.get("user1", 15)
    print(f'timeMap.get("user1", 15) → "{result1}"')
    print(f"  Expected: \"Alice\" (timestamp 10 is largest <= 15)\n")
    
    result2 = timeMap.get("user1", 25)
    print(f'timeMap.get("user1", 25) → "{result2}"')
    print(f"  Expected: \"Bob\" (timestamp 20 is largest <= 25)\n")
    
    # Example 2: Query before any timestamp
    result3 = timeMap.get("user1", 5)
    print(f'timeMap.get("user1", 5) → "{result3}"')
    print(f"  Expected: \"\" (no timestamp <= 5)\n")
    
    # Example 3: Query non-existent key
    result4 = timeMap.get("nonexistent", 100)
    print(f'timeMap.get("nonexistent", 100) → "{result4}"')
    print(f"  Expected: \"\" (key doesn't exist)\n")

