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

class TripAnalyzer:
    """
    Analyzes travel logs to count direct trips between cities.
    """

    def __init__(self, travel_log):
        # Dictionary to store counts of (origin, destination)
        # Key: (origin, destination), Value: count
        self.trip_count = {}

        # Process the travel log
        self._process_travel_log(travel_log)

    def _process_travel_log(self, travel_log):
        """
        Process the travel log to identify direct legs.
        """

        # Group cities by trip_id
        trips = {}
        for city, trip_id in travel_log:
            if trip_id not in trips:
                trips[trip_id] = []
            trips[trip_id].append(city)

        # Count consecutive city pairs (legs) for each trip
        for trip_id in trips:
            cities = trips[trip_id]
            for i in range(len(cities) - 1):
                origin = cities[i]
                destination = cities[i + 1]
                key = (origin, destination)

                if key not in self.trip_count:
                    self.trip_count[key] = 0
                self.trip_count[key] += 1

    def countTrips(self, origin, destination):
        """
        Return the number of direct trips from origin to destination.
        """
        key = (origin, destination)
        if key in self.trip_count:
            return self.trip_count[key]
        return 0


# Example usage
if __name__ == "__main__":
    travel_log = [
        ["Boston", 101],
        ["New York", 101],
        ["Washington", 101],
        ["Seattle", 202],
        ["Portland", 202],
        ["New York", 303],
        ["Boston", 303]
    ]

    analyzer = TripAnalyzer(travel_log)

    print(analyzer.countTrips("Boston", "New York"))      # 1
    print(analyzer.countTrips("New York", "Washington"))  # 1
    print(analyzer.countTrips("Seattle", "Portland"))     # 1
    print(analyzer.countTrips("New York", "Boston"))      # 1
    print(analyzer.countTrips("Boston", "Washington"))    # 0
