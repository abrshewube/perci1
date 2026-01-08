Question 1 (George 1)

The battery sizing team has developed a body cam usage procedure and has tested this procedure on a camera hooked up to a power supply.
Sensor data for this camera gives you a list of time intervals (in seconds),
and a corresponding list of average current draw in milli-amps over those intervals.
Describe an object model that lets you find the total energy in milli-amp hours, from time 0 to T. The list of time intervals can be arbitrarily long, and you may want to be able to repeatedly query the power used at different times.
Example:
Seconds Average Power
0-300 125mA
300-400 50mA
400-550 500mA
550-1000 20mA
The total energy usage from T=0 to T=700s is 33.47mAH (milli amp hours)
(300*125 + 100*50 + 150*500 + 150*20)/(3600) = 33.47














Question 2 (George 2)

You are given an ordered travel log represented as a list of pairs
[city, trip_id], where:

city is the location visited,

trip_id uniquely identifies a single trip,

entries with the same trip_id appear in the order they were visited.

Each trip may consist of multiple legs. A leg is defined as a direct movement from one city to the next within the same trip_id.

Design a class TripAnalyzer with a method countTrips(origin, destination) that returns the number of times a traveler moved directly from origin to destination across all trips.
Example input
[
["Boston", 101],
["New York", 101],
["Washington", 101],
["Seattle", 202],
["Portland", 202],
["New York", 303],
["Boston", 303]
]

Example queries
countTrips("Boston", "New York") → 1
countTrips("New York", "Washington") → 1
countTrips("Seattle", "Portland") → 1
countTrips("New York", "Boston") → 1
countTrips("Boston", "Washington") → 0

Question 3 (Bolutife, Winnie)

We are building an in-memory API to support two use cases.
We have users (officers) that wear a GPS device that streams location data to our system in real-time.We also have users (dispatchers) who want to know where a specific officer was at a specific point in time.
Example:

Officer 1: GPS coordinate (1, 4) sent at time = 1
Officer 1: GPS coordinate (2, 5) sent at time = 5
Officer 2: GPS coordinate (9, 8) sent at time = 8
Officer 1: GPS coordinate (3, 6) sent at time = 10

If the dispatcher searches for Officer 1 at time = 8, return GPS coordinate (3, 6) sent at time = 10.

If the dispatcher searches for Officer 1 at time = 5, return GPS coordinate (2, 5) sent at time = 5.

















Question 4 (Ammar)

981. Time Based Key-Value Store
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
Implement the TimeMap class:
TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 
Example 1:
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"





Question 5 (Jermaine)
The evidence review team is analyzing body-camera recording sessions to understand how often cameras transition between recording states during a shift.
Each camera sends state change events to the system in chronological order.
A state change event consists of:
camera_id
state (one of "recording", "paused", "off")
timestamp (in seconds)
Once a camera enters a state, it remains in that state until the next state change event for that camera.
Dispatch supervisors want to query the system to determine how long a given camera spent in a specific state within a time window.
Example events
Camera 7 enters "recording" at time = 0
Camera 7 enters "paused" at time = 300
Camera 7 enters "recording" at time = 450
Camera 7 enters "off" at time = 900

Example question
getStateDuration(camera_id = 7, state = "recording", start = 0, end = 700)

Result 
550 seconds






Question 6 (Oluwatomisin)
Implement the RandomizedSet class:
RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns trueif the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns trueif the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity. 
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 Constraints:
-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called
