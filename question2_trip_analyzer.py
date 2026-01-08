"""
Question 2: Trip Analyzer
==========================
You are given an ordered travel log represented as a list of pairs [city, trip_id].

Design a class TripAnalyzer with a method countTrips(origin, destination) that 
returns the number of times a traveler moved directly from origin to destination 
across all trips.

A leg is defined as a direct movement from one city to the next within the same trip_id.

Example input:
[
    ["Boston", 101],
    ["New York", 101],
    ["Washington", 101],
    ["Seattle", 202],
    ["Portland", 202],
    ["New York", 303],
    ["Boston", 303]
]

Example queries:
countTrips("Boston", "New York") → 1
countTrips("New York", "Washington") → 1
countTrips("Seattle", "Portland") → 1
countTrips("New York", "Boston") → 1
countTrips("Boston", "Washington") → 0  (not direct)
"""


from collections import defaultdict


class TripAnalyzer:
    """
    Analyzes travel logs to count direct trips between cities.
    
    Processes an ordered list of [city, trip_id] pairs and tracks
    direct movements (legs) between consecutive cities within the same trip.
    """
    
    def __init__(self, travel_log):
        """
        Initialize the analyzer with a travel log.
        
        Args:
            travel_log (list): List of [city, trip_id] pairs in chronological order
        
        The constructor processes the log to build a dictionary mapping
        (origin, destination) pairs to their occurrence count.
        """
        # Dictionary to count occurrences of (origin, destination) pairs
        # Key: (origin_city, destination_city), Value: count
        self.trip_count = defaultdict(int)
        
        # Process the travel log to extract direct trips (legs)
        self._process_travel_log(travel_log)
    
    def _process_travel_log(self, travel_log):
        """
        Process the travel log to identify and count direct trips.
        
        For each trip_id, we look at consecutive cities to identify legs.
        A leg is a direct movement from one city to the next within the same trip.
        
        Args:
            travel_log (list): List of [city, trip_id] pairs
        """
        # Group entries by trip_id to process each trip separately
        trips = defaultdict(list)
        
        # Group cities by their trip_id
        for city, trip_id in travel_log:
            trips[trip_id].append(city)
        
        # For each trip, identify consecutive city pairs (legs)
        for trip_id, cities in trips.items():
            # Iterate through consecutive pairs in the trip
            # If a trip has cities [A, B, C], we get legs: A→B and B→C
            for i in range(len(cities) - 1):
                origin = cities[i]
                destination = cities[i + 1]
                
                # Count this leg (direct trip)
                self.trip_count[(origin, destination)] += 1
    
    def countTrips(self, origin, destination):
        """
        Returns the number of times a traveler moved directly from origin to destination.
        
        Args:
            origin (str): The starting city
            destination (str): The destination city
        
        Returns:
            int: Number of direct trips from origin to destination across all trips
        
        Example:
            analyzer.countTrips("Boston", "New York")  # Returns 1
        """
        return self.trip_count.get((origin, destination), 0)


# Example usage and test cases
if __name__ == "__main__":
    # Example input from the problem
    travel_log = [
        ["Boston", 101],
        ["New York", 101],
        ["Washington", 101],
        ["Seattle", 202],
        ["Portland", 202],
        ["New York", 303],
        ["Boston", 303]
    ]
    
    # Create the analyzer
    analyzer = TripAnalyzer(travel_log)
    
    # Test cases from the problem
    print("Test Cases:")
    print("=" * 50)
    
    # Test 1: Boston → New York (trip 101)
    result1 = analyzer.countTrips("Boston", "New York")
    print(f'countTrips("Boston", "New York") → {result1}')
    print(f"  Expected: 1 (from trip 101: Boston → New York)\n")
    
    # Test 2: New York → Washington (trip 101)
    result2 = analyzer.countTrips("New York", "Washington")
    print(f'countTrips("New York", "Washington") → {result2}')
    print(f"  Expected: 1 (from trip 101: New York → Washington)\n")
    
    # Test 3: Seattle → Portland (trip 202)
    result3 = analyzer.countTrips("Seattle", "Portland")
    print(f'countTrips("Seattle", "Portland") → {result3}')
    print(f"  Expected: 1 (from trip 202: Seattle → Portland)\n")
    
    # Test 4: New York → Boston (trip 303)
    result4 = analyzer.countTrips("New York", "Boston")
    print(f'countTrips("New York", "Boston") → {result4}')
    print(f"  Expected: 1 (from trip 303: New York → Boston)\n")
    
    # Test 5: Boston → Washington (should be 0, not direct)
    result5 = analyzer.countTrips("Boston", "Washington")
    print(f'countTrips("Boston", "Washington") → {result5}')
    print(f"  Expected: 0 (Boston → Washington is not direct, goes through New York)\n")
    
    # Additional example: Show all trips in the log
    print("All trips in the log:")
    print("  Trip 101: Boston → New York → Washington")
    print("  Trip 202: Seattle → Portland")
    print("  Trip 303: New York → Boston")
    print("\n  Direct legs extracted:")
    print("    Boston → New York (1 time)")
    print("    New York → Washington (1 time)")
    print("    Seattle → Portland (1 time)")
    print("    New York → Boston (1 time)")

