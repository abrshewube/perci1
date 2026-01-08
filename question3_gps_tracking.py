"""
Question 3: GPS Tracking API
=============================
We are building an in-memory API to support two use cases:
1. Officers wear GPS devices that stream location data to our system in real-time
2. Dispatchers want to know where a specific officer was at a specific point in time

If the dispatcher searches for an officer at a given time, we return the GPS 
coordinate from the most recent update that was sent at or before that time.

Example:
Officer 1: GPS coordinate (1, 4) sent at time = 1
Officer 1: GPS coordinate (2, 5) sent at time = 5
Officer 2: GPS coordinate (9, 8) sent at time = 8
Officer 1: GPS coordinate (3, 6) sent at time = 10

Query: Officer 1 at time = 8 → Returns (2, 5) from time = 5
Query: Officer 1 at time = 5 → Returns (2, 5) from time = 5
Query: Officer 1 at time = 12 → Returns (3, 6) from time = 10
"""


from collections import defaultdict
from bisect import bisect_right


class GPSTrackingSystem:
    """
    In-memory GPS tracking system for officers.
    
    Stores location updates from officers and allows queries for officer
    locations at specific points in time.
    """
    
    def __init__(self):
        """
        Initialize the GPS tracking system.
        
        Structure:
        - officer_locations: Dict mapping officer_id -> list of (timestamp, (x, y)) tuples
                             The list is kept sorted by timestamp for efficient queries
        """
        # Dictionary: officer_id -> list of (timestamp, (x, y)) tuples
        # Each list is sorted by timestamp
        self.officer_locations = defaultdict(list)
    
    def update_location(self, officer_id, x, y, timestamp):
        """
        Record a GPS location update for an officer at a specific timestamp.
        
        Args:
            officer_id (int): ID of the officer
            x (float): X coordinate of GPS location
            y (float): Y coordinate of GPS location
            timestamp (int): Timestamp when this location was recorded
        
        Example:
            system.update_location(1, 1, 4, 1)  # Officer 1 at (1,4) at time 1
        """
        # Store the location update
        # Format: (timestamp, (x, y))
        self.officer_locations[officer_id].append((timestamp, (x, y)))
        
        # Keep the list sorted by timestamp for efficient binary search
        # Since updates come in chronological order typically, we can just
        # check if we need to sort, but for safety we'll sort after each insert
        # (In production, you might use bisect.insort for better performance)
        self.officer_locations[officer_id].sort(key=lambda item: item[0])
    
    def get_location(self, officer_id, timestamp):
        """
        Get the location of an officer at a specific timestamp.
        
        Returns the GPS coordinate from the most recent update that was sent
        at or before the requested timestamp.
        
        Args:
            officer_id (int): ID of the officer to query
            timestamp (int): Timestamp to query
        
        Returns:
            tuple: (x, y) GPS coordinates, or None if no location data exists
        
        Example:
            system.get_location(1, 8)  # Returns (2, 5) from time 5
        """
        # Check if we have any location data for this officer
        if officer_id not in self.officer_locations:
            return None
        
        locations = self.officer_locations[officer_id]
        
        # If no locations exist, return None
        if not locations:
            return None
        
        # Use binary search to find the rightmost location with timestamp <= query timestamp
        # We'll iterate backwards from the end to find the most recent valid location
        
        # Find the insertion point (rightmost position where timestamp <= query timestamp)
        # bisect_right returns the position after the last element <= timestamp
        pos = bisect_right(locations, timestamp, key=lambda item: item[0])
        
        # If pos is 0, all locations have timestamp > query timestamp
        if pos == 0:
            return None
        
        # Return the location at position pos-1 (the last location <= timestamp)
        _, coordinates = locations[pos - 1]
        return coordinates


# Example usage and test cases
if __name__ == "__main__":
    # Create the GPS tracking system
    system = GPSTrackingSystem()
    
    # Add location updates from the example
    system.update_location(1, 1, 4, 1)   # Officer 1: (1, 4) at time 1
    system.update_location(1, 2, 5, 5)   # Officer 1: (2, 5) at time 5
    system.update_location(2, 9, 8, 8)   # Officer 2: (9, 8) at time 8
    system.update_location(1, 3, 6, 10)  # Officer 1: (3, 6) at time 10
    
    print("GPS Location Updates:")
    print("=" * 50)
    print("Officer 1: (1, 4) at time 1")
    print("Officer 1: (2, 5) at time 5")
    print("Officer 2: (9, 8) at time 8")
    print("Officer 1: (3, 6) at time 10\n")
    
    # Test queries
    print("Test Queries:")
    print("=" * 50)
    
    # Query 1: Officer 1 at time = 8
    result1 = system.get_location(1, 8)
    print(f"Officer 1 at time 8: {result1}")
    print(f"  Expected: (2, 5) from time 5 (most recent update at or before time 8)\n")
    
    # Query 2: Officer 1 at time = 5
    result2 = system.get_location(1, 5)
    print(f"Officer 1 at time 5: {result2}")
    print(f"  Expected: (2, 5) from time 5 (exact match)\n")
    
    # Query 3: Officer 1 at time = 1
    result3 = system.get_location(1, 1)
    print(f"Officer 1 at time 1: {result3}")
    print(f"  Expected: (1, 4) from time 1 (exact match)\n")
    
    # Query 4: Officer 1 at time = 10
    result4 = system.get_location(1, 10)
    print(f"Officer 1 at time 10: {result4}")
    print(f"  Expected: (3, 6) from time 10 (exact match)\n")
    
    # Query 5: Officer 1 at time = 12 (future time)
    result5 = system.get_location(1, 12)
    print(f"Officer 1 at time 12: {result5}")
    print(f"  Expected: (3, 6) from time 10 (most recent available)\n")
    
    # Query 6: Officer 1 at time = 0 (before any updates)
    result6 = system.get_location(1, 0)
    print(f"Officer 1 at time 0: {result6}")
    print(f"  Expected: None (no location data before time 1)\n")
    
    # Query 7: Officer 2 at time = 8
    result7 = system.get_location(2, 8)
    print(f"Officer 2 at time 8: {result7}")
    print(f"  Expected: (9, 8) from time 8 (exact match)\n")
    
    # Query 8: Officer 2 at time = 10
    result8 = system.get_location(2, 10)
    print(f"Officer 2 at time 10: {result8}")
    print(f"  Expected: (9, 8) from time 8 (most recent available)\n")

