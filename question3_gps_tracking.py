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

# 
class InMemoryGPS:
    def __init__(self):
        # Dictionary to store data for each officer
        # officer_id -> list of (time, (x, y))
        self.data = {}

        # example
        # self.data={1:[(1,(1,4)),(5,(2,5)),(10,(3,6))],2:[(8,(9,8))]}
     


    def add_location(self, officer_id, time, x, y):
        # If officer does not exist, create empty list


        # xample:

# Officer 1: GPS coordinate (1, 4) sent at time = 1
# Officer 1: GPS coordinate (2, 5) sent at time = 5
# Officer 2: GPS coordinate (9, 8) sent at time = 8
# Officer 1: GPS coordinate (3, 6) sent at time = 10

        if officer_id not in self.data:
            self.data[officer_id] = []

        # Add the GPS record
        # self.data={1:[(1,(1,4)),(5,(2,5)),(10,(3,6))],2:[(8,(9,8))]}
        self.data[officer_id].append((time, (x, y)))

    def get_location(self, officer_id, search_time):
#         If the dispatcher searches for Officer 1 at time = 8, return GPS coordinate (3, 6) sent at time = 10.

   # If the dispatcher searches for Officer 1 at time = 5, return GPS coordinate (2, 5) sent at time = 5.
        # If officer not found, return None
        if officer_id not in self.data:
            return None

        # Get all GPS records for the officer
        # example for officer 1 at time =5
        # records=self.data[1]=[(1,(1,4)),(5,(2,5)),(10,(3,6))]
        records = self.data[officer_id]

        # Go through each record in order.......loop
        for time, coordinate in records:
            # Return the first time that is >= search_time
            if time >= search_time:
                return coordinate

        # If no matching record is found
        return None
